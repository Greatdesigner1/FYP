from django.shortcuts import render
from rest_framework import viewsets
from students.models import Session, Student , Attendance
from .serializers import SessionSreializer, StudentSerializer, StudentUpdateSerializer,CaptureSerializer,VerifyFingerSerializer, AttendanceSerializer
from .utils import capture_fingerprint , verify_fingerprint
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime


# Create your views here.


class StudentsViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = [FormParser,MultiPartParser]
    http_method_names = ['post', 'patch', 'delete','get']
    lookup_field = 'matric_no'

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return StudentUpdateSerializer
        return super().get_serializer_class()
    
    @action(
        methods=["GET"],
        detail=True,
        permission_classes = [IsAuthenticated],
        serializer_class = CaptureSerializer,
    )
    @swagger_auto_schema(
        operation_summary='used to register user fingerprint',
        manual_parameters=[
            openapi.Parameter(
                'right',
                openapi.IN_QUERY,
                description="Filter by order status (true/false)",
                type=openapi.TYPE_STRING,
                enum=[True,False]
            )
        ]
    )
    def startCapture(self,request, matric_no):
        try:
            isRight = request.GET.get("right", 0)
            matric_no=  f'{matric_no[0::3]}/{matric_no[2::]}'
            student  = Student.objects.get(matric_no=matric_no) #change to getorthrow
            response = capture_fingerprint()
            data = response.json()

            if data.get('NFIQ') <=3:
                if isRight:
                    student.right_fingerprint = data.get('TemplateBase64')
                else:
                    student.left_fingerprint = data.get('TemplateBase64')
                student.save()
                return Response({"message": "Captured finger Succesfully"},status=200)
            else:
                return Response({"message":"Please capture again"}, status=200)      
        except Exception as e :
            return Response({"message": str(e)}, status=400)

    @action(
        methods=["POST"],
        detail=True,
        permission_classes = [IsAuthenticated],
        serializer_class = VerifyFingerSerializer,
    )  
    def verifyCapture(self, request, matric_no):
        try:
            matric_no=  f'{matric_no[0::3]}/{matric_no[2::]}'
            student  = Student.objects.get(matric_no = matric_no) #change to getorthrow
            serializer = self.get_serializer(data = request.data)
            if serializer.is_valid(raise_exception = True): 
                print(serializer.validated_data)    
                session = get_object_or_404(Session, id = serializer.validated_data['session_id'])
                Attendance.objects.get_or_create(session= session, student = student)
            response = capture_fingerprint()
            data = response.json()

            if data.get('NFIQ') <=3:
                captured_fingerprint = data.get('TemplateBase64')

                if verify_fingerprint(student.left_fingerprint,captured_fingerprint) or verify_fingerprint(student.right_fingerprint,captured_fingerprint):
                    Attendance.objects.get_or_create(student = student , )
                    serializer = StudentSerializer(student)
                    return Response(serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'message': 'Fingerprint does not match'},status=HTTP_400_BAD_REQUEST )
            else:
                return Response({"message":"Please capture again"}, status=200)      
        except Exception as e :
            return Response({"message": str(e)}, status=400)
        
    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[IsAuthenticated],
        serializer_class=AttendanceSerializer,
    )
    @swagger_auto_schema(
        operation_summary='Get attendance list for a session',
        manual_parameters=[
            openapi.Parameter('session_id', openapi.IN_QUERY, description="Session UUID", type=openapi.FORMAT_UUID),
            openapi.Parameter('date', openapi.IN_QUERY, description="Date of session (YYYY-MM-DD)", type=openapi.TYPE_STRING),
            openapi.Parameter('status', openapi.IN_QUERY, description="Filter by attendance status (present/absent)", type=openapi.TYPE_STRING)
        ]
    )
    def get_attendace(self, request, *args, **kwargs):
        session_id = request.query_params.get('session_id')
        date_str = request.query_params.get('date')
        status_filter = request.query_params.get('status')

        # Fetch session
        session = None
        if date_str:
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

            session = Session.objects.filter(date=date_obj).first()
            if not session:
                return Response({"error": "No session found for the given date."}, status=404)
        elif session_id:
            session = get_object_or_404(Session, id=session_id)
        else:
            session = Session.objects.last()

        # Get students and attendance
        all_students = Student.objects.all()
        attendance_records = Attendance.objects.filter(session=session)
        attendance_lookup = {att.student.matric_no: att for att in attendance_records}

        # Prepare response data
        data = []
        for student in all_students:
            attendance = attendance_lookup.get(student.matric_no)
            present = attendance is not None

            # Filter by status if provided
            if status_filter == "present" and not present:
                continue
            elif status_filter == "absent" and present:
                continue

            data.append({
                "name": student.name,
                "matric_no": student.matric_no,
                "level": student.level,
                "faculty": student.course,
                "date": session.date,
                "status": present,
                "attendance_time": attendance.created_at if present else None
            })

        return Response(data, status=HTTP_200_OK)



class SessionViewset(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSreializer
    http_method_names = ['post', 'delete']


    

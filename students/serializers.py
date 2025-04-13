import re

from datetime import datetime
from typing import Required
from .models import Session, Student, Attendance
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "left_fingerprint","right_fingerprint"]

class VerifyFingerSerializer(serializers.Serializer):
    session_id = serializers.IntegerField(required=True)

class StudentUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    matric_no = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"


class SessionSreializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "day", "period"]

    def create(self, validated_data):
        now = datetime.now()
        day = now.strftime("%A")  # e.g., Monday
        hour = now.hour

        if 5 <= hour < 12:
            period = "MORNING"
        else:
            period = "EVENING"
        
        validated_data['day'] = day.upper()
        validated_data['period'] = period
        return super().create(validated_data)


class CaptureSerializer(serializers.Serializer):
    message = serializers.CharField()

class AttendanceSerializer(serializers.Serializer):
    name = serializers.CharField()
    matric_no = serializers.CharField()
    level = serializers.CharField()
    faculty = serializers.CharField()
    date = serializers.DateField()
    status = serializers.BooleanField()
    attendance_time = serializers.DateTimeField()
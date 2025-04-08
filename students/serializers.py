import re
from typing import Required
from .models import Session, Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    matric_no = serializers.CharField(required=False)

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class SessionSreializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]


class SessionUpdateSerializer(serializers.ModelSerializer):
    day = serializers.ChoiceField(choices=Session.Day.choices, required=False)
    period = serializers.ChoiceField(
        choices=Session.Period.choices, required=False)
    chapel = serializers.PrimaryKeyRelatedField(
        queryset=Session.objects.all(), required=False)

    class Meta:
        model = Session
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

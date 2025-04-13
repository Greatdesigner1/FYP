import uuid
from django.db import models

from users.models import GENDERS, LEVEL, TimeStamp

# Create your models here.


class Chapel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    pastor = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(TimeStamp):

    class Faculty(models.TextChoices):
        ARTS = "ARTS", "Arts and Humanities"
        SCIENCE = "SCIENCE", "Science and Technology"
        SOCIAL_SCIENCE = "SOCIAL_SCIENCE", "Social Science"
        ENGINEERING = "ENGINEERING", "Engineering"
        LAW = "LAW", "Law"
        MEDICAL_SCIENCES = "MEDICAL_SCIENCES", "Medical Sciences"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    matric_no = models.CharField(max_length=20, unique=True)
    gender = models.CharField(
        max_length=20, choices=GENDERS, null=False, blank=False, default="MALE"
    )
    level = models.CharField(max_length=20, choices=LEVEL, default="100")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    course = models.CharField(
        max_length=50, choices=Faculty.choices, default=Faculty.ARTS)
    left_fingerprint = models.TextField(blank=True, null=True)
    right_fingerprint = models.TextField(blank=True, null=True)
    chapel = models.ForeignKey(
        Chapel, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.id


class Session(TimeStamp):

    class Period(models.TextChoices):
        MORNING = "MORNING", "Morning"
        EVENING = "EVENING", "Evening"

    class Day(models.TextChoices):
        MONDAY = "MONDAY", "Monday"
        TUESDAY = "TUESDAY", "Tuesday"
        WEDNESDAY = "WEDNESDAY", "Wednesday"
        THURSDAY = "THURSDAY", "Thursday"
        FRIDAY = "FRIDAY", "Friday"
        SATURDAY = "SATURDAY", "Saturday"
        SUNDAY = "SUNDAY", "Sunday"

    day = models.CharField(max_length=20, choices=Day.choices)
    period = models.CharField(max_length=20, choices=Period.choices)
    chapel = models.ForeignKey(
        Chapel, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['date','period',]


class Attendance(TimeStamp):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.session}"

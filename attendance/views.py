from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, Student, CourseRegistration
from datetime import date as currentDate

class TakeAttendance(APIView):
    def post(self, request):
        # Extract data from the request
        student_id = request.data.get('student_id')
        status = request.data.get('status')
        course_code = request.data.get('course_code')

        # Get the current date
        current_date = currentDate.today()

        # Retrieve the student and course objects
        try:
            student = Student.objects.get(id=student_id)
            course_registration = CourseRegistration.objects.get(course_code=course_code, student=student)
        except Student.DoesNotExist:
            return Response({'error': 'Student does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except CourseRegistration.DoesNotExist:
            return Response({'error': 'Student is not registered for this course'}, status=status.HTTP_404_NOT_FOUND)

        # Validate the status
        if status not in [0, 1]:
            return Response({'error': 'Invalid status. Status must be 0 (Absent) or 1 (Present)'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the attendance record
        attendance = Attendance.objects.create(
            date=current_date,
            student=student,
            status=status,
            course_code=course_registration.course_code  # Assuming course_code is a field in CourseRegistration model
        )

        return Response({'message': 'Attendance recorded successfully'}, status=status.HTTP_201_CREATED)

# Example usage
from datetime import date
from account.models import Student
from .models import Attendance
from rest_framework.views import APIView
from account.models import Student, Faculty, CourseRegistration
from django.http import JsonResponse
from rest_framework.response import Response
from datetime import date


def process_attendance_data(data):
    course_name = data.get('course_name')

    students_data = data.get('students', [])
    for student_data in students_data:
        student_roll_no = student_data.get('roll_no')
        status = student_data.get('status')

        # Check if roll_no and status are provided
        if student_roll_no is None or status is None:
            continue

        try:
            student = Student.objects.get(id=student_roll_no)
            # Create Attendance object
            Attendance.objects.create(
                date=date.today(),
                student=student,
                status=status,
                course_name=course_name
            )
        except Student.DoesNotExist:
            print(f"Student with roll_no {student_roll_no} does not exist.")

class HandleAttendance(APIView):
    def post(self, request):
        data = request.data
        
        # Process the attendance data
        process_attendance_data(data)

        return JsonResponse({'message': 'Attendance data processed successfully'})




class CourseStudent(APIView):
    def post(self, request):
        course_name = request.data.get('course_name')

        # Query CourseRegistration objects for the given course name
        registrations = CourseRegistration.objects.filter(course_name=course_name)

        # Extract student names and roll numbers from registrations
        students_data = []
        for registration in registrations:
            student = registration.student
            students_data.append({
                'name': student.name,
                'roll_no': student.id,
                'status':0
            })



        # Return JsonResponse with student data
        return JsonResponse({'students': students_data})

# Example usage
from datetime import date
from account.models import Student
from .models import Attendance
from rest_framework.views import APIView
from account.models import Student, Faculty, CourseRegistration
from django.http import JsonResponse
from rest_framework.response import Response




# def create_attendance(student_instance, date, status, course_name):
#     try:
#         # Create attendance record
#         attendance = Attendance.objects.create(
#             student=student_instance,
#             date=date,
#             status=status,
#             course_name=course_name
#         )
#         return attendance
#     except Exception as e:
#         # Handle exception (e.g., IntegrityError, ValidationError)
#         print(f"Error creating attendance record: {e}")
#         return None

# class Take_attandance(APIView):
#     def post(self, request):
        # Assuming student_instance is an instance of the Student model
        # student_instance = Student.objects.get(id=1)
        # date = date.today()  # or any other date
        # status = 1  # 1 for Present, 0 for Absent
        # course_name = "CS101"

        # Create attendance record
        # attendance_record = create_attendance(student_instance, date, status, course_name)
        # if attendance_record:
        #     print("Attendance record created successfully")
        # else:
        #     print("Failed to create attendance record")



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
                'roll_no': student.id
            })



        # Return JsonResponse with student data
        return JsonResponse({'students': students_data})

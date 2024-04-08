# Example usage
from datetime import date
from account.models import Student
from .models import Attendance
from rest_framework.views import APIView
from account.models import Student, Faculty, CourseRegistration
from django.http import JsonResponse
from rest_framework.response import Response
from datetime import date, datetime

from rest_framework.decorators import api_view
from django.db.models import Q


# @api_view(['POST'])
class LeaveApproved(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        start_date_str = request.data.get('start_date')
        end_date_str = request.data.get('end_date')

        if student_id is None or start_date_str is None or end_date_str is None:
            return Response({'error': 'student_id, start_date, and end_date are required'}, status=400)

        try:
            student_id = int(student_id)
        except ValueError:
            return Response({'error': 'student_id must be an integer'}, status=400)

        try:
            start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
            end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()
        except ValueError:
            return Response({'error': 'start_date and end_date must be in dd-mm-yyyy format'}, status=400)

        attendance_records = Attendance.objects.filter(
            student_id=student_id,
            date__range=[start_date, end_date]
        )

        for record in attendance_records:
            record.status = 1
            record.save()

        return Response({'message': 'Attendance marked as Present for the specified date range'}, status=200)



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
        print(request.data)

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
    


from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count
from attendance.models import Attendance
from account.models import Student
from rest_framework.views import APIView
from django.db.models import Q


@method_decorator(csrf_exempt, name='dispatch')
class AttendanceStatsView(APIView):
    def post(self, request):
        # Get student_id from request data
        email_id = request.data.get('email_id')
        student_id = Student.objects.filter(email_id=email_id)[0].id

        if not student_id:
            return JsonResponse({'error': 'Student ID not provided'}, status=400)

        # Calculate attendance stats for the given student
        stats = self.calculate_attendance_stats(student_id)

        Response = response()
        Response.data = {
            'course':stats
        }

        # Return the data as JSON response
        return Response

    def calculate_attendance_stats(self, student_id):
        # Retrieve attendance data for the given student
        attendance_data = Attendance.objects.filter(student_id=student_id)
        
        # Calculate the number of present and absent days for each course
        course_attendance_stats = attendance_data.values('course_name').annotate(
            present=Count('status', filter=Q(status=1)),
            absent=Count('status', filter=Q(status=0))
        )
        
        # Format the data
        course_stats_formatted = [
            {
                'name': course['course_name'],
                'present': course['present'],
                'absent': course['absent']
            }
            for course in course_attendance_stats
        ]
        
        return course_stats_formatted

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Administration
from account.models import Student
from rest_framework.response import Response
from datetime import datetime

from rest_framework import status
from .models import AppliedLeave


class AppliedLeaveView(APIView):
    def post(self, request, format=None):
        # Extract data from the request
        student_id = request.data.get('student_id')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        # Convert date strings to date objects
        try:
            start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
            end_date = datetime.strptime(end_date, '%d-%m-%Y').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Please provide dates in dd-mm-yyyy format'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an instance of AppliedLeave and save it to the database
        applied_leave = AppliedLeave.objects.create(
            student_id=student_id,
            start_date=start_date,
            end_date=end_date
        )

        # Return a success response
        return Response({'message': 'Applied leave created successfully'}, status=status.HTTP_201_CREATED)


# Create your views here.
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = Administration.objects.filter(email_id=email).first()


        response = Response()

        if user is None:
            response.status_code=400
            response.data = {
                "allowed":"no",
                "message": "Email not found"
            }
            return response

        if not user.check_password(password):
            response.status_code=400
            response.data = {
                "allowed":"no",
                "message": "Incorrect Password"
            }
            return response

        response.status_code = 200
        response.data = {
            "allowed":"yes",
            "email_id": user.email_id,
        }

        applied_leaves = AppliedLeave.objects.all()

        # Create a list to store formatted data
        leave_list = []

        # Iterate through each applied leave
        for leave in applied_leaves:
            # Get the student associated with the leave
            student = Student.objects.get(id=leave.student_id)

            # Format the data
            leave_data = {
                'student_id': student.id,
                'student_name': student.name,
                'start_date': leave.start_date,
                'end_date': leave.end_date,
                'status':0
            }

            # Append the formatted data to the list
            leave_list.append(leave_data)

            response.data['leave_list']=leave_list


        return response
    

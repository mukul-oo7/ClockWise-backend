from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Faculty, CourseRegistration
import jwt, datetime, time
from .serializers import StudentSerializer, FacultySerializer
from rest_framework import status



# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        if request.data['cat'] == 'Student' :
            serializer = StudentSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()

            return Response(serializer.data)
        
        if request.data['cat'] == 'Faculty' :
            serializer = FacultySerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()

            return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        cat = request.data.get('cat')

        if cat == "Student":
            user = Student.objects.filter(email_id=email).first()

        if cat == "Faculty":
            user = Faculty.objects.filter(email_id=email).first()

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

        current_timestamp = int(time.time())

        payload = {
            "id": str(user.id),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            "iat": current_timestamp,
        }

        encoded_token = jwt.encode(payload, 'secret', 'HS256')


        # response.headers['Authorization'] = 'Bearer '+ encoded_token

        response.status_code = 200
        response.data = {
            "allowed":"yes",
            "user_id": user.id,
        }

        if cat == 'Faculty':
            response.data['cat']='Faculty'

        if cat == 'Student':
            response.data['cat']='Student'


        return response


class RegisterCourse(APIView):
    def post(self, request):
        print(request)
        cr_name = request.data.get('course_name')
        start_id = request.data.get('start_id')
        end_id = request.data.get('end_id')

        print(cr_name, " ", start_id, " ", end_id)


        students = Student.objects.filter(id__range=(start_id, end_id))

        for student in students:
            try:
                registration = CourseRegistration.objects.create(
                    student=student,
                    course_name=cr_name
                )
            except Exception as e:
                return Response({'error': f'Error registering {student.name} for the course: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # for student in students:
        #     print(student.name)
        #     CourseRegistration.create_registration(student=student, course_name="cr_name")

        response = Response()

        response.status_code = 200
        response.data = {
            'message': 'Course registration successful'
        }

        return response
    
# Example usage
from datetime import date
from account.models import Student
from .models import Attendance

def create_attendance(student_instance, date, status, course_name):
    try:
        # Create attendance record
        attendance = Attendance.objects.create(
            student=student_instance,
            date=date,
            status=status,
            course_name=course_name
        )
        return attendance
    except Exception as e:
        # Handle exception (e.g., IntegrityError, ValidationError)
        print(f"Error creating attendance record: {e}")
        return None

class Take_attandance(APIView):
    def post:
        # Assuming student_instance is an instance of the Student model
        student_instance = Student.objects.get(id=1)
        date = date.today()  # or any other date
        status = 1  # 1 for Present, 0 for Absent
        course_name = "CS101"

        # Create attendance record
        attendance_record = create_attendance(student_instance, date, status, course_name)
        if attendance_record:
            print("Attendance record created successfully")
        else:
            print("Failed to create attendance record")

import json
import datetime
from app.student import StudentUser
# Corrected Import: TeacherUser and Course now come from the same file.
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.attendance_log = []
        self.next_lesson_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # The logic here remains the same, but the source of the Course class has changed.
                # TODO: For each dictionary in data['students'], create a StudentUser object and append to self.students.
                self.students = []
                for student_data in data.get("students", []):
                    student = StudentUser(student_data["id"], student_data["name"])
                    student.enrolled_course_ids = student_data.get("enrolled_course_ids", [])
                    self.students.append(student)

                # TODO: Do the same for teachers (creating TeacherUser objects).
                self.teachers = []
                for teacher_data in data.get("teachers", []):
                    teacher = TeacherUser(
                        teacher_data["id"],
                        teacher_data["name"],
                        teacher_data["speciality"]
                    )
                    self.teachers.append(teacher)

                # TODO: Do the same for courses (creating Course objects).
                self.courses = []
                for course_data in data.get("courses", []):
                    course = Course(
                        course_data["id"],
                        course_data["name"],
                        course_data["instrument"],
                        course_data["teacher_id"]
                    )
                    course.enrolled_student_ids = course_data.get("enrolled_student_ids", [])
                    course.lessons = course_data.get("lessons", [])
                    self.courses.append(course)

                # Load attendance
                self.attendance_log = data.get("attendance", [])

        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # The logic here remains the same.
        # TODO: Create a 'data_to_save' dictionary.
        # Convert self.students, self.teachers, and self.courses into lists of dictionaries.
        # Write the result to the JSON file.
        data_to_save = {
                    "students": [s.__dict__ for s in self.students],
                    "teachers": [t.__dict__ for t in self.teachers],
                    "courses": [c.__dict__ for c in self.courses],
                    "attendance": self.attendance_log
                }
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def register_new_student(self, name, instrument):
        name = name.strip()
        instrument = instrument.strip()

        if not name or not instrument:
            return None

        # Extra function: check that a teacher specialises in the requested instrument.
        for teacher in self.teachers:
            if teacher.speciality.lower() == instrument.lower():
                break
        else:
            return None

        # Generate a new student ID.
        if self.students:
            new_student_id = max(student.id for student in self.students) + 1
        else:
            new_student_id = 1

        # Create the new student.
        new_student = StudentUser(new_student_id, name)
        self.students.append(new_student)
        self._save_data()

        return new_student

    def check_in(self, student_id, course_id):
        student = None
        course = None

        # Find the student.
        for s in self.students:
            if s.id == student_id:
                student = s
                break

        # Find the course.
        for c in self.courses:
            if c.id == course_id:
                course = c
                break

        if student is None or course is None:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False

        if course_id not in student.enrolled_course_ids:
            print("Error: Check-in failed. Student is not enrolled in this course.")
            return False

        timestamp = datetime.datetime.now().isoformat()

        check_in_record = {
            "student_id": student_id,
            "course_id": course_id,
            "timestamp": timestamp
        }

        self.attendance_log.append(check_in_record)
        self._save_data()

        print(
            f"Success: Student {student.name} "
            f"checked into {course.name}."
        )

        return True


    

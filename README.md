# Music School Management System (MSMS)

## Overview
This project is a Music School Management System (MSMS) developed in Python. It allows reception staff to manage student and teacher, courses, enrolments, attendance, and lesson schedules. It also provides features for switching a student's course, viewing the daily lesson roster, and printing student ID cards. The system uses a JSON file (`msms.json`) to permanently store data. PST3 builds on the previous PST2 implementation by refactoring the application into an object-oriented design. The system uses a `ScheduleManager` to coordinate the main application data and business logic, while the user interface remains in `main.py`.

## What Each Part Does?
## (MSMS.py)
### -Data Models 
This part defines the Student and Teacher classes. Each object stores basic information such as ID, names and, for students, the instruments they are enrolled in and for teacher, the speciality of them.

### -In-Memory Databases
This part stores all the global lists (student_db, teacher_db) and ID counters that will store all our data.

### -Core Helper Functions 
Provides the basic functions for adding, listing and searching students and teachers.

### -Front Desk Functions 
Simulates the receptionist's tasks such as registering students, enrolling them in instruments and searching the system.

### -Main Application 
Displays the menu, accepts user input and calls the correct functions based on the selected option

## (pst2_main.py)
### -Core Persistence Engine
Implements load_data() and save_data() to store all data in a JSON file (msms.json).

### -Full CRUD for Core Data 
Implements adding, updating and removing teacher and student records using dictionaries stored in app_data.

### -New Receptionist Features 
Checking a student in by recording attendance and printing student ID cards as text files.

## (main.py)
### - Main Application
Displays the main menu, accepts user input and calls the appropriate functions for the selected option.

### - Front Desk Functions
Provides receptionist features such as checking in students, viewing the daily lesson roster and switching students between courses.

## (app/student.py)
### - Student Class
Defines the `StudentUser` class. Each student object stores information such as ID, name and enrolled course IDs.

## (app/teacher.py)
### - Teacher and Course Classes
Defines the `TeacherUser` and `Course` classes. Teacher objects store teacher information, while course objects store course details, enrolled students and lesson information.

## (app/schedule.py)
### - Schedule Manager
This part contains the `ScheduleManager` class. It loads and saves data from `msms.json`, finds students and courses, records attendance, retrieves lessons by day, and handles course switching.

## (gui/main_dashboard.py)
### - Main Dashboard
Provides the main Streamlit dashboard and navigation between different parts of the system. It also maintains the `ScheduleManager` using Streamlit session state.

## (gui/student_pages.py)
### - Student Management Page
Provides a Streamlit interface for searching students and registering new students. The registration form collects the student's name and first instrument and calls the `ScheduleManager` to create the student.

## (gui/roster_pages.py)
### - Daily Roster Page
Provides a Streamlit interface for viewing the daily lesson roster and checking students into their courses. The page displays success or error messages based on the check-in result.


## How to Run and Test
### msms.py
Run python file. The program will display a menu where users can register students, enrol students in instruments, search for students or teachers, and list all students and teachers. The program was tested by registering new students, enrolling students into different and same instruments, searching using different keywords, listing all students and teachers, and checking how the program handles invalid menu options.

### pst2_main.py
Run python file. The program will display a menu where users can check in a student, updating teacher information, removing a student, and printing a student card. The program was tested by making sure that changes were saved to `msms.json` and correctly loaded again when the program was restarted. 

### main.py
Run python file. The program will display a menu where users can check in students, view daily lessons and switch students between courses. The program was tested by checking in students, viewing lessons on different days, switching students between courses, using invalid student and course IDs, and checking that changes were saved and loaded correctly from `data/msms.json`.

### PST4 Streamlit Interface
Run the Streamlit application using: python -m streamlit run main.py. The program will display the Streamlit dashboard with navigation for Student Management, Daily Roster and other available sections. The student management page was tested by registering a new student, submitting blank fields, and trying to register a student for an instrument without a suitable teacher. The daily roster page was tested by selecting different days and checking that the correct lessons, courses, teachers and rooms were displayed. The student check-in function was tested using both an enrolled student and a student who was not enrolled in the selected course. The enrolled student was successfully checked in, while the non-enrolled student was rejected.

## Extensions made
### msms.py
As a small improvement, I modified the `front_desk_enrol()` function so that a student cannot be enrolled in the same instrument more than once. If the instrument already exists in the student's enrolment list, the program displays a message instead of creating a duplicate entry. 

### pst2_main.py
In PST2, I added a validation step in the `check_in()` function to ensure that attendance is only recorded for existing students. This helps prevent invalid attendance records from being saved.

### schedule.py
As a small improvement, I added sorting to the daily roster so that lessons are displayed in chronological order based on their start time. This makes the schedule easier to read.

### PST4
As an additional improvement, I added a validation check when registering a new student. The system checks whether a teacher specialises in the requested instrument before allowing the student to be registered. If no suitable teacher is available, the registration is rejected.



## Github Link
https://github.com/LOWJOEYAN/msms-project.git

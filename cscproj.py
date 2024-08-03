import tkinter as tk
from tkinter import messagebox

def get_grade_points(grade):
    grade_points_mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    return grade_points_mapping.get(grade.upper(), 0.0)

def submit_data():
    school_name = 'Hagerstown Community College'
    school_address = '11400 Robinwood Dr, Hagerstown, MD 21742'
    school_phone = '(240) 500-2000'

    student_name = name_entry.get()
    student_id = id_entry.get()
    student_address = address_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    courses = []
    grades = []
    for i in range(len(course_entries)):
        courses.append(course_entries[i].get())
        grades.append(grade_entries[i].get())

    with open('School&StudentData.txt', 'a') as file:
        file.write(f"School Details:\n")
        file.write(f"Name: {school_name}\n")
        file.write(f"Address: {school_address}\n")
        file.write(f"Phone: {school_phone}\n\n")

        file.write(f"\nStudent Details:\n")
        file.write(f"Name: {student_name}\n")
        file.write(f"ID: {student_id}\n")
        file.write(f"Address: {student_address}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")

        total_grade_points = 0
        for course, grade in zip(courses, grades):
            file.write(f"Course: {course}, Grade: {grade}\n")
            if grade.upper() in ['A', 'B', 'C', 'D', 'F']:
                total_grade_points += get_grade_points(grade)

        num_courses_with_grades = max(len(courses), 1)
        gpa = total_grade_points / num_courses_with_grades

        file.write(f"\nTranscript:\n")
        file.write(f"GPA: {gpa:.2f}\n")

    messagebox.showinfo("Success", "Data has been saved to School&StudentData.txt")

# Create the main window
root = tk.Tk()
root.title("Student Data Entry")


# Create and place widgets
tk.Label(root, text="Student Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Student ID:").grid(row=1, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

tk.Label(root, text="Student Address:").grid(row=2, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1)

tk.Label(root, text="Email:").grid(row=3, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

tk.Label(root, text="Phone:").grid(row=4, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1)

# Course and grade entries
course_entries = []
grade_entries = []
for i in range(5):  # Assuming a maximum of 5 courses
    tk.Label(root, text=f"Course {i+1}:").grid(row=5+i, column=0)
    course_entry = tk.Entry(root)
    course_entry.grid(row=5+i, column=1)
    course_entries.append(course_entry)

    tk.Label(root, text=f"Grade {i+1}:").grid(row=5+i, column=2)
    grade_entry = tk.Entry(root)
    grade_entry.grid(row=5+i, column=3)
    grade_entries.append(grade_entry)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=10, column=1, columnspan=2)

root.mainloop()
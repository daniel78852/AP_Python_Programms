import sys

# Initialize variables
totalPoints = 0
totalCourses = 0  # Initialize totalCourses

# Input and calculate GPA

num_courses = int(input("Enter the number of courses: "))




for _ in range(num_courses):
	grade = input("Enter the grade (A/B/C/D/F/Q to quit): ").upper()


	# Calculate grade points
	if grade == "A":
		courseGradePoints = 4.0

	elif grade == "B":
		courseGradePoints = 3.0

	elif grade == "C":
		courseGradePoints = 2.0

	elif grade == "D":
		courseGradePoints = 1.0

	elif grade == "Q":
		exit(0)

	else:
		courseGradePoints = 0.0




		# Update totalPoints with courseGradePoints

	totalPoints += courseGradePoints  # Error 1 corrected
	totalCourses += 1  # Error 2

gpa = totalPoints/totalCourses

print(f'Your current Grade Point Average is: {gpa}'.format(gpa))

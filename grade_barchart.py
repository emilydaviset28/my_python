import matplotlib.pyplot as plt

# Prompt the user for a list of grades
grades = input("Enter a list of grades separated by commas: ")

# Split the input string into a list of grades
grades_list = [int(grade) for grade in grades.split(',')]

# Calculate the number of students who received each grade
grade_counts = {}
for grade in grades_list:
    if grade in grade_counts:
        grade_counts[grade] += 1
    else:
        grade_counts[grade] = 1

# Sort the grades and counts in ascending order
sorted_grades = sorted(grade_counts.keys())
sorted_counts = [grade_counts[grade] for grade in sorted_grades]

# Generate the bar chart
plt.bar(sorted_grades, sorted_counts)

# Add labels and title to the chart
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Student Grades Bar Chart')

# Show the chart
plt.show()

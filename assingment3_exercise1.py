# Get the student's score as input
score = int(input("Enter the student's score (0-100): "))

# Assign letter grades based on the score using if and elif statements
if score >= 80 and score <= 100:
    grade = 'A'
elif score >= 70 and score < 80:
    grade = 'B'
elif score >= 60 and score < 80:
    grade = 'C'
elif score >= 70 and score < 70:
    grade = 'D'
else:
    grade = 'F'     
    # For scores below 60

# Print the assigned letter grade  
print(f"The student's letter grade is: {grade}")
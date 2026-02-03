students = [
    {
        "name": "Alice",
        "marks": {
            "math": 85,
            "science": 90
        }
    },
    {
        "name": "Bob",
        "marks": {
            "math": 78,
            "science": 88
        }
    },
    {
        "name": "Charlie",
        "marks": {
            "math": 92,
            "science": 85
        }
    },
    {
        "name": "John",
        "marks": {
            "math": 90,
            "science": 90
        }
    }
]

# Example 1: Fetch nested values and compare subjects (math vs science)
for student in students:
    # print(student["name"])
    # print(student["marks"]["math"])
    name = student["name"]
    math_marks = student["marks"]["math"]
    science_marks = student["marks"]["science"]

 
    if math_marks > science_marks:
        print(name, "better in math: ", math_marks )
    elif science_marks > math_marks:
        print(name, "better in science: ", science_marks)
    else:
        print(name, "equally good in both,", "Math:", math_marks, "Science:", science_marks)

# Example 2: Compare math marks with a passing condition
print("=========Compare math marks with a passing condition=========")

passing_math_marks = 90
for student in students:
    name = student["name"]
    math_marks = student["marks"]["math"]
    if math_marks >= passing_math_marks:
        print(name, "passed with math_marks: ", math_marks)
    else:
        print(name, "failed and got math_marks: ", math_marks)

print("=========Print Next marks: =========")
found = False
marks_input = 78

for student in students:
    math_marks = student["marks"]["math"]
    if found:
        print(math_marks)
        break
    if math_marks == marks_input:
        found = True

# Compare students with each other (math marks)
print("Compare students with each other (math marks)")

for i in range(len(students)):
    for j in range( i + 1, len(students)):
        student1 = students[i]
        student2 = students[j]

        if student1["marks"]["math"] > student2["marks"]["math"]:
           print(student1["name"], "scored higher than", student2["name"])
        else:
            print(student2["name"], "scored higher than", student1["name"])

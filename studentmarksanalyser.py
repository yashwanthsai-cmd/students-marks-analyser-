import csv

# Load CSV into a list

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # skip empty/invalid rows
        if row["Name"].strip() == "" or row["Marks"].strip() == "":
            continue
        
        try:
            marks = float(row["Marks"])
        except:
            continue

        students.append({
            "Name": row["Name"],
            "Marks": marks
        })

# Calculate basic statistics

marks_list = [s["Marks"] for s in students]

average_marks = sum(marks_list) / len(marks_list)
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

# Assign Grades

def get_grade(m):
    if m >= 90:
        return 'A'
    elif m >= 75:
        return 'B'
    elif m >= 60:
        return 'C'
    elif m >= 40:
        return 'D'
    else:
        return 'F'

for s in students:
    s["Grade"] = get_grade(s["Marks"])

# Count grades
grade_counts = {}
for s in students:
    g = s["Grade"]
    grade_counts[g] = grade_counts.get(g, 0) + 1


# Top 3 scorers

top3 = sorted(students, key=lambda x: x["Marks"], reverse=True)[:3]

# Save cleaned CSV

with open("students_cleaned.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks", "Grade"])
    for s in students:
        writer.writerow([s["Name"], s["Marks"], s["Grade"]])

# Print Results

print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print("\nGrade Counts:")
for g, c in grade_counts.items():
    print(g, ":", c)

print("\nTop 3 Scorers:")
for s in top3:
    print(s["Name"], "-", s["Marks"])

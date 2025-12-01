import csv

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def is_valid_number(value):
    """Checks if value is a valid integer."""
    try:
        int(value)
        return True
    except:
        return False


def run_analysis(filename="students.csv"):
    # Read CSV file
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:

            # Skip rows with missing name or subject
            if row["Name"] == "" or row["Subject"] == "":
                continue

            # Skip rows with invalid or empty marks
            if not is_valid_number(row["Marks"]):
                continue

            # Convert marks to integer
            row["Marks"] = int(row["Marks"])
            data.append(row)

    if len(data) == 0:
        raise ValueError("CSV contains no valid rows.")

    # Dictionary to store marks per student
    student_marks = {}

    for row in data:
        name = row["Name"]
        marks = row["Marks"]

        if name not in student_marks:
            student_marks[name] = []
        student_marks[name].append(marks)

    # Calculate average and grade per student
    student_avg = {}

    for name, marks_list in student_marks.items():
        avg = sum(marks_list) / len(marks_list)
        grade = get_grade(avg)
        student_avg[name] = [avg, grade]

    # Sort by highest average
    sorted_students = sorted(student_avg.items(), key=lambda x: x[1][0], reverse=True)

    # Top 3
    top3 = sorted_students[:3]

    # Highest & lowest marks overall
    all_marks = [row["Marks"] for row in data]
    highest = max(all_marks)
    lowest = min(all_marks)
    overall_avg = sum(all_marks) / len(all_marks)

    # Save cleaned data
    with open("students_cleaned.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Avg Marks", "Grade"])
        for name, details in sorted_students:
            writer.writerow([name, round(details[0], 2), details[1]])

    # Build return message (for GUI)
    result = "=== Student Marks Analyzer ===\n\n"
    result += "Average Marks of Each Student:\n"
    for name, details in student_avg.items():
        result += f"{name}: {details[0]:.2f}  Grade: {details[1]}\n"

    result += "\nTop 3 Performers:\n"
    rank = 1
    for name, details in top3:
        result += f"{rank}. {name}: {details[0]:.2f} (Grade {details[1]})\n"
        rank += 1

    result += f"\nOverall Class Average: {round(overall_avg, 2)}"
    result += f"\nHighest Marks in CSV: {highest}"
    result += f"\nLowest Marks in CSV: {lowest}"
    result += "\n\nCleaned data saved to students_cleaned.csv"

    return result


# Allow standalone running (no GUI)
if __name__ == "__main__":
    print(run_analysis())

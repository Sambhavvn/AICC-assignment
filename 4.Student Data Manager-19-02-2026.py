def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

students = {
    "Aman": {"marks": [85, 90, 88]},
    "Riya": {"marks": [92, 95, 94]},
    "Karan": {"marks": [70, 75, 72]},
    "Sneha": {"marks": [60, 65, 63]},
    "Arjun": {"marks": [78, 82, 80]}
}

topper = ""
top_avg = 0
total_avg = 0

for name, data in students.items():
    avg = sum(data["marks"]) / len(data["marks"])
    students[name]["average"] = avg
    students[name]["grade"] = get_grade(avg)

    total_avg += avg

    if avg > top_avg:
        top_avg = avg
        topper = name

class_avg = total_avg / len(students)

print("Topper:", topper, "-", round(top_avg, 2))
print("Class Average:", round(class_avg, 2))

print("\nStudent Results:")
for name, data in students.items():
    print(name, "-> Avg:", round(data["average"], 2), ", Grade:", data["grade"])
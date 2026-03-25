def categorize_age(age):
    if age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    elif age < 60:
        return "adult"
    else:
        return "senior"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

category = categorize_age(age)

print("\nHello", name + "!")
print("At", age, "years old, you are a", category + ".")
print("It's great that you enjoy", hobby + "!")
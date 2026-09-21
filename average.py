def main():
    marks = {}

    # Ask for subjects until the user types "done"
    while True:
        subject = input("Subject (or done): ").strip().lower()
        if subject == "done":
            break
        marks[subject] = get_mark()

    # Nothing entered, nothing to calculate
    if len(marks) == 0:
        print("No marks entered")
        return

    print()
    for subject in marks:
        print(f"{subject}: {marks[subject]}")

    average = sum(marks.values()) / len(marks)

    # Find the best and the worst subject
    best = None
    worst = None
    for subject in marks:
        if best is None or marks[subject] > marks[best]:
            best = subject
        if worst is None or marks[subject] < marks[worst]:
            worst = subject

    print()
    print(f"Average: {round(average, 2)}")
    print(f"Highest mark: {best} ({marks[best]})")
    print(f"Lowest mark: {worst} ({marks[worst]})")
    print(f"Grade: {get_grade(average)}")


def get_mark():
    mark = float(input("Enter your mark (0-20): "))
    while mark < 0 or mark > 20:
        print("Invalid mark. Please enter a mark between 0 and 20.")
        mark = float(input("Enter your mark (0-20): "))
    return mark


def get_grade(average):
    if average < 10:
        return "Fail"
    elif average < 12:
        return "Pass"
    elif average < 14:
        return "Fairly Good"
    elif average < 16:
        return "Good"
    else:
        return "Very Good"


main()

try:
    score = float(input("Enter the score: "))

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade is: {grade}")

except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")
except Exception as e:
    print(f"An error occurred: {e}")

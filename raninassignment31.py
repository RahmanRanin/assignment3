try:
    hours = float(input("Enter the hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    if hours < 0 or not hours.is_integer():
        raise ValueError("Please enter an integer value.")

    if hours <= 40:
        salary = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (1.5 * rate)
        salary = regular_pay + overtime_pay

    print(f"Salary: ${salary:.2f}")

except ValueError as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by the user.")
except Exception as e:
    print(f"An error occurred: {e}")


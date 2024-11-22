import calendar

# Example caregivers with availability
caregivers = {
    "Alice": {"preferred": ["Monday AM", "Tuesday PM"], "available": ["Wednesday AM", "Friday PM"]},
    "Bob": {"preferred": ["Tuesday AM", "Friday AM"], "available": ["Monday PM", "Saturday AM"]},
    "Charlie": {"preferred": ["Wednesday PM"], "available": ["Thursday AM", "Sunday PM"]},
}

# Example function to generate a schedule
def create_schedule(month, year):
    # Create a simple HTML calendar
    cal = calendar.HTMLCalendar()
    schedule = cal.formatmonth(year, month)

    # Example: Assign caregivers to shifts (simple round-robin)
    shifts = ["AM", "PM"]
    caregivers_list = list(caregivers.keys())
    schedule_assignments = {}

    for day in range(1, calendar.monthrange(year, month)[1] + 1):  # Days in the month
        for shift in shifts:
            caregiver = caregivers_list[(day - 1) % len(caregivers_list)]
            schedule_assignments[(day, shift)] = caregiver

    # Display assignments
    print("Care Schedule:")
    for (day, shift), caregiver in schedule_assignments.items():
        print(f"Day {day}, {shift}: {caregiver}")

    return schedule


# Generate a schedule for December 2024
html_calendar = create_schedule(12, 2024)

# Pay rate
PAY_RATE = 20  # $20/hour

# Weekly hours for each caregiver (Example Data)
caregiver_hours = {
    "Alice": 20,  # 20 hours per week
    "Bob": 15,    # 15 hours per week
    "Charlie": 25,  # 25 hours per week
}

# Function to calculate weekly pay
def calculate_weekly_pay(hours, rate):
    return hours * rate

# Generate pay report
def generate_pay_report():
    print("Weekly Pay Report")
    total_weekly_pay = 0
    for caregiver, hours in caregiver_hours.items():
        weekly_pay = calculate_weekly_pay(hours, PAY_RATE)
        print(f"{caregiver}: ${weekly_pay:.2f}")
        total_weekly_pay += weekly_pay

    total_monthly_pay = total_weekly_pay * 4  # Assuming 4 weeks per month
    print(f"Total Weekly Pay: ${total_weekly_pay:.2f}")
    print(f"Total Monthly Pay: ${total_monthly_pay:.2f}")

# Generate the report
generate_pay_report()
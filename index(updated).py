import calendar


# Caregiver Class
class Caregiver:
    # Holds info about caregivers and their availability
    def __init__(self, name, phone, email, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours = 0  # Hours worked
        self.availability = {}  # Availability for shifts

    def set_availability(self, date, shift, status="available"):
        # Update the caregiver's availability for a shift
        if date not in self.availability:
            self.availability[date] = {}
        self.availability[date][shift] = status

    def get_weekly_hours(self):
        # Calculate how many hours they worked in a week
        return self.hours


# Scheduler Class
class Scheduler:
    # Manages the caregivers and schedules
    def __init__(self):
        self.caregivers = []  # List of caregivers
        self.schedule = {}  # Schedule for all days

    def add_caregiver(self, caregiver):
        # Add a caregiver to the system
        self.caregivers.append(caregiver)

    def create_schedule(self, month, year):
        # Create a schedule for a whole month using a simple round-robin method
        cal = calendar.Calendar()
        days_in_month = calendar.monthrange(year, month)[1]
        shifts = ["AM", "PM"]
        caregivers_list = self.caregivers
        schedule_assignments = {}

        for day in range(1, days_in_month + 1):  # Days in the month
            for shift in shifts:
                # Assign a caregiver based on availability and preference
                for caregiver in caregivers_list:
                    date_str = f"{year}-{month:02d}-{day:02d}"
                    if date_str in caregiver.availability and caregiver.availability[date_str].get(
                            shift) == "preferred":
                        schedule_assignments[(day, shift)] = caregiver.name
                        caregiver.hours += 4  # Add 4 hours per shift
                        break

        self.schedule = schedule_assignments  # Update the schedule
        return schedule_assignments

    def display_schedule(self):
        print("Schedule:")
        for (day, shift), caregiver in self.schedule.items():
            print(f"Day {day}, {shift}: {caregiver}")

    def generate_pay_report(self):
        # Generate pay report based on hours worked
        pay_report = {}
        for caregiver in self.caregivers:
            pay_report[caregiver.name] = caregiver.hours * caregiver.pay_rate
        return pay_report

    def display_pay_report(self):
        pay_report = self.generate_pay_report()
        print("Pay Report:")
        for caregiver, pay in pay_report.items():
            print(f"{caregiver} earned ${pay:.2f}")


# Function to create and display work schedule as HTML
def display_schedule_as_html(schedule, year, month):
    # Create the HTML structure for work schedule
    html_schedule_day = f"""
    <html>
    <head>
        <title>Work Schedule for {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            td {{
                height: 100px;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        <h1>Work Schedule for {calendar.month_name[month]} {year}</h1>
        <table>
            <tr>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
    """

    # Get the first weekday of the month and the total days
    first_weekday, num_days = calendar.monthrange(year, month)

    # Fill in the days of the month
    current_day = 1
    for week in range((num_days + first_weekday) // 7 + 1):
        html_schedule_day += "<tr>"
        for day in range(7):
            if (week == 0 and day < first_weekday) or current_day > num_days:
                html_schedule_day += "<td></td>"  # Empty cell for days outside the month
            else:
                # Add the day and the assigned shifts
                shifts_for_day = {shift: schedule.get((current_day, shift), "N/A") for shift in ["AM", "PM"]}
                morning_shift_day = shifts_for_day["AM"]
                afternoon_shift_day = shifts_for_day["PM"]

                html_schedule_day += f"<td>{current_day}<br><b>AM:</b> {morning_shift_day}<br><b>PM:</b> {afternoon_shift_day}</td>"
                current_day += 1
        html_schedule_day += "</tr>"

    # Close the table and HTML
    html_schedule_day += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(f"work_schedule_{year}_{month}.html", "w") as file:
        file.write(html_schedule_day)

    print(f"HTML work schedule for {calendar.month_name[month]} {year} generated successfully!")


# Function to display caregiver's availability as HTML
def display_availability_as_html(caregiver_availability):
    # Create the HTML structure for availability schedule
    html_schedule = """
    <html>
    <head>
        <title>User Availability Schedule</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }
            th, td {
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
            td {
                height: 100px;
                vertical-align: top;
            }
        </style>
    </head>
    <body>
        <h1>User Availability Schedule</h1>
        <table>
            <tr>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
            <tr>
    """

    # Loop over the days and availability
    for day in range(1, 8):
        # Retrieve availability for the morning and afternoon shifts
        if day in caregiver_availability:
            morning_shift = caregiver_availability[day].get("AM", "NA")
            afternoon_shift = caregiver_availability[day].get("PM", "NA")
        else:
            morning_shift = "NA"
            afternoon_shift = "NA"

        html_schedule += f"<td><b>Morning:</b> {morning_shift}<br><b>Afternoon:</b> {afternoon_shift}</td>"

    # Close the table and HTML
    html_schedule += """
        </tr>
        </table>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open("availability_schedule.html", "w") as file:
        file.write(html_schedule)

    print("HTML availability schedule generated successfully!")


# Main program
if __name__ == "__main__":
    # Start the scheduling program
    scheduler = Scheduler()

    # Add caregivers
    caregiver1 = Caregiver("John Doe", "555-1234", "john@example.com")
    caregiver2 = Caregiver("Alice Smith", "555-5678", "alice@example.com")
    caregiver3 = Caregiver("Bob Brown", "555-9876", "bob@example.com")

    scheduler.add_caregiver(caregiver1)
    scheduler.add_caregiver(caregiver2)
    scheduler.add_caregiver(caregiver3)

    # Set up availability for caregivers
    caregiver1.set_availability("2024-11-01", "AM", "preferred")
    caregiver2.set_availability("2024-11-01", "PM", "preferred")
    caregiver3.set_availability("2024-11-02", "AM", "preferred")

    # Get user input for the year and month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Generate work schedule for the specified month and year
    scheduler.create_schedule(month, year)

    # Show the schedule
    scheduler.display_schedule()

    # Show the pay report
    scheduler.display_pay_report()

    # Generate the HTML work schedule
    display_schedule_as_html(scheduler.schedule, year, month)

    # Generate the HTML availability schedule for caregivers
    caregiver_availability = {
        1: {"AM": "preferred", "PM": "NA"},
        2: {"AM": "NA", "PM": "available"},
        3: {"AM": "available", "PM": "unavailable"},
        # Add more days as needed
    }
    display_availability_as_html(caregiver_availability)



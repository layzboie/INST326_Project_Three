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

    def calculate_weekly_pay(self):
        # Calculate weekly pay based on hours worked
        return self.hours * self.pay_rate

# Scheduler Class
class Scheduler:
    # Manages the caregivers and schedules
    def __init__(self):
        self.caregivers = []  # List of caregivers
        self.schedule = {}  # Schedule for all days

    def add_caregiver(self, caregiver):
        # Add a caregiver to the system
        self.caregivers.append(caregiver)

    def create_schedule(self, year, month):
        # Create a schedule for a whole month
        cal = calendar.Calendar()
        days_in_month = calendar.monthrange(year, month)[1]
        shifts = ["AM", "PM"]

        # Go through each day and assign caregivers
        for day in range(1, days_in_month + 1):
            for shift in shifts:
                assigned = False
                for caregiver in self.caregivers:
                    date_str = f"{year}-{month:02d}-{day:02d}"
                    if date_str in caregiver.availability:
                        if caregiver.availability[date_str].get(shift) == "preferred":
                            self.schedule[(day, shift)] = caregiver.name
                            caregiver.hours += 6  # Each shift is 6 hours
                            assigned = True
                            break
                        elif caregiver.availability[date_str].get(shift) == "available" and not assigned:
                            self.schedule[(day, shift)] = caregiver.name
                            caregiver.hours += 6
                            assigned = True

    def show_schedule(self):
        # Print the schedule
        for (day, shift), caregiver in self.schedule.items():
            print("Day " + str(day) + ", " + shift + " shift: " + caregiver)

    def calculate_pay_report(self):
        # Generate and display pay report
        total_weekly_pay = 0
        for caregiver in self.caregivers:
            weekly_pay = caregiver.calculate_weekly_pay()
            total_weekly_pay += weekly_pay
            print(caregiver.name + ": $" + str(weekly_pay))
        print("Total Weekly Pay: $" + str(total_weekly_pay))

# Function to create an HTML work schedule
def create_html_schedule(schedule, year, month):
    html = """
    <html>
    <head>
        <title>Work Schedule</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Work Schedule for """ + calendar.month_name[month] + " " + str(year) + """</h1>
        <table>
            <tr>
                <th>Day</th>
                <th>AM Shift</th>
                <th>PM Shift</th>
            </tr>
    """

    # Add each day's schedule to the HTML
    days_in_month = calendar.monthrange(year, month)[1]
    for day in range(1, days_in_month + 1):
        am_shift = schedule.get((day, "AM"), "Unassigned")
        pm_shift = schedule.get((day, "PM"), "Unassigned")
        html += "<tr><td>" + str(day) + "</td><td>" + am_shift + "</td><td>" + pm_shift + "</td></tr>"

    html += """
        </table>
    </body>
    </html>
    """

    # Save the HTML to a file
    with open("schedule.html", "w") as file:
        file.write(html)
    print("HTML schedule created and saved as 'schedule.html'.")

# Main program
if __name__ == "__main__":
    # Create the scheduler
    scheduler = Scheduler()

    # Add caregivers with different attributes
    caregiver1 = Caregiver("John Doe", "555-1234", "john@example.com", pay_rate=20)
    caregiver2 = Caregiver("Alice Smith", "555-5678", "alice@example.com", pay_rate=20)
    caregiver3 = Caregiver("Bob Brown", "555-9876", "bob@example.com", pay_rate=25)
    caregiver4 = Caregiver("Sara Jones", "555-4321", "sara@example.com", pay_rate=20)

    # Add caregivers to the scheduler
    scheduler.add_caregiver(caregiver1)
    scheduler.add_caregiver(caregiver2)
    scheduler.add_caregiver(caregiver3)
    scheduler.add_caregiver(caregiver4)

    # Set availability for caregivers
    for i in range(1, 8):
        date = f"2024-11-{i:02d}"
        caregiver1.set_availability(date, "AM", "preferred" if i % 2 == 0 else "available")
        caregiver1.set_availability(date, "PM", "available")
        caregiver2.set_availability(date, "AM", "available")
        caregiver2.set_availability(date, "PM", "preferred" if i % 3 == 0 else "available")
        caregiver3.set_availability(date, "AM", "available")
        caregiver3.set_availability(date, "PM", "preferred" if i % 2 != 0 else "available")
        caregiver4.set_availability(date, "AM", "available")
        caregiver4.set_availability(date, "PM", "preferred" if i % 4 == 0 else "available")

    # Generate the schedule
    print("\nGenerating schedule for November 2024...")
    scheduler.create_schedule(2024, 11)

    # Display the schedule
    print("\nSchedule:")
    scheduler.show_schedule()

    # Display the pay report
    print("\nPay Report:")
    scheduler.calculate_pay_report()

    # Generate HTML schedule
    print("\nCreating HTML schedule...")
    create_html_schedule(scheduler.schedule, 2024, 11)

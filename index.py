import calendar

# Caregiver Class
class Caregiver:
    # Holds info about caregivers and their availability
    def __init__(self, name, phone, email, pay_rate=20):
        # Set up the caregiver's details
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
        # Figure out how many hours they worked in a week
        return self.hours

# Scheduler Class
class Scheduler:
    # Manages the caregivers and schedules
    def __init__(self):
        # Set up the scheduler
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
                    if (f"{year}-{month:02d}-{day:02d}") in caregiver.availability and caregiver.availability[f"{year}-{month:02d}-{day:02d}"].get(shift) == "preferred":
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

    # Set up availability
    caregiver1.set_availability("2024-11-01", "AM", "preferred")
    caregiver2.set_availability("2024-11-01", "PM", "preferred")
    caregiver3.set_availability("2024-11-02", "AM", "preferred")

    # Make a schedule for November 2024
    scheduler.create_schedule(11, 2024)

    # Show the schedule
    scheduler.display_schedule()

    # Show the pay report
    scheduler.display_pay_report()
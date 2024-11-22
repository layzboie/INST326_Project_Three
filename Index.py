
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
        pass

    def get_weekly_hours(self):
        # Figure out how many hours they worked in a week
        pass


class Scheduler:
    # Manages the caregivers and schedules
    def __init__(self):
        # Set up the scheduler
        self.caregivers = []  # List of caregivers
        self.schedule = {}  # Schedule for all days

    def add_caregiver(self, caregiver):
        # Add a caregiver to the system
        pass

    def create_schedule(self, month, year):
        # Make a schedule for a whole month
        pass

    def assign_shift(self, date, shift):
        for c in self.caregivers:
            if date in c.availability and shift in c.availability[date] and c.availability[date][shift] == "preferred":
                if date not in self.schedule:
                    self.schedule[date] = {"AM": [], "PM": []}
                self.schedule[date][shift] = [c.name]  # assign caregiver
                c.hours = c.hours + 4  # add hours
                print("Assigned " + c.name + " to " + shift + " on " + date)
                return
        print("No one for " + shift + " on " + date)  


    def generate_pay_report(self):
        pay = {}  
        for c in self.caregivers:
            pay[c.name] = c.hours * c.pay_rate 
        return pay  

    def display_schedule(self):
        print("Schedule")
        for d in self.schedule:  
            am = "No one"
            pm = "No one"
            if "AM" in self.schedule[d]:
                am = ", ".join(self.schedule[d]["AM"])
            if "PM" in self.schedule[d]:
                pm = ", ".join(self.schedule[d]["PM"])
            print(d + ": AM: " + am + ", PM: " + pm)

    def display_pay_report(self):
        pay = self.generate_pay_report()  
        print("Pay Report")
        for n in pay:  
            print(n + " earned " + str(pay[n]) + " dollars")


# main program
if __name__ == "__main__":
    # Start the scheduling program
    scheduler = Scheduler()

    # Add some example caregivers
    caregiver1 = Caregiver("John Doe", "555-1234", "john@example.com")
    caregiver2 = Caregiver("Alice Smith", "555-5678", "alice@example.com")

    scheduler.add_caregiver(caregiver1)
    scheduler.add_caregiver(caregiver2)

    # Set up availability 
    caregiver1.set_availability("2024-11-01", "AM", "preferred")
    caregiver2.set_availability("2024-11-01", "PM", "preferred")

    # Make a schedule for November
    scheduler.create_schedule(11, 2024)

    # Show the schedule
    scheduler.display_schedule()

    # Show the pay report
    scheduler.display_pay_report()

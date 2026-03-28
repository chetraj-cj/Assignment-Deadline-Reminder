# Assignment Deadline Reminder System with Date + Time + Popup

from datetime import datetime
from plyer import notification
import time
import threading

assignments = []

# -------------------------------
# Function: Check Deadlines & Notify
# -------------------------------
def check_deadlines():
    while True:
        now = datetime.now()

        for name, deadline_str in assignments:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            time_left = deadline - now
            minutes_left = int(time_left.total_seconds() / 60)

            # Notification conditions
            if minutes_left < 0:
                message = f"{name} deadline missed!"
            elif minutes_left == 0:
                message = f"{name} is due NOW!"
            elif minutes_left <= 120:
                message = f"{name} urgent! {minutes_left} minutes left"
            elif minutes_left <= 1440:
                hours = minutes_left // 60
                message = f"{name} due in {hours} hours"
            else:
                continue  # Skip non-urgent

            # Popup Notification
            notification.notify(
                title="Assignment Reminder",
                message=message,
                timeout=5
            )

        time.sleep(60)  # Check every 1 minute

# -------------------------------
# Start Background Thread
# -------------------------------
thread = threading.Thread(target=check_deadlines, daemon=True)
thread.start()

# -------------------------------
# Main Menu
# -------------------------------
while True:
    print("\n1. Add Assignment")
    print("2. Check Deadlines")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter assignment name: ")
        deadline = input("Enter deadline (YYYY-MM-DD HH:MM): ")

        assignments.append((name, deadline))
        print("✅ Assignment added!")

    elif choice == '2':
        now = datetime.now()

        for name, deadline_str in assignments:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            time_left = deadline - now
            minutes_left = int(time_left.total_seconds() / 60)

            print(f"\n{name}")

            if minutes_left < 0:
                print("❌ Deadline missed!")
            else:
                hours = minutes_left // 60
                minutes = minutes_left % 60
                print(f"⏳ Time left: {hours} hours {minutes} minutes")

                if minutes_left <= 60:
                    print("🚨 Very Urgent!")
                elif minutes_left <= 1440:
                    print("⚠️ Due within a day")
                else:
                    print("✅ You have time")

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

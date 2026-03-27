# LabLog/Labs n' Logs Manager Main Application
# This program allows users to add, view, and store lab entries.
# It uses object-oriented programming (classes), regex validation, and file I/O.
import csv
from lablog.models import ExperimentEntry, FaultEntry
from lablog.validators import is_valid_email

entries = []
# Main menu loop that continuously runs until the user exits
# It allows the user to interact with the system by selecting options
def menu():
    while True:
        print("1. Add Experiment")
        print("2. Add Fault")
        print("3. View Entries")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            add_experiment()
        elif choice == "2":
            add_fault()
        elif choice == "3":
            view_entries()
        elif choice == "4":
            save_csv()
        elif choice == "5":
            break
        else:
            print("Invalid option")
# Function to create a new ExperimentEntry object
# Validates the email using regex before creating the entry
# Email is valid in any xxxx@xxxx.xxx format
def add_experiment():
    email = input("Email: ")

    if not is_valid_email(email):
        print("Invalid email")
        return

    entry = ExperimentEntry(
        input("ID: "),
        input("Date: "),
        email,
        input("Equipment ID: "),
        input("Description: "),
        float(input("Voltage: ")),
        float(input("Current: "))
    )

    entries.append(entry)
    print("Experiment added.")

def add_fault():
    entry = FaultEntry(
        input("ID: "),
        input("Date: "),
        input("Email: "),
        input("Equipment ID: "),
        input("Description: "),
        input("Severity: "),
        False
    )

    entries.append(entry)
    print("Fault added.")

def view_entries():
    if len(entries) == 0:
        print("No entries yet.")
        return

    for e in entries:
        e.display()


def save_csv():
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["ID", "Date", "Email", "Equipment", "Description"])

        for e in entries:
            writer.writerow([
                e.entry_id,
                e.date,
                e.email,
                e.equipment_id,
                e.description
            ])

    print("Data saved to data.csv")

menu()

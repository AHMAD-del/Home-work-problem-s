"""
program for adding or viewing patient data
"""
import csv
from rich.console import Console
from rich.traceback import install
import re
from tabulate import tabulate
console = Console()
install()

def main():
    console.print("Welcome!", style="green")
    while True:
        console.print("\nOptions:", style="cyan")
        console.print("1. Add Patient Data", style="cyan")
        console.print("2. View Patient Data", style="cyan")
        console.print("3. User Guide", style="cyan")
        console.print("4. Exit", style="cyan")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            PatientIntro()
        elif choice == "2":
            viewData()
        elif choice == "3":
            userGuide()
        elif choice == "4":
            console.print("Goodbye!", style="green")
            break
        else:
            console.print("Invalid choice. Try again.", style="red")

def PatientIntro():
    introLst = []
    id = 1
    lst = ["male", "female", "neutral"]

    diseases = [
        "flu", "diabetes", "hypertension", "asthma", "arthritis", "tuberculosis", "heart disease", "pneumonia", "malaria"
    ]

    while True:
        try:
            name = input("Patient name: ").lower().strip()
            # this will allow user to enter name having about two whitspaces in it
                # ^
                # |------------v-------------v
            if re.search(r"^([a-z]{3,15}) ?([a-z]{3,15})*$", name):
                age = input("Patient Age(1 to 100): ").strip()
                # first ensure that input is between 0 to 9 with infinite number of repitation
                if re.search(r"^[0-9]+$", age):
                    # secondly this check if first one is true
                    # now condition will checked between 1 to 100
                    if (int(age) > 0) and (int(age) <= 100):
                        gender = input("Gender(male/female/neutral): ").lower().strip()
                        if gender in lst:
                            disease = input("Patient Disease: ").lower().strip()
                            if disease in diseases:
                                introLst.append(id)
                                id += 1
                                introLst.append(name)
                                introLst.append(age)
                                introLst.append(gender)
                                introLst.append(disease)
                                insertingData(introLst)
                                console.print("Data added successfully!", style="green")
                                break

        except:
            userinput = input("Press 3 for Exit: ").strip()
            if userinput == "3":
                break


def insertingData(introLst):
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(introLst)

def viewData():
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            console.print("\nPatient Records:", style="bold blue")
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        console.print("No data found. Add some patient records first.", style="red")


def userGuide():
    print("<--------------------------------------------------------------------------------------->")
    console.print("User Guide",style="green")
    print("1. Add Data:\n  Add Data option will add data by pressing only 1\n  first it will take 'Name'\n  secondly it will take 'Age'\n  third one will take 'Gender'\n  lastly it will take 'Disease name'")
    print("2. view Data:\n  view Data option will show data(Patient Records) by pressing only 2")
    print("3. Exit:\n  exit option will Exit by pressing only 3")
    print("4. User Guide:\n  User Guide option will guidance to use the program by pressing only 4")
    print("<--------------------------------------------------------------------------------------->")

if __name__ == "__main__":
    main()

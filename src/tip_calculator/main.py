from tip_calculator.calculator import bill_per_person


def main() -> None:
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    final_amount = bill_per_person(bill, tip, people)
    print(f"Each person should pay: ${final_amount:.2f}")


if __name__ == "__main__":
    main()

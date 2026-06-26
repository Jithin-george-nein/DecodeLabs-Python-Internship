def main():
    total_spent = 0.0

    while True:
        user_input = input().strip()

        if user_input.lower() == 'quit':
            break

        try:
            new_expense = float(user_input)
            if new_expense < 0:
                continue

            total_spent += new_expense
            print(total_spent)

        except ValueError:
            print("Invalid Data")

    print(total_spent)

if __name__ == "__main__":
    main()
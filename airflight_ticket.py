seat = [False] * 10  
booked_seat = True

first_class = 0
economy_class = 5

while True:
    try:
        userinput = int(input("Enter 1 for First Class or 2 for Economy Class: "))

        match userinput:
            case 1: 
                if first_class < 5:
                    seat[first_class] = booked_seat
                    first_class += 1
                    print(f"First-class seat booked: {seat}")
                else:
                    print("First-class is full. Consider booking in Economy.")

            case 2:  
                if economy_class < 10:
                    seat[economy_class] = booked_seat
                    economy_class += 1
                    print(f"Economy-class seat booked: {seat}")
                else:
                    print("Economy is full. Would you like a First-class seat? (1 for Yes, 2 for No)")
                    choice = int(input("Enter 1 for Yes or 2 for No: "))

                    if choice == 1 and first_class < 5:
                        seat[first_class] = booked_seat
                        first_class += 1
                        print(f"First-class seat booked: {seat}")
                    else:
                        print("No available seats. The next flight leaves in 3 hours.")
                        break  # Exit loop if no seats are available

            case _:
                print("Invalid selection. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    # Stop booking if all seats are full
    if first_class >= 5 and economy_class >= 10:
        print("All seats are booked. The next flight leaves in 3 hours.")
        break


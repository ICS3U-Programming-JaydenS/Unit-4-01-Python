#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program tells you the sum of the user's number


def main():

    # First I define my variables
    user_num = input("What is the number you want the sum of:")
    counter = 0
    total = 0
    try:

        # Try to convert the user num to int
        user_num_as_int = int(user_num)

        # Checks if it is negative
        if user_num_as_int < 0:
            print((user_num_as_int),"is not a positive integer")
        elif user_num_as_int == 0:

            print(
                (user_num_as_int),
                "is not positive or negative and would just give you 0.",
            )

        # If not code continued as intended
        else:

            # Checks if user_num is greater then counter
            while user_num_as_int > counter:
                counter = counter + 1
                print("Tracking", (counter), "Times through the loop")
                total = counter + total

                # If counter is the same the loop breaks
                if user_num_as_int == counter:
                    break

        # It then prints the sum
            print("The sum is", (total))

    # What happens if you do not put a number
    except:
        print((user_num), "is not a integer!")


if __name__ == "__main__":
    main()

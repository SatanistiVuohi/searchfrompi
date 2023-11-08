#! python 3
# searchforpi.py - 1 000 000 digits of pi and lets search a string of
# numbers out of it
import pidecimal
while True:
    pi = pidecimal.pi

    number = input("Give me a number number: ")

    if number == "no":
        print("Thank you!")
        break
    else:
        print(f"Yay! We found your number first at: {pi.find(number)}")
        print(f"Your number was found {pi.count(number)} times!")
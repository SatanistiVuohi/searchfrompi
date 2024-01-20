#! python 3
# searchforpi.py - 1 000 000 digits of pi and lets search a string of
# numbers out of it
import pidecimal

pi = pidecimal.pi
print("Give me a number or 'no' to quit:")
number = input(str())

if number == "no":
    print("Thank you!")

else:
    print(f"We found your number first at: {pi.find(number)}")
    print(f"We found your number second at: {pi.find(number, pi.find(number) + 1)}")
    print(f"Your number was found {pi.count(number)} times!")


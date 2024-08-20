import time

def animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def happy_birthday(name, age):
    print("Happy Birthday, " + name + "!")
    print("Congratulations on turning " + str(age) + " years old.")
    print("May your day be filled with joy and happiness.")
    print()
    print("    \U0001F382   \U0001F389   \U0001F381")
    print("  \U0001F601       \U0001F389")
    print("    \U0001F4F2  🥳  \U0001F389")
    print("    \U0001F377       \U0001F389")
    print("    \U0001F3C0   \U0001F389")
    print()

name = input("Enter your name: ")
age = int(input("How old are you today? "))

animation("Generating Birthday Message...")
time.sleep(1)
happy_birthday(name, age)

import time

running = True

b = input("\nType q to quit, Enter to continue:\n")
if b == "q":
    running = False

else:
    running = True

while running:
    time.sleep(3)
    print("\nLook away from the screen\n")

    b = input("\nType q to quit, Enter to continue:\n")
    if b == "q":
        running = False

print("Bye!")
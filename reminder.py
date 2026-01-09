import time

a = True
b = input("\nType q to quit, Enter to continue:\n")
while a:
    if b == "q":
        print("Bye!")
        break
    if b == "":
        time.sleep(3600)
        print("Look away from the screen")
    

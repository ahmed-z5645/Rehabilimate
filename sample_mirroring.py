import time

def fake():
    while True:
        print("Welcome to RehabiliMate!!")
        print("Would you like to do Reaction Potential Mirroring (type mirror),",
              "\n", "or the automated routine training (type automate)")
        answer = input()

        if answer == "mirror":
            print("Starting Mirroring")
            print("Training Complete")
        elif answer == "automate":
            print("Starting Routine")
            print("Training Complete")
        else:
            print("Invalid Answer")
        
fake()

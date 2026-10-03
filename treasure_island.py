def start_adventure():
    print("welcome to my island(:")
    print("""
    *   *
   *** ***
  *********
     ||
     ||
~~~~~||~~~~~~
""")
    
    print("there are two doors in front of you.  a red door and  a blue door ")
    open_door = input("which door do you want to open?: ").lower()
    
    if open_door == "red":
        print("great! you entered a room.")
        print("you founded three boxes:  white,  black,  green")
        open_box = input("which box do you open? ").lower()
        
        if open_box == "green":
            print("congratulations!you found the treasure🏆👑")
        elif open_box == "white":
            print("oops you opend a box filled with snakes!🐍🐍🐍")
        elif open_box == "black":
            print("oops you opend a box filled with spiders!🕷️🕷️🕷️")
        else:
            print("invalid choice!🚫🚫🚫")
    elif open_door == "blue":
        print("Oops you opend the crocodile door.\ngame over🐊🐊🐊")
    else:
        print("invalid choice!🚫🚫🚫")

if __name__ == "__main__":
    start_adventure()

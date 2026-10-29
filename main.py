#ruff Rule Break 1: unused import rule
import os

def main():
    print("Hello from dsc-190-assignment-5!")
    
    #ruff Rule Break 2: unused local variable
    unused_variable = 67
    
    #ruff Rule Break 3: using == to compare none
    x= None
    if x == None:
        print("This is improper style")

if __name__ == "__main__":
    main()

#ruff Rule Break 1: unused import rule

def main():
    print("Hello from dsc-190-assignment-5!")
    
    #ruff Rule Break 2: unused local variable
    
    #ruff Rule Break 3: using == to compare none
    x= None
    if x == None:
        print("This is improper style")

if __name__ == "__main__":
    main()

print("Program to check wheather th nth bit is Set or Not")

num = int(input("Enter the number: "))
pos = int(input("Enter the bit position:  "))

def setOrnot(num, pos):
    if(pos & 1) == 1 or (pos&1) == 0:
        if num & (1 <<  (pos- 1)):
            print("SET BIT")
        else:
            print("It's NOT a SET BIT")


setOrnot(num , pos)
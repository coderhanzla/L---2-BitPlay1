
def numberOfBits(number):
    ones = 0
    zeros = 0
    while(number):
        if(number & 1== 1):
            ones = ones+1
        else:
            zeros = zeros+1
        number >>= 1

    print("Number of ones =" , ones , "Number of zeros = " , zeros)   

number = int(input("Enter the number: "))
numberOfBits(number)
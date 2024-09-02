a = int(input("Enter The Number : "))
if a <= 1:
    print("It is not Prime Number")
else:
    for i in range (2,(a*0.5)+1):
        if a % i == 0:
            k = "Not Prime"
            break
        else:
            k = "Prime"
    print("The Entered Number is",k)

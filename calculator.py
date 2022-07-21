from operations import add,sub

opp= input("Enter the operation:\n1.ADD\n2.SUBTRACT")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if opp.lower()=="add":
    result= add(num1,num2)
    print('The sum is ', result)

elif opp.lower()=="sub":
    result= sub(num1,num2)
    print('The difference is ', result)

else:
    print("operation not defined. Please select addition.")
    print('Subtraction work done.')   
   
    



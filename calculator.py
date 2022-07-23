from operations import add,sub

opp= input("Enter the operation:\n1.ADD\n2.SUBTRACT ")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))


if opp.lower()=="1":

    result= add(num1,num2)
    print('The sum is ', result)

else: 
    print("Operation is invalid ")    
    print("Enter the correct opp" )    


   
    

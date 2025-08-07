num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))



print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter your operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(" Result:", result)

elif operation =="-":
  result= num1 - num2
  print(" Result:". result)   

elif operation =="*":
  result= num1 * num2
  print(" Result:". result)   

elif operation =="-":
  result= num1 - num2
  print(" Result:". result)  

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(" Result:", result)
    else:
        print(" Error")
else:
    print(" Invalid operation .") 
def calculator():
    while True:
     print("\n                                          =CALCULATOR=")
     print("                                             ENTER")
     print("                                        1 for Addition(+)")
     print("                                        2 for Subtraction(-)")
     print("                                        3 for Multiplication(*)")
     print("                                        4 for Division(/)")
     print("                                        5 for Ending the program")

     choice = int(input("\n                                       Enter your choice here: "))

     if choice == 5:
        print("Ending the program...")
        break

     if choice in [1,2,3,4]:
        try:
         a = float(input("                                       Enter first number: "))
         b = float(input("                                       Enter second number: "))
        except ValueError:
           print("                                       Invalid input! Enter numeric values only.")
           continue

        if choice == 1:
           r = a + b
           print(f"                                       Result: {a} + {b} = {r}")
        elif choice == 2:
           r = a - b
           print(f"                                       Result: {a} - {b} = {r}")
        elif choice == 3:
           r = a * b
           print(f"                                       Result: {a} * {b} = {r}")
        elif choice == 4:
           if b!=0:
              r = a/b
              print(f"                                       Result: {a} / {b} = {r}")
           else:
              print("                                       Cannot divide by zero!")
     else:
       print("                                       Please choose a number between 1 and 5.")

calculator() 
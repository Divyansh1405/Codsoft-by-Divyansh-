class Calculator:
    def __init__(self):
        self.num1 = ""
        self.num2 = ""
        self.menu()

    def menu(self):
        user_input = input("""
Choose the operation (1-5)
  1. Addition " + "
  2. Subtraction " - "
  3. Multiplication " * "
  4. Division " / "
  5. Exit
                           
Enter your choice:  """)
        
        if user_input == "1":
            self.add()
        elif user_input == "2":
            self.subtract()
        elif user_input == "3":
            self.multiply()
        elif user_input == "4":
            self.divide()
        elif user_input == "5":
            print("Exit")
        else:
            print("Wrong Input")
            self.menu()

    def add(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("The sum of two numbers are: ", x + y)
        self.menu()

    def subtract(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("The difference of two numbers are: ", x - y)
        self.menu()

    def multiply(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("The product of two numbers are: ", x * y)
        self.menu()

    def divide(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print("The division of two numbers are: ", x / y)
        self.menu()

obj = Calculator()

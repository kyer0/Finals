print("="*60)
print("                 WELCOME TO PYTHON TUTORIAL")
print("="*60)
print("\nWelcome, learner!")
print("Below are the available lessons that you can browse\n")

lesson = ["1.Introduction to Programming",
"2.Python Basic Syntax",
"3.Arithmetic Operators and Expressions",
"4.Basic Input and Output in Python",
"5.Conditional Statements in Python",
"6.Logical Operators in Python",
"7.Introduction to Iteration and Loops",
"0.Exit"]

for x in lesson:
 print(x)
print("-"*60)
ans = int(input("\nWhich lesson you want to view (0...7): "))
print("")
if ans == 1:
 print("=" * 60)
 print("     LESSON 1: INTRODUCTION TO PROGRAMMING")
 print("=" * 60)

 print("""
 WHAT IS A PROGRAMMING LANGUAGE?
 A programming language is used to give instructions
 to a computer to perform specific tasks.

 COMMON PROGRAMMING LANGUAGES:
 - Python: Beginner-friendly and versatile.
 - Java: Used for applications and systems.
 - C/C++: Used for games and system programming.
 - JavaScript: Used for interactive websites.
 - PHP: Used for web development.
 - Ruby: Used for web applications.

 WHAT IS PYTHON?
 Python is a high-level, interpreted, general-purpose
 programming language created by Guido van Rossum in 1991.

 WHY LEARN PYTHON?
 - Easy to learn and understand.
 - Simple and readable syntax.
 - Used in AI, websites, automation, and games.
 - Has a large programming community.

 PYTHON EDITORS:
 - PyCharm
 - Visual Studio Code
 - Jupyter Notebook
 """)
 
 print("-"*60)
 print("                      ASSESSMENT")
 print("-"*60)
 print("\n1.Yes\n2.No")
 ans2 = int(input("Would you like to take a short quiz?: "))
  
 if ans2 == 1:
  print("\n1.Multiple Choices\n2.Identification\n3.Fill in d blank")
  ans3 = int(input("What type of quiz would u like to take?: "))
  print("")
  print("-"*60)
  
  if ans3 == 1:
    
 
elif ans == 2:
 print("=" * 60)
 print("LESSON 2: PYTHON BASIC SYNTAX")
 print("=" * 60)

 print("""
 WHAT IS SYNTAX?
 Syntax refers to the rules for writing correct Python code.

 1. CASE-SENSITIVE
 Python recognizes uppercase and lowercase letters
 as different characters.

 2. INDENTATION
 Spaces are used to identify blocks of code.

 Example:
 if 10 > 5:
    print("Ten is greater.")

 3. PRINT STATEMENT
 The print() function displays information on the screen.

 Example:
 print("Welcome!")

 4. COMMENTS
 Comments are notes ignored by Python.
 They begin with the # symbol.

 Example:
 # This is a comment

 5. VARIABLES
 A variable stores information that can be used
 and changed in a program.

 Example:
 name = "Aki"
 age = 18

 VARIABLE NAMING RULES:
 - Must begin with a letter or underscore.
 - Cannot begin with a number.
 - No spaces or special characters.
 - Names are case-sensitive.

 6. CONSTANTS
 A constant is a value intended to remain unchanged.

 Example:
 PI = 3.14159

 7. BASIC DATA TYPES

 int - Whole numbers. Example: age = 18
 float - Decimal numbers. Example: grade = 89.5
 str - Text or characters. Example: name = "Aki"
 bool - True or False. Example: is_student = True

 REMEMBER:
 - Text needs quotation marks.
 - Numbers do not need quotation marks.
 - Follow proper indentation.
""")

elif ans == 3:
 print("=" * 60)
 print("LESSON 3: ARITHMETIC OPERATORS AND EXPRESSIONS")
 print("=" * 60)

 print("""
 WHAT ARE ARITHMETIC OPERATORS?
 These are symbols used to perform mathematical
 calculations in Python.

 OPERATORS:

 +   Addition
 -   Subtraction
 *   Multiplication
 /   Division
 //  Floor Division
 %   Modulus (remainder)
 **  Exponentiation (power)

 Example:
 a = 10
 b = 5

 print(a + b)   # 15
 print(a - b)   # 5
 print(a * b)   # 50
 print(a / b)   # 2.0
 print(a // b)  # 2
 print(a % b)   # 0
 print(a ** b)  # 100000

 WHAT IS AN EXPRESSION?
 An expression combines values, variables, and
 operators to produce a result.

 ORDER OF OPERATIONS: PEMDAS
 P - Parentheses
 E - Exponents
 M - Multiplication
 D - Division
 A - Addition
 S - Subtraction

 Example:
 print(2 + 3 * 4)

 Output: 14
""")

elif ans == 4:
 print("=" * 60)
 print("LESSON 4: BASIC INPUT AND OUTPUT")
 print("=" * 60)

 print("""
 WHAT IS INPUT?
 Input allows a program to receive information
 from the user.

 input() FUNCTION
 Used to receive information through the keyboard.

 Example:
 name = input("Enter your name: ")
 print("Hello,", name)

 IMPORTANT:
 input() returns a string by default.

 CONVERTING INPUT:

 int() - Converts input into a whole number.
 float() - Converts input into a decimal number.

 Example:
 age = int(input("Enter your age: "))
 grade = float(input("Enter your grade: "))

 print("Age:", age)
 print("Grade:", grade)

 PRACTICAL EXAMPLES:
 - Grade Calculator
 - BMI Calculator
 - Grocery Store Receipt
 - Simple Sales Calculator
""")

elif ans == 5:
 print("=" * 60)
 print("LESSON 5: CONDITIONAL STATEMENTS")
 print("=" * 60)

 print("""
 WHAT ARE CONDITIONAL STATEMENTS?
 They allow a program to make decisions based
 on whether a condition is True or False.

 COMPARISON OPERATORS:

 ==  Equal to
 !=  Not equal to
 >   Greater than
 <   Less than
 >=  Greater than or equal to
 <=  Less than or equal to

 1. IF STATEMENT
 Executes code when a condition is True.

 Example:
 age = 18
 if age >= 18:
    print("Adult")

 2. IF-ELSE STATEMENT
 Provides another action when the condition is False.

 Example:
 score = 65
 if score >= 75:
    print("Passed")
 else:
    print("Failed")

 3. IF-ELIF-ELSE STATEMENT
 Used to check multiple conditions.

 Example:
 score = 85

 if score >= 90:
    print("Excellent")
 elif score >= 80:
    print("Very Good")
 else:
    print("Needs Improvement")

 4. NESTED CONDITIONS
 An if statement placed inside another if statement.

 Example:
 age = 20
 has_id = True

 if age >= 18:
    if has_id:
              print("Allowed")
""")

elif ans == 6:
 print("=" * 60)
 print("LESSON 6: LOGICAL OPERATORS")
 print("=" * 60)

 print("""
 WHAT ARE LOGICAL OPERATORS?
 They combine or reverse conditions in a program.

 THREE MAIN LOGICAL OPERATORS:

 1. AND
 Both conditions must be True.

 Example:
 age = 20
 has_id = True

 if age >= 18 and has_id:
    print("Allowed")

 2. OR
 At least one condition must be True.

 Example:
 day = "Saturday"

 if day == "Saturday" or day == "Sunday":
    print("Weekend")

 3. NOT
 Reverses the result of a condition.

 Example:
 is_raining = False

 if not is_raining:
    print("You can go outside.")

 REMEMBER:
 and = Both conditions are True.
 or = At least one condition is True.
 not = Reverses the result.
""")

elif ans == 7:
 print("=" * 60)
 print("LESSON 7: INTRODUCTION TO ITERATION AND LOOPS")
 print("=" * 60)

 print("""
 WHAT IS ITERATION?
 Iteration means repeating a set of instructions
 multiple times.

 WHY USE LOOPS?
 Loops reduce repeated code and make programs
 shorter and easier to manage.

 TYPES OF LOOPS:

 1. FOR LOOP
 Used when the number of repetitions is known
 or when going through a sequence.

 Example:
 for number in range(1, 6):
    print(number)

 Output: 1 2 3 4 5

 2. WHILE LOOP
 Repeats instructions while a condition is True.

 Example:
 count = 1

 while count <= 5:
    print(count)
    count += 1

 Output: 1 2 3 4 5

 3. WHILE TRUE
 Repeats continuously until stopped.

 Example:
 while True:
    name = input("Enter name (X to exit): ")

    if name.upper() == "X":
        break

    print("Hello,", name)

 THE break STATEMENT
 The break statement immediately stops a loop.

 REMEMBER:
 - for = Repeats through a sequence.
 - while = Repeats while a condition is True.
 - range() = Generates a sequence of numbers.
 - break = Stops the loop.
 - Indentation is required inside loops.
""") 

elif ans == 0:
 print("Thank-you for checking our program ^^")
else:
 print("Your answer didn't match any of the choices -_-")        

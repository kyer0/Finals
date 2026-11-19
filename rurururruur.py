print("="*60)
print("                 WELCOME TO PYTHON TUTORIAL")
print("="*60)
print("\nWelcome, learner!")

def vl():
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
    ans = int(input("\n      Which lesson you want to view (0...7): "))
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
        a = ["B","C","B","A","D","C"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1.What is a programming language used for?
        A. Playing music      B. Giving instructions to a computer
        C. Drawing pictures   D. Browsing the internet 
    
        2.Who created Python?
        A. Bill Gates         B. Mark Zuckerberg
        C. Guido van Rossum   D. James Gosling 
    
        3.In what year was Python created?
        A. 1985  B. 1991  C. 2000  D. 2010 
    
        4.Which programming language is beginner-friendly?
        A. Python  B. C++  C. Assembly  D. Machine Code 
    
        5.Which language is commonly used for interactive websites?
        A. Ruby  B. Java  C. C/C++  D. JavaScript 
    
        6.Which of the following is a Python editor?
        A. Microsoft Word     B. PowerPoint
        C. PyCharm            D. Photoshop 
        """)
    
      elif ans3 == 2:
        a = ["PROGRAMMING LANGUAGE","GUIDO VAN ROSSUM","1991","HIGH LEVEL","PYCHARM","JAVASCRIPT"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1.What is the term for a language used to give instructions to a computer?
        
        2.Who created Python?
        
        3.What year was Python created?
        
        4.What type of programming language is Python that is easy to understand?
        
        5.What Python editor is commonly used for writing and running code?
        
        6.What programming language is commonly used for interactive websites?
        """)
        
      elif ans3 == 3:
        a = ["HIGH","GUIDO VAN ROSSUM","1991","INTERPRETED","GAMES","PYCHARM"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1.Python is a __________-level programming language.
        
        2.Python was created by __________.
        
        3.Python was created in the year __________.
        
        4.Python is an __________ programming language.
        
        5.Python is used in AI, websites, automation, and __________.
        
        6.__________ is one example of a Python editor.
        """)
        
      else:
        print("Invalid quiz type dawg..")
        
     elif ans2 == 2:
      print("")
      print("-"*60)
      
     else:
      print("\nSorry we didn't quite catch that...")
     
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
        a = ["B", "A", "C", "D", "A", "C"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. What does syntax refer to in Python?
        A. Computer hardware       B. Rules for writing correct code
        C. Internet connection     D. Programming speed
    
        2. Is Python case-sensitive?
        A. Yes  B. No  C. Sometimes  D. Only with numbers
    
        3. What is indentation used for?
        A. Adding colors       B. Creating variables
        C. Identifying blocks of code  D. Printing text
    
        4. Which symbol is used to create a comment?
        A. @  B. $  C. &  D. #
    
        5. Which data type stores whole numbers?
        A. int  B. float  C. str  D. bool
    
        6. Which is a valid variable name?
        A. 2name  B. my name  C. my_name  D. my-name
        """)
    
      elif ans3 == 2:
        a = ["SYNTAX", "INDENTATION", "PRINT()", "#", "VARIABLE", "BOOL"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What refers to the rules for writing correct Python code?
    
        2. What is the term for spaces used to identify blocks of code?
    
        3. What function displays information on the screen?
    
        4. What symbol is used to begin a comment?
    
        5. What do you call a storage location for information in a program?
    
        6. What data type represents True or False?
        """)
    
      elif ans3 == 3:
        a = ["CASE", "PRINT()", "#", "INT", "FLOAT", "UNCHANGED"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. Python is __________-sensitive.
    
        2. The __________ function displays information on the screen.
    
        3. A comment begins with the __________ symbol.
    
        4. The __________ data type stores whole numbers.
    
        5. The __________ data type stores decimal numbers.
    
        6. A constant is a value intended to remain __________.
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\nSorry we didn't quite catch that...")
    
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
        a = ["A", "B", "C", "D", "B", "A"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. Which operator is used for addition?
        A. +  B. -  C. *  D. /
    
        2. Which operator is used for multiplication?
        A. /  B. *  C. %  D. //
    
        3. What does the // operator represent?
        A. Division  B. Modulus  C. Floor Division  D. Exponentiation
    
        4. Which operator is used to get the remainder?
        A. +  B. **  C. //  D. %
    
        5. What is the result of 2 + 3 * 4?
        A. 20  B. 14  C. 24  D. 9
    
        6. What does PEMDAS stand for?
        A. Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
        B. Print, Enter, Multiply, Divide, Add, Subtract
        C. Power, Equal, Multiply, Divide, Add, Solve
        D. Parentheses, Equal, Modulus, Division, Addition, Syntax
        """)
    
      elif ans3 == 2:
        a = ["ARITHMETIC OPERATORS", "**", "%", "//", "EXPRESSION", "PEMDAS"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What are symbols used to perform mathematical calculations called?
    
        2. What operator is used for exponentiation?
    
        3. What operator returns the remainder of a division?
    
        4. What operator performs floor division?
    
        5. What do you call a combination of values, variables, and operators that produces a result?
    
        6. What order of operations is used in Python calculations?
        """)
    
      elif ans3 == 3:
        a = ["-", "/", "*", "**", "%", "EXPONENTS"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. The __________ operator is used for subtraction.
    
        2. The __________ operator is used for division.
    
        3. The __________ operator is used for multiplication.
    
        4. The __________ operator is used to calculate powers.
    
        5. The modulus operator uses the __________ symbol.
    
        6. In PEMDAS, the letter E stands for __________.
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\nSorry we didn't quite catch that...")
    
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
        a = ["B", "C", "A", "D", "B", "D"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. What is input in Python?
        A. Displaying information  B. Receiving information from the user
        C. Deleting information    D. Closing a program
    
        2. Which function receives information through the keyboard?
        A. print()  B. int()  C. input()  D. float()
    
        3. What data type does input() return by default?
        A. String  B. Integer  C. Float  D. Boolean
    
        4. Which function converts a value into a whole number?
        A. str()  B. float()  C. print()  D. int()
    
        5. Which function converts a value into a decimal number?
        A. int()  B. float()  C. input()  D. print()
    
        6. Which of the following is an example of a practical Python program?
        A. Grade Calculator  B. BMI Calculator
        C. Grocery Store Receipt  D. All of the above
        """)
    
      elif ans3 == 2:
        a = ["INPUT()", "PRINT()", "STRING", "INT()", "FLOAT()", "INPUT"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What function is used to receive information from the user?
    
        2. What function displays information on the screen?
    
        3. What data type does input() return by default?
    
        4. What function converts input into a whole number?
    
        5. What function converts input into a decimal number?
    
        6. What do you call information entered by the user into a program?
        """)
    
      elif ans3 == 3:
        a = ["INPUT()", "PRINT()", "STRING", "INT()", "FLOAT()", "INT"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. The __________ function receives information from the user.
    
        2. The __________ function displays output on the screen.
    
        3. The input() function returns a __________ by default.
    
        4. Use __________ to convert input into a whole number.
    
        5. Use __________ to convert input into a decimal number.
    
        6. age = __________(input('Enter age: '))
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\nSorry we didn't quite catch that...")
    
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
        a = ["B", "C", "A", "D", "B", "C"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. What are conditional statements used for?
        A. Repeating code  B. Making decisions
        C. Displaying images  D. Receiving input
    
        2. Which operator checks if two values are equal?
        A. =  B. !=  C. ==  D. >
    
        3. Which statement executes code when a condition is True?
        A. if  B. else  C. break  D. while
    
        4. What keyword provides an alternative action when an if condition is False?
        A. elif  B. if  C. and  D. else
    
        5. Which statement is used to check multiple conditions?
        A. if  B. if-elif-else  C. print  D. input
    
        6. What is a nested condition?
        A. A loop inside a loop
        B. A variable inside a function
        C. An if statement inside another if statement
        D. A comment inside code
        """)
    
      elif ans3 == 2:
        a = ["CONDITIONAL STATEMENTS", "==", "!=", "ELSE", "ELIF", "NESTED CONDITION"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What statements allow a program to make decisions based on conditions?
    
        2. Which comparison operator means equal to?
    
        3. Which comparison operator means not equal to?
    
        4. What keyword is used when the if condition is False?
    
        5. What keyword checks another condition after an if statement?
    
        6. What is an if statement placed inside another if statement called?
        """)
    
      elif ans3 == 3:
        a = ["IF", "ELSE", "ELIF", "==", ">", "<="]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. The __________ statement executes code when a condition is True.
    
        2. The __________ keyword provides an alternative action.
    
        3. The __________ keyword checks additional conditions.
    
        4. The __________ operator checks if values are equal.
    
        5. The __________ operator means greater than.
    
        6. The __________ operator means less than or equal to.
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\nSorry we didn't quite catch that...")
    
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
        a = ["A", "C", "B", "D", "B", "A"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. What are logical operators used for?
        A. Combining or reversing conditions
        B. Performing multiplication
        C. Printing information
        D. Creating variables
    
        2. Which logical operator requires both conditions to be True?
        A. or  B. not  C. and  D. if
    
        3. Which logical operator requires at least one condition to be True?
        A. and  B. or  C. not  D. else
    
        4. Which operator reverses the result of a condition?
        A. and  B. or  C. if  D. not
    
        5. What is the result of True and False?
        A. True  B. False  C. None  D. Error
    
        6. What is the result of True or False?
        A. True  B. False  C. None  D. Error
        """)
    
      elif ans3 == 2:
        a = ["LOGICAL OPERATORS", "AND", "OR", "NOT", "TRUE", "TRUE"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What operators combine or reverse conditions in Python?
    
        2. Which operator requires both conditions to be True?
    
        3. Which operator requires at least one condition to be True?
    
        4. Which operator reverses the result of a condition?
    
        5. What is the result of True and True?
    
        6. What is the result of not False?
        """)
    
      elif ans3 == 3:
        a = ["AND", "OR", "NOT", "TRUE AND FALSE", "AND", "OR"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. The __________ operator requires both conditions to be True.
    
        2. The __________ operator requires at least one condition to be True.
    
        3. The __________ operator reverses a condition's result.
    
        4. In Python, __________ and __________ are the two Boolean values.
    
        5. True __________ False produces False.
    
        6. True __________ False produces True.
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\nSorry we didn't quite catch that...")
    
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
        a = ["B", "C", "A", "D", "B", "C"]
        print("                  MULTIPLE CHOICES")
        print("-"*60)
        print("""
        1. What is iteration?
        A. Deleting code  B. Repeating instructions multiple times
        C. Creating variables  D. Receiving input
    
        2. Which loop is commonly used when the number of repetitions is known?
        A. if loop  B. while loop  C. for loop  D. break loop
    
        3. Which loop repeats while a condition is True?
        A. while loop  B. for loop  C. if statement  D. print loop
    
        4. What is the purpose of range()?
        A. Stop a program  B. Display text
        C. Receive input  D. Generate a sequence of numbers
    
        5. Which statement immediately stops a loop?
        A. continue  B. break  C. print  D. range
    
        6. What is the output of range(1, 6) when printed using a for loop?
        A. 1 2 3 4 5 6  B. 0 1 2 3 4 5
        C. 1 2 3 4 5  D. 2 3 4 5 6
        """)
    
      elif ans3 == 2:
        a = ["ITERATION", "FOR LOOP", "WHILE LOOP", "RANGE()", "BREAK", "WHILE TRUE"]
        print("                    IDENTIFICATION")
        print("-"*60)
        print("""
        1. What is the process of repeating a set of instructions called?
    
        2. What loop is used to go through a sequence?
    
        3. What loop repeats while a condition is True?
    
        4. What function generates a sequence of numbers?
    
        5. What statement immediately stops a loop?
    
        6. What type of loop repeats continuously until stopped?
        """)
    
      elif ans3 == 3:
        a = ["ITERATION", "FOR", "WHILE", "RANGE()", "BREAK", "INDENTATION"]
        print("                          F-I-T-B")
        print("-"*60)
        print("""
        1. __________ means repeating a set of instructions multiple times.
    
        2. The __________ loop is used to go through a sequence.
    
        3. The __________ loop repeats while a condition is True.
    
        4. The __________ function generates a sequence of numbers.
    
        5. The __________ statement immediately stops a loop.
    
        6. The __________ statement is required inside loops to identify code blocks.
        """)
        
      else:
        print("Invalid quiz type dawg..")
    
     elif ans2 == 2:
      print("")
      print("-"*60)
     else:
      print("\n      Sorry we didn't quite catch that...")
    
    elif ans == 0:
     print("-"*60)
     print("\n       Thank-you for checking our program ^^")
     return
    else:
     ans2 = 0
     print("Your answer didn't match any of the choices -_-")
     
    if ans >= 1 and ans <= 7:
     if ans2 == 1 and (ans3 == 1 or ans3 == 2 or ans3 == 3):
      print("-"*60)
      ans4 = [
        input("Enter your answer for number 1: ").upper(),
        input("Enter your answer for number 2: ").upper(),
        input("Enter your answer for number 3: ").upper(),
        input("Enter your answer for number 4: ").upper(),
        input("Enter your answer for number 5: ").upper(),
        input("Enter your answer for number 6: ").upper()
      ]
      print("-"*60)
      scr = 0
      if ans4[0] == a[0]:
        print(f'1.Ur answer {ans4[0]} is correct.')
        scr += 1
      else:
        print(f'1.Incorrect, the correct answer is {a[0]}')
        scr += 0
      if ans4[1] == a[1]:
        print(f'2.Ur answer {ans4[1]} is correct.')
        scr += 1
      else:
        print(f'2.Incorrect, the correct answer is {a[1]}')
        scr += 0
      if ans4[2] == a[2]:
        print(f'3.Ur answer {ans4[2]} is correct.')
        scr += 1
      else:
        print(f'3.Incorrect, the correct answer is {a[2]}')
        scr += 0
      if ans4[3] == a[3]:
        print(f'4.Ur answer {ans4[3]} is correct.')
        scr += 1
      else:
        print(f'4.Incorrect, the correct answer is {a[3]}')
        scr += 0
      if ans4[4] == a[4]:
        print(f'5.Ur answer {ans4[4]} is correct.')
        scr += 1
      else:
        print(f'5.Incorrect, the correct answer is {a[4]}')
        scr += 0
      if ans4[5] == a[5]:
        print(f'6.Ur answer {ans4[5]} is correct.')
        scr += 1
      else:
        print(f'6.Incorrect, the correct answer is {a[5]}')
        scr += 0  
      print("-"*60)
      print(f'                    Your score is {scr}')
          
     else:
        print("")

vl()

while True:
    
    print("-"*60)
    print("1. Yes")
    print("2. No")

    ans5 = int(input("Would u like to view another lesson brochaco?: "))

    if ans5 == 1:
        print("\nReturning to lesson menu...\n")
        vl()

    elif ans5 == 2:
        print("-"*60)
        print("\n                       Ty Mwamwa")
        print("-"*60)
        break

    else:
        print("\nInvalid Choice...")
    
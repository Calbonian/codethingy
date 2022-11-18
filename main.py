import sys
import random
while (True):
    print("Choose a program to run.")
    print("Choose either security system, promotional spammer, calculator, password encrypter, random word generator,")
    print("or language creator.")
    Program = str(input())
    if Program == "security system" or Program == "Security system" or Program == "SECURITY SYSTEM" or Program == "Security System" or Program == "Security" or Program == "security" or Program == "SECURITY" or Program == "System" or Program == "system" or Program == "SYSTEM":
        A = 1
        B = 2
        C = 3
        D = A+B
        E = A+C
        F = B+C
        G = A+B+C
        H = A+B+C+D+E+F+G
        H += A+B+C+D+E+F+G
        Password1 = "Thisiscool"
        Password2 = "IamCaleb"
        Password3 = "IamJoshua"
        Password4 = "IEXIST!"
        user = input("What is your name? ") 
        print(user)
        print("Hello," + user) 
        if user == "Caleb" or user == "caleb" or user == "CALEB" or user == "C" or user == "c":
            print("Access granted")
            print(7-3+10-1+B-2+A-C+3+D-E+F+3+5+H)
        elif user == "Joshua" or user == "joshua" or user == "JOSHUA" or user == "J" or user == "j":
            print("Access granted")
            print(7-3+1-1+B-F-2+A-C+3+D-E+F+3+C+5+H)
        else:
            print("Access denied")
            print(7-3+1-1+B-F-2+A-C+-+D-E-F+3+C-5-H)
            quit()
        Password1 = input("What is Password 1? ") 
        Password2 = input("What is Password 2? ")
        Password3 = input("What is Password 3? ")
        Password4 = input("What is Password 4? ") 
        if Password1 == "Thisiscool":
            print("CORRECT")
            Checker1 = 26
        else:
            Checker1 = -14
        if Password2 == "IamCaleb":
            print("CORRECT")
            Checker2 = 26
        else:
            Checker2 = -14
        if Password3 == "IamJoshua":
            print("CORRECT")
            Checker3 = 26
        else:
            Checker3 = -14
        if Password4 == "IEXIST!":
            print("CORRECT")
            Checker4 = 26
        else:
            Checker4 = -14
        Checker5 = Checker1+Checker2+Checker3+Checker4
        if Checker5 == 104:
            print("ACCESS GRANTED")
            print(7+3)
            print('Blah')
            print('Hello world')
            Me = "Caleb"
            print(Me)
            print(A+B)
            print(A+B-C)
            print (D+E)
            print (D+E-F)
            pass
        elif Checker5 == 64:
            print("ACCESS DENIED")
            sys.exit()
        elif Checker5 == 24:
            print("ACCESS DENIED")
            sys.exit()
        elif Checker5 == -16:
            print("ACCESS DENIED")
            sys.exit()
        elif Checker5 == -56:
            print("ACCESS DENIED")
            sys.exit()
        else:
            print("ERROR!")
            quit()
    elif Program == "promotional spammer" or Program == "Promotional spammer" or Program == "PROMOTIONAL SPAMMER" or Program == "Promotional Spammer" or Program == "spammer" or Program == "Spammer" or Program == "SPAMMER" or Program == "promotional" or Program == "Promotional" or Program == "PROMOTIONAL":
        while (True):
            def Function1(TEXT):
                print(TEXT)
                print("I am Caleb")
                print("I am the best")
            Function1('HI')
    elif Program == "calculator" or Program == "Calculator" or Program == "CALCULATOR":
        def Function2():
            print("What is your first number?")
            Num1 = input()
            print("What is your operation?")
            Operation = input()
            print("What is your second number?")
            Num2 = input()
            Num1 = int(Num1)
            Num2 = int(Num2)
            if Operation == "+":
                Answer = Num1 + Num2
            elif Operation == "-":
                Answer = Num1 - Num2
            elif Operation == "x" or Operation == "*":
                Answer = Num1 * Num2
            elif Operation == "/" or Operation == "÷" or Operation == "—":
                Answer = Num1 / Num2
            elif Operation == "%" or Operation == "% of":
                Answer = Num1 * Num2 / 100
            else:
                Answer = "INVALID OPERATION"
            print(Answer)
            print("Do you want to calculate another problem? Answer Yes or No.")
            Continue = input()
            if Continue == 'Yes' or Continue == 'yes' or Continue == 'YES':
                Function2()
            elif Continue == 'No' or Continue == 'no' or Continue == 'NO':
                Program = "None"
            else:
                print("ERROR!")
        Function2()
    elif Program == "password encrypter" or Program == "Password Encrypter" or Program == "Password encrypter" or Program == "PASSWORD ENCRYPTER" or Program == "encrypter" or Program == "Encrypter" or Program == "ENCRYPTER":
        def Function3():
            print("Hello, welcome to the password encrypter.")
            print("Please enter a message below to be encoded.")
            print("Enter only numbers.")
            Message = input()
            Message = int(Message)
            Encryption = Message * 35637809243 / 6283908493 -6378928732 /63278134 +3273948 * 42789374
            print(Encryption)
            print("Do you want to unencript the message?")
            Unencrypt = input()
            if Unencrypt == "YES" or Unencrypt == "Yes" or Unencrypt == "yes":
                print(Message)
            elif Unencrypt == "NO" or Unencrypt == "No" or Unencrypt == "no":
                pass
            else:
                print("ERROR!")
            print("Do you want to encrypt another message?")
            Reencrypt = input()
            if Reencrypt == "YES" or Reencrypt == "Yes" or Reencrypt == "yes":
                Function3()
            elif Reencrypt == "NO" or Reencrypt == "No" or Reencrypt == "no":
                Program = "None"
            else:
                print("ERROR!")
        Function3()
    if Program == "Random word generator" or Program == "random word generator" or Program == "RANDOM WORD GENERATOR" or Program == "Random Word Generator" or Program == "Random" or Program == "random" or Program == "RANDOM" or Program == "Word" or Program == "word" or Program == "WORD" or Program == "generator" or Program == "Generator" or Program == "GENERATOR" or Program == "Random Word" or Program == "Random word" or Program == "random word" or Program == "RANDOM WORD" or Program == "Word Generator" or Program == "Word generator" or Program == "word generator" or Program == "WORD GENERATOR" or Program == "Random Generator" or Program == "Random generator" or Program == "random generator" or Program == "RANDOM GENERATOR":
        def Function1():
            V = ["A", "E", "I", "O", "U"]
            C = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Y", "Z"]
            R1 = random.choice(C)
            R2 = random.choice(V)
            R3 = random.choice(C)
            R4 = random.choice(V)
            R5 = random.choice(C)
            print("Welcome to the random word generator.")
            print("This generator will generate a 5 letter word.")
            print("Do you want to generate a random word?")
            Generate = input()
            if Generate == "Yes" or Generate == "yes" or Generate == "YES" or Generate == "Y" or Generate == "y":
                print(R1+R2+R3+R4+R5)
            else:
                Program = "None"
        Function1()
    if Program == "Language Creator" or Program == "Language creator" or Program == "language creator" or Program == "LANGUAGE CREATOR" or Program == "Language" or Program == "language" or Program == "LANGUAGE" or Program == "creator" or Program == "Creator" or Program == "CREATOR":
        def L():
            print("Welcome to the new language creator")
            print("Enter 37 values of numbers between 1 and 10, letters, and spaces.")
            A=input()
            B=input()
            C=input()
            D=input()
            E=input()
            F=input()
            G=input()
            H=input()
            I=input()
            J=input()
            K=input()
            L=input()
            M=input()
            N=input()
            O=input()
            P=input()
            Q=input()
            R=input()
            S=input()
            T=input()
            U=input()
            V=input()
            W=input()
            X=input()
            Y=input()
            Z=input()
            N0=input()
            N1=input()
            N2=input()
            N3=input()
            N4=input()
            N5=input()
            N6=input()
            N7=input()
            N8=input()
            N9=input()
            SP=input()
            print("What is your language's name?")
            NA=input()
            print("Congratulations. You made your own language. Now, some numbers and words will be displayed, first in English, then in "+NA)
            print("1.""Language")
            print(L+A+N+G+U+A+G+E)
            print("2.""Hello world")
            print(H+E+L+L+O+SP+W+O+R+L+D)
            print("3.""359687")
            print(N3+N5+N9+N6+N8+N7)
            print("4.""9179553")
            print(N9+N1+N7+N9+N5+N5+N3)
            print("5.""4u59fd87")
            print(N4+U+N5+N9+F+D+N8+N7)
            print("6.""8794ieksgdskz8")
            print(N8+N7+N9+N4+I+E+K+S+G+D+S+K+Z+N8)
            
        print("Do you want to create a language?")
        ST=input()
        if ST == "Yes" or ST == "YES" or ST == "yes":
            pass
        elif ST == "No" or ST == "no" or ST == "NO":
            Program = "None"
        else:
            print("ERROR!")
            print("Do you want to create another language?")
            ST=input()
            if ST == "Yes" or ST == "YES" or ST == "yes":
                pass
            elif ST == "No" or ST == "no" or ST == "NO":
                Program = "None"
            else:
                print("ERROR!")
                quit()
        L()
        print("Do you want to create another language?")
        CO=input()
        if CO == "Yes" or CO == "YES" or CO == "yes":
            pass
        elif CO == "No" or CO == "no" or CO == "NO":
            Program = "None"
        else:
            print("ERROR!")
            print("Do you want to create another language?")
            CO=input()
            if CO == "Yes" or CO == "YES" or CO == "yes":
                pass
            elif CO == "No" or CO == "no" or CO == "NO":
                Program = "None"
            else:
                print("ERROR!")
                quit()
    else:
        if Program == "None" or Program == True:
            Program == True
        else:
            Program == False
        if Program == False:
            print("INVALID PROGRAM")
            sys.exit()
            quit()
        else:
            pass
    print("Do you want to use another program? Answer Yes or No.")
    Continue2 = input()
    if Continue2 == 'Yes' or Continue2 == 'yes' or Continue2 == 'YES':
        pass
    elif Continue2 == 'No' or Continue2 == 'no' or Continue2 == 'NO':
        sys.exit()
        quit()
    else:
        print("ERROR!")
        quit()

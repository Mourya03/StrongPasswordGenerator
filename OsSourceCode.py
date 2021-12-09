import random
import array
import time
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print("*"*100)
    print("*"*44+" P W - G E N "+"*"*43)
    print("*"*100)
    return("   ")

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '*', '(', ')']
  
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
  
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
  
def gen_pass():
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
          
    return password

if __name__ == "__main__":
    try:
        while(1):
            clear()
            print("\nSELECT AN OPTION : \n")
            print("1) Generate a Random Strong Password\n2) Generate n number of Random Strong Passwords")
            print("3) Check Whether my Password is Strong\n4) How to create Strong Password ?\n5) Why do I need a Strong Password ?\n6) Change Password Length\n\n0) Exit Application")
            choice = int(input("Enter Your Choice : "))
            if choice==0:
                break
            elif choice==1:
                while(1):
                    for i in range(3):
                        clear()
                        print("\n\nGenerating a Password for you in",3-i,"seconds")
                        time.sleep(1)
                    clear()
                    print("\n\nYour Password :",gen_pass())
                    print("\n\nDo you want to generate another one ? <Y/N>")
                    choice2 = input("Your Choice : ").lower()
                    if choice2 == 'n' or choice2=='no':
                        break
            elif choice==2:
                while(1):
                    clear()
                    print("\n\nHow many passwords do you want ?")
                    n = int(input("Your Choice : "))
                    for i in range(3):
                        clear()
                        print("\n\nGenerating a Password for you in",3-i,"seconds")
                        time.sleep(1)
                    clear()
                    for i in range(n):
                        print("\n\nYour Password ",i+1,":",gen_pass())
                    print("\n\nDo you want to generate more ? <Y/N>")
                    choice2 = input("Your Choice : ").lower()
                    if choice2 == 'n' or choice2=='no':
                        break
            elif choice==3:
                clear()
                print("\n\nEnter Your Password : ")
                passw = input()
                f1,f2,f3,f4=0,0,0,0
                for i in passw:
                    if i in DIGITS:
                        f1=1
                    if i in LOCASE_CHARACTERS:
                        f2=1
                    if i in UPCASE_CHARACTERS:
                        f3=1
                    if i in SYMBOLS:
                        f4=1
                if f1+f2+f3+f4 == 4:
                    print("\n\nYour Password is Strong !")
                else:
                    print("\n\nYour Password is Weak !")
                for i in range(3):
                    print("Redirecting in",3-i,"seconds...")
                    time.sleep(3)
            elif choice==4:
                while(1):
                    clear()
                    print("\n\nA Strong Password contain atleast one of the below :")
                    print("\nLower Case Alphabets")
                    print(LOCASE_CHARACTERS)
                    print("\nUpper Case Alphabets")
                    print(UPCASE_CHARACTERS)
                    print("\nNumerical Digits")
                    print(DIGITS)
                    print("\nSymbols")
                    print(SYMBOLS)
                    print("\n\nGo Back <Y/N>")
                    choice2 = input("Your Choice : ").lower()
                    if choice2 == 'y' or choice2=='yes':
                        break
            elif choice==5:
                while(1):
                    clear()
                    print("\n\nThe more complex your password is, the more security it provides for your account.\nRemember that your account is where you store a great deal of sensitive information that you don’t want to have stolen.\nAs you understand, the stakes are very high.\nTherefore, taking care of your account password is crucial.")
                    print("\nYour account password should never include these:\n->any obvious combinations such as 12345, combinations of phone numbers and addresses, or your personal information;\n->any string with sequential numbers or letters;\n->any part of the username with a slight variation of the password;\n->words in the dictionary that a hacker can easily hack with the help of a dictionary program.")
                    print("\n\nNow that you’ve come up with the strongest password possible, \nit’s time to absorb some principles of good password security practice in daily life:\n\n->Never disclose usernames and passwords to third parties\n->Never store usernames and passwords on paper or in an unencrypted computer file\n->Update your account password at least every 6 months\n->Do not use passwords that have been used in the past\n->Never provide credentials when requested through email\n->Run regular virus scans on your computer\n->Use Two-Factor Authentication (2FA). With 2FA, you will receive a text message for log in and password reset requests.\n->Don’t save passwords or use “remember me” on public computers")
                    print("\n\nGo Back <Y/N>")
                    choice2 = input("Your Choice : ").lower()
                    if choice2 == 'y' or choice2=='yes':
                        break
            elif choice==6:
                clear()
                print("\n\nCurrent Password Length :",MAX_LEN)
                print("\nEnter Your Prefered Length :")
                n = int(input())
                if n<4:
                    print("Minimum length of the password is 4 !")
                else:
                    print("Do you want to change the length of the password to",n,"? <y/n> : ")
                    choice2=input().lower()
                    if choice2=='y' or choice2=='yes':
                        MAX_LEN = n
                    print("\n\nPassword Length Updated !")
                for i in range(3):
                    print("Redirecting in",3-i,"seconds")
                    time.sleep(1)

    except Exception as e:
        for i in range(3):
            clear()
            print("An Unexpected Error has Occured !",e)
            print("\nTerminating Application in",3-i,"seconds")
            time.sleep(i)
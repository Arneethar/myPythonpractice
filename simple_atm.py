#!/usr/bin/python3
myCustomers = {"lucy gamble": 1234,"anita matthew": 2345}

# This function checks if the username is available and if the password is correct
def isACustomer(name,password,myCustomers):
  unknown ="not found"
  for keys,values in myCustomers.items():
    if keys == name:
      if values == password:
        return name, True
      else:
        print("Invalid password")
        return name, False
    elif keys not in myCustomers:
      return unknown, False

  # This function prints the account balance of the user    
def enquiry(balance):
  return balance

# This function allows the user to make numerous deposits
def deposit2(balance):
  code1 = input("Enter the amount you wish to deposit\n> ")
  deposit2 = int(code1)
  print("You have just deposited ${:.2f}".format(deposit2))
  return deposit2 + balance

  # This function allows the user to withdraw money
def withdraw(balance):
  withdraw = int(input("How much do you want to withdraw\n> "))
  if withdraw < balance:
    balance = balance - withdraw
    print("You have just withdrawn ${:.2f}".format(withdraw))
    return balance   
  else:
    print("Insufficient funds, please deposit\nor kindly withdraw a lesser amount")
    print("")
    return balance
# End of functions

# Beginning of main

print("Welcome to SunCity Trust Bank")
print("")
name = input("Enter your name\n> ")
name = name.lower()
password = int(input("Enter your password\n> "))
try:
  Username,Status =isACustomer(name,password,myCustomers)
except (TypeError, NameError):
  print("")

print("")
  
try:
  if Status:
    newName = Username.title()
    print(f"Hi {newName}")
    code = 0
  code = input("Enter the amount you wish to deposit\n> ")
  deposit = int(code)         
  print("To view balance input 1")
  print("To withdraw input 2")
  print("To deposit new cash input 3")
# code = input("Choose a number\n> ")
  balance = deposit
  while code:
# != "exit":
    print("")
    code = input("Choose a number\n> ")
    print("")
    remainder = balance
    if code == "1":
     remainder = enquiry(balance)
     print(f"Account balance")
     print("${:.2f}".format(remainder))
     print("")
    elif code == "2": 
      balance = withdraw(remainder)
      remainder = balance
    elif code == "3":
      balance = deposit2(balance)
      remainder = balance 
    elif code == "exit" or code == "quit" or code == "q":
      print("Thank you for banking with us")
      break
    else:
      print("please choose a valid number")
    
except NameError:
    print("Incorrect details\nKindly input your right details")



  




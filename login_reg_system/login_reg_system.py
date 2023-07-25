# Matts Login Registration system


#############################################################################
# Login function
#############################################################################
def func_login():

  # Ask User for Username:
  print("You have chosen to login!\n")

  # Reading text file, storing as a list in *lines*
  while True:

    username_inp = input("Please Enter Your Username:\n")

    with open('database.txt', 'r') as database:
      lines = database.read().splitlines()

      #If the lines.index is a number - checking it is ok - then move on
      try:
        lines.index(username_inp)

        password = input("Please input Your password:")

        if lines[lines.index(username_inp) + 1] == password:

          print("You have Logged in Successfully!!")

          # Retuning the inputted username which they use to login
          # This means that they don't need to enter their username twice
          return username_inp
          break

        else:
          print("Your Password is Incorrect")

    # Except means that it does not work if there is a value error - aka if the index doesn't             output an element number
      except ValueError:
        print("Your Username is Incorrect")


#############################################################################
# Register function
#############################################################################


def func_registration():

  print("You Have Chosen to Register!")

  username = ""
  password = ""

  # Stopping people from entering nothing as a username or password
  while username == "":
    username = input("Please Enter a Username:")
    if username == "":
      print("Sorry, Not a Valid Username!")

  # Reading text file, storing as a list in *lines*
  with open('database.txt') as database:
    lines = database.read().splitlines()

  # Check for username in odd numbered elements of list
  # start:stop:step
  if username in lines[::2]:
    print("Sorry That Username Already Exists!")

  else:
    # Writing the username onto a new line
    with open('database.txt', 'a') as database:
      database.write('\n')
      database.write(username)

    while password == "":
      password = input("Please Enter a Password:")
      if password == "":
        print("Sorry, Not a Valid Password!")

    # Writing a password onto a new line
    with open('database.txt', 'a') as database:
      database.write('\n')
      database.write(password)
      print("You Have Successfully Registered!!")


#############################################################################
# Reset Password:
#############################################################################


def func_reset():

  print("You Have Chosen to Change Your Password!")
  print("Confirming Login Information")

  # This is waiting for the login function to follow through until it hits 'return' and then returns the username input so it doesnt need to be entered twice

  username_inp = func_login()

  # Making sure that 'password'exists beyond the while loop
  password = ""

  # Equivalent of a do loop - in that it must happen once, and then loops if passwords don't match

  while password == ""
    password = input("Please Enter a New Password:")
    if password == input("Please Confirm Your Password:"):
      break
    password = ""

  # Establishes a blank array of data

  newdatabase = []

  # Opening the file so it can be overwritten using 'w'
  with open("database.txt", "r") as database:

    lines = database.read().splitlines()
    found_user = False
    for line in lines:
      # If the found user is false (which it isn't by standard) then the line is copied and           added into the new database
      if found_user == False:
        newdatabase.append(line)
      # If the usernername is found, add the new password as the next line below it into the new         data set
      else:
        found_user = False
        newdatabase.append(password)
      # If the username is found, this triggers the else loop
      if line == username_inp:
        found_user = True

  # Clears the original file and overwrites with the new data set - but checking here that the         length of the new data set is the same as the old one
  with open("database.txt", "w") as database:
    if len(newdatabase) == len(lines):
      i = 0
      while i < len(newdatabase):
        database.write(newdatabase[i])
        if i != len(newdatabase) - 1:
          database.write("\n")

        i += 1

    # The only potential issue with this method is that it has to rewrite all lines in the file -      if this number was massive it isnt ideal - but we are using small data sets


#############################################################################
# Main:
#############################################################################
while True:
  try:
    print("-------------------------------------------")

    print("Welcome to the Login / Registration System!")
    print("-------------------------------------------\n")
    print(" 1 - Login\n")
    print(" 2 - Register\n")
    print(" 3 - Change Your Password\n")
    print(" 4 - Exit\n")
    print("-------------------------------------------")

    user_input = int(input())

    match user_input:
      case 1:
        func_login()
      case 2:
        func_registration()
      case 3:
        func_reset()
      case 4:
        break
      case _:
        print("Sorry try again!")

  except:
    print("Sorry try again!")

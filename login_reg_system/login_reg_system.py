# Matts Login Registration system


#############################################################################
# Login function
#############################################################################
def func_login():


  # Ask User for Username:
  print("You have chosen to login!\n")
  print("Please Enter a Username:\n")
  username = input()

  # Reading text file, storing as a list in *lines*
  with open('database.txt') as database:
    lines = database.read().splitlines()
    
  # Check for username in odd numbered elements of list
  # start:stop:step
  if username in lines[::2]:
    print("Please input a password:")
    password = input()

    # Check for password in even numbered elements in the list
    if password in lines[1::2]:
      print("You have Logged in Successfully!!")
    else:
      print("Your password was incorrect")

  else:
    print("Username not Found")

#############################################################################
# Register function
#############################################################################

def func_registration():
  print("You Have Chosen to Register!")
  print("Please Enter a Username:")

  username = input()

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

    print("Please Enter a Password:")

    password = input()

    # Writing a password onto a new line
    with open('database.txt', 'a') as database:
      database.write('\n')
      database.write(password)
      print("You Have Successfully Registered!!")

#############################################################################
# Overwrite Line function:
#############################################################################
def replace_line(filename, line_number, text):
  with open(filename) as file:
    lines = file.readlines()


#############################################################################
# Reset Password:
#############################################################################

def func_reset():
  print("You Have Chosen to Change Your Password!")
  print("Please Enter Your Username:")

  username = input()

  # Reading text file, storing as a list in *lines*
  with open('database.txt') as database:
    lines = database.read().splitlines()

  # Check for username in odd numbered elements of list
  # start:stop:step
  if username in lines[::2]: 


    print("Please Enter a New Password:")

    password = input()

    print("Please Confirm Your Password:")

    password_confirm = input()

    if password == password_confirm:

      # with open('database.txt', 'r') as database:
      #   line_number = lines.index(username)
      #   password_line_number = line_number + 1



      #   database.seek(int(password_line_number))
      #   database.replace(password_confirm)
      #   database.truncate()
        
        







#############################################################################
# Main:
#############################################################################
while True: 
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
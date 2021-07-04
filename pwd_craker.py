import random
import pyautogui


# store all possible character and number in chars variable like so
#convert string chars to a list
#get password from the user using pyaoutgui interfence
#declare guess_password to store guessed password as an empty string
#give guess_password random chars from chars_list with length of password for example my passwaord is abc so random lendth will be 3 chars
#using random.choices(list, k) function K: represent how much random char we want from a list
chars ="abcdefghijklmnopqrstuvwxyz0123456789"
chars_list=list(chars)


password =pyautogui.password("Enter you password: ")

guess_password=""

while(guess_password !=password):
    guess_password=random.choices(chars_list, k=len(password))
    print("<======="+str(guess_password)+"=======>")

    if(guess_password==list(password)):
        print("Your password is: "+"".join(guess_password))
        break

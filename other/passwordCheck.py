psd1 = input("Enter Password: ")
psd2 = "BALU BAVA"

class PasswordError(Exception):
    def __init__(self):
        Exception(self)
try:
    if not psd1==psd2:
        raise PasswordError
except PasswordError:
    print("Password error,try again!")
finally:
    print(" ^_^ THANK YOU ^_^ ")
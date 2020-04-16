import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

class InvalidPasswordException(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    password = str(input("Enter your password: "))
    if len(password)<8:
        logging.info("Password is less than 8 characters long.")
        raise InvalidPasswordException("Password is less than 8 characters long.")
except InvalidPasswordException as error:
    print(error,"Please enter a password that is 8 characters or more.")
    
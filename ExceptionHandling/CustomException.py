import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawl(amount):
    if amount>500:
        logging.error("Withdrawing more than 500")
        raise OverTheLimitException("You cannot withdraw more than 500")

withdrawl(501)
# all the exception handling i write here

import sys


def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()  # all the info like on which file the exception occur, on which line the exception happen, all info stored in this variable
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))  # first variable contain file name, second on which line error happen, and last variable error message

    return error_message


class CustomeException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
    

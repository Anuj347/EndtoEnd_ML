#for exceptional handling purpose
#custom exception handling---documentation

import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message
#whenever the error raises the above function should be called

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        #we are inheriting from the above function
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
#Now this will be common for entire code


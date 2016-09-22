#
# Copyright 2015 riteme
#

UNKNOWN = 0
ACCEPTED = 1
ERROR = 2
INTERNAL_ERROR = 3

status = UNKNOWN
message = ""

input_file = ""
std_output = ""
user_output = ""

def init(_input_file, _std_output, _user_output):
    global input_file
    global std_output
    global user_output

    input_file = _input_file
    std_output = _std_output
    user_output = _user_output

def judge():
    global status
    global message

    try:
        flag,  message = _judge()
        if flag:
            status = ACCEPTED
        else:
            status = ERROR
    except Exception as e:
        status = INTERNAL_ERROR
        message = str(e)

def _judge():
    raise NotImplementedError("Judger not implemented.")

#!/usr/bin/env python3

import os
import time
import shutil
import subprocess
import readline
from subprocess import *

COMPILE_COMMAND = 'g++ -std=c++11 -lpthread'

def diff(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    lineNumber = 0
    L1 = [x for x in f1.readlines() if x.strip() != '']
    L2 = [x for x in f2.readlines() if x.strip() != '']
    f1.close()
    f2.close()

    if len(L1) != len(L2):
        return (False, 0, 'Incorrect file size', 'Incorrect file size')

    for index in range(0, len(L2)):
        lineNumber += 1
        # print(L1[index], L2[index])

        if L1[index].strip() != L2[index].strip():
            return (False, lineNumber, L1[index].strip(), L2[index].strip())

    return (True, 0, '', '')


readline.parse_and_bind('tab: complete')
filename = input("File Name: ")
interval = input('Start/End: ')
timelimit = input("Time Limit: ")

if filename.strip() == '':
    print('(error) Filename can\'t be None.')
    exit(-1)

if interval.strip() == '':
    interval = '1 10'

if timelimit.strip() == '':
    timelimit = '1.0'

D = interval.split()
startid = int(D[0])
endid = int(D[1])

timelimit = float(timelimit)

print('(info) Compiling source...')
status = os.system("{} {}.cpp".format(COMPILE_COMMAND, filename))

if status != 0:
    print('\033[36mCompile Error\033[0m')
    exit(-1)

total_passed = 0
total_time = 0.0
final_status = 'Accepted'

for i in range(startid, endid + 1):
    print('\n\033[32m# Testcase\033[0m {}'.format(i))

    time.sleep(0.5)
    try:
        os.remove('{}.out'.format(filename))
    except:
        pass 

    shutil.copy2('./{0}/{0}{1}.in'.format(filename, i), '{0}.in'.format(filename))

    # ......
    os.system('pkill -9 a.out')

    starttime = time.time()

    flag = True

    try:
        status = Popen(['./a.out']).wait(timeout = timelimit)
    except subprocess.TimeoutExpired:
        if final_status == 'Accepted':
            final_status = 'Time Limit Exceeded'
        flag = False

    endtime = time.time()
    passed = endtime - starttime
    print("Time:   {}s".format(passed))

    if not flag:        
        print('Status: \033[35mTime Limit Exceeded\033[0m')

    if flag:
        if status != 0:
            print('Status: \033[33mRuntime Error\033[0m')

            if final_status == 'Accepted':
                final_status = 'Runtime Error'
            flag = False

    if flag:
        succeeded, lineNo, std, mine = diff('./{0}/{0}{1}.out'.format(filename, i), '{}.out'.format(filename))
        if not succeeded:
            print('Status: \033[31mWrong Answer\033[0m')
            
            if lineNo == 0:
                print('(info) {}'.format(std))
            else:
                print('(info) At line {0}:\n\texpected: {1}\n\tbut read: {2}'.format(lineNo, std, mine))

            if final_status == 'Accepted':
                final_status = 'Wrong Answer'
            flag = False

    if flag:
        print('Status: \033[34mAccepted\033[0m')
        total_passed += 1

    total_time += passed

color_table = {
    'Accepted': '\033[34m',
    'Wrong Answer': '\033[31m',
    'Time Limit Exceeded': '\033[35m',
    'Runtime Error': '\033[33m'
}

print('\n\033[32m### ANALYZE ###\033[0m')
print('Status: {}{}\033[0m\nScores: {}\nTime:   {}s'.format(
    color_table[final_status],
    final_status,
    100.0 * (float(total_passed) / (endid - startid + 1)),
    total_time
    )
)


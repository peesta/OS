import os
import sys
import struct

FIFO_NAME = 'calc_fifo'

def create_task(operator, operand1, operand2):
    return struct.pack('c i i', operator, operand1, operand2)


def take_task():
    operator = input('Enter operator (+, -, *, /): ')
    if operator == 'exit':
        os.remove(FIFO_NAME)
        sys.exit(0)
    operand1 = input('Enter first operand: ')
    if operand1 == 'exit':
        os.remove(FIFO_NAME)
        sys.exit(0)
    else: operand1 = int(operand1)
    operand2 = input('Enter second operand: ')
    if operand2 == 'exit':
        os.remove(FIFO_NAME)
        sys.exit(0)
    else: operand2 = int(operand2)

    return operator, operand1, operand2

while True:
    if not os.path.exists(FIFO_NAME):
        os.mkfifo(FIFO_NAME)
    
    operator, operand1, operand2 = take_task()

    if not operator in ['+', '-', '*', '/']:
        print('Not supported operator')
        sys.exit(1)
    if operator == '/' and operand2 == 0:
        print(f'{operand1} can not divided by zero')
        sys.exit(1)

    task = create_task(operator.encode(), operand1, operand2)

    with open(FIFO_NAME, 'wb') as fifo:
        fifo.write(task)


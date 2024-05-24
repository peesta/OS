import os
import struct

FIFO_NAME = 'calc_fifo'

def calculation(operator, operand1, operand2):
    print(operator)
    if operator == b'+':
        return operand1 + operand2
    if operator == b'-':
        return operand1 - operand2
    if operator == b'*':
        return operand1 * operand2
    if operator == b'/':
        return operand1 / operand2


while True:
    if os.path.exists(FIFO_NAME):
            
        with open(FIFO_NAME, 'rb') as fifo:
            task = fifo.read(struct.calcsize('iii'))
            operator, operand1, operand2 = struct.unpack('iii', task)
            result = calculation(operator, operand1, operand2)
            print(f'Result: {result}')
        

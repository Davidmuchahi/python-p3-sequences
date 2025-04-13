#!/usr/bin/env python3

def print_fibonacci(length):
    if length==0:
        print([])
        return
    
    sequence=[]
    for i in range(length):
        if i==0:
            sequence.append(0)

        elif i==1:
            sequence.append(1)
        else:
            next_number=sequence[i-1]+sequence[i-2]
            sequence.append(next_number)
    
    print(sequence)

              
print_fibonacci(0)
print_fibonacci(1)  
print_fibonacci(2)  
print_fibonacci(5)  
print_fibonacci(10) 


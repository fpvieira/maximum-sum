#-*- coding: utf-8 -*-
import sys

def execute_sum(vector):
    first = 0
    _sum = max_sum = i = j = 0
    for last in range(len(vector)):
        valor = vector[last]
        _sum += int(valor)
        if _sum > max_sum:
            max_sum = _sum
            i = first
            j = last
        elif _sum < 0:
            first = last + 1
            _sum = 0

    return vector[i:j+1]

def prepar_vector(sys_arguments):
    arguments = sys_arguments.split(",")
    vector = []
    for arg in arguments:
        vector.append(int(arg))

    return vector

def print_interval(sub_vector, vector):
    first_element = sub_vector[0]
    last_element = sub_vector[len(sub_vector)-1]
    
    return vector.index(first_element), vector.index(last_element)


def main():
    vector = prepar_vector(sys.argv[1])
    sub_vector = execute_sum(vector)
    position_numbers = print_interval(sub_vector,vector)

    print 'As posições são : %s e %s '%(position_numbers[0], position_numbers[1])

if __name__ == '__main__':
    main()
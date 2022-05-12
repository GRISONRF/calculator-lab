"""Functions for common math operations."""


def add(num_list): # + ['1', '2' 3 4 5]
    """Return the sum of the two input integers."""
    sum_list = 0
    for num in num_list:
        sum_list += num
    return sum_list



def subtract(num_list):
    """Return the second number subtracted from the first."""
    sub_list = num_list[0]
    for num in num_list[1:]:
        sub_list -= num
    return sub_list


def multiply(num_list):
    """Multiply the two inputs together."""
    mult_list = 1
    for num in num_list:
        mult_list *= num
    return mult_list



def divide(num_list):
    """Divide the first input by the second, returning a floating point."""
    div_list = num_list[0]
    for num in num_list[1:]:
        div_list /= num
    return div_list



def square(num_list):
    """Return the square of the input."""
    sq_list = []
    for num in num_list:
        sq_list.append(num**2) 
    return sq_list



def cube(num_list): 
    """Return the cube of the input."""
    cub_list = []
    for num in num_list:
        cub_list.append(num**3)
    return cub_list


def power(num_list): 
    """Raise num1 to the power of num and return the value."""
    pow_list = pow(num_list[0], num_list[1])
    return pow_list


def mod(num_list):
    return num_list[0] % num_list[1]

    

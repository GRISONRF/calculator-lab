"""CLI application for a prefix-notation calculator."""


from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    equation = input("Enter your equation: ").strip() 
    if equation == 'q' or equation == 'quit':
        break
    else:
        lst_equation = equation.split()
        num_list = [int(num) for num in lst_equation[1:]]
        signal = lst_equation[0]

        
        if signal == '+':
            sum_num = add(num_list)
            print(sum_num)

        elif signal == '-':
            sub_num = subtract(num_list)
            print(sub_num)
            
        elif signal == '/':
            div_num = divide(num_list)
            print(div_num)

        elif signal == '*':
            mult_num = multiply(num_list)
            print(mult_num)

        elif signal == 'square':
            squ_num = square(num_list)
            print(squ_num)
            
        elif signal == 'cube':
            cube_num = cube(num_list)
            print(cube_num)

        elif signal == 'pow':
            if len(num_list) > 2:
                print("Only 2 numbers")
            else:    
                pow_num = power(num_list)
                print(pow_num)
                
        elif signal == 'mod':
            if len(num_list) > 2:
                print("Only 2 numbers")
            else:
                mod_num = mod(num_list)
                print(mod_num)
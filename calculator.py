"""CLI application for a prefix-notation calculator."""


from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    equation = input("Enter your equation: ").strip() # cube 3
    if equation == 'q' or equation == 'quit':
        break
    else:
        lst_equation = equation.split()
        signal = lst_equation[0]
        num1 = int(lst_equation[1])
         
        if len(lst_equation) == 3:    
            num2 = int(lst_equation[2]) 

        if signal == '+':
            sum_num = add(num1, num2)
            print(sum_num)

        elif signal == '-':
            sub_num = subtract(num1,num2)
            print(sub_num)
            
        elif signal == '/':
            div_num = divide(num1,num2)
            print(div_num)

        elif signal == '*':
            mult_num = multiply(num1,num2)
            print(mult_num)

        elif signal == 'square':
            squ_num = square(num1)
            print(squ_num)
            
        elif signal == 'cube':
            cube_num = cube(num1)
            print(cube_num)

        elif signal == 'pow':
            pow_num = power(num1,num2)
            print(pow_num)
            
        elif signal == 'mod':
            mod_num = mod(num1,num2)
            print(mod_num)
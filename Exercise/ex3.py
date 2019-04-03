from random import randint

running = True

while running:
    num1 = randint(-20, 20)
    num2 = randint(-20, 20)

    coin = randint(0, 1)
    result = 0
    status = 'True'

    if coin == 1:
        result = num1 + num2
        status = 'True'
    else: 
        result = randint(-40, 40)
        while result == num1 + num2:
            result = randint(-40, 40)
        status = 'False'

    print(num1, '+', num2, '=', result)
    ans = str(input("True or false:"))
    if ans == status:
        print("Win")
    elif ans == 'Exit': 
        running = False
    elif ans != status: 
        print('Lose')
        
   


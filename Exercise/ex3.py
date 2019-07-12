from random import randint
running = True
point = 0
while running:
    num1 = randint(-20, 20)
    num2 = randint(-20, 20)
    coin = randint(0, 1)
    result = 0
    status = 'true'
    if coin == 1:
        result = num1 + num2
    else: 
        result = randint(-40, 40)
        while result == num1 + num2:
            result = randint(-40, 40)
        status = 'false'
    print(num1, '+', num2, '=', result)
    ans = str(input("True or false:"))
    if ans == status:
        point += 1
        print("Point:", point)
    elif ans == 'Exit': 
        running = False
    else: 
        print('Lose')
        running = False
    print("\n")
        
   


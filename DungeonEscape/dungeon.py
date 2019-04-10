from random import randint
map = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for i in range(4):
    for j in range(4):
        map[i][j] = '-'
    print("")

player = randint(0, 15)
key = randint(0, 15)
end = randint(0, 15)

while player == key and key == end and end == player:
    player = randint(0, 15)
    key = randint(0, 15)
    end = randint(0, 15)

playerX = int(player / 4)
playerY = player % 4
keyX = int(key / 4)
keyY = key % 4
endX = int(end /4)
endY = end % 4
keys = 1
map[playerX][playerY] = 'P'
map[keyX][keyY] = 'K'
map[endX][endY] = "E"

def printMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end = " ")
        print("")

printMap(map)

while True:

    move = input("Your move(a, s ,d ,w): ")

    if move == "a":
        if playerY > 0:
            map[playerX][playerY] = "-"
            playerY -= 1
            map[playerX][playerY] = "P"

            if playerX == keyX and playerY == keyY:
                keys -= 1

    elif move == "s":
        if playerX < 3:
            map[playerX][playerY] = "-"
            playerX += 1
            map[playerX][playerY] = "P"

            if playerX == keyX and playerY == keyY:
                keys -= 1

    elif  move == "d":
        if playerY < 3:
            map[playerX][playerY] = "-"
            playerY += 1
            map[playerX][playerY] = "P"

            if playerX == keyX and playerY == keyY:
                keys -= 1

    elif move == "w":
        if playerX > 0:
            map[playerX][playerY] = "-"
            playerX -= 1
            map[playerX][playerY] = "P"

            if playerX == keyX and playerY == keyY:
                keys -= 1
                            
    map[endX][endY] = "E"

    printMap(map)

    if playerX == endX and playerY == endY and keys != 0:
        print("Collect the key first")
        
    elif playerX == endX and playerY == endY and keys == 0:
        print("You win")
        break
   



    








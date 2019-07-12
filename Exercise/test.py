# from random import randint
# a = randint(0, 9)
# print(a)

# res = input("Radius?")
# r = float(res)
# area = 3.14 * r ** 2
# print("Area =" , area)
# res = input("Temperature in C?")
# c = float(res)
# f = c * 1.8 + 32
# print("Temperature in F", f)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(20, 9, -1):
#     print(i)

# res = input("nhap n")
# n = int(res)
# res = input("nhap m")
# m = int(res)
# if n < m:
#     print("n phai lon hon m. Nhap lai")
#     res = input("nhap n ")
#     n = int(res)
#     res = input("nhap m ")
#     m = int(res)
# else:
#     for i in range(n, m -1, -1):
#         print(i)

# print("How many legs a spider has?")
# print("\t1. None")
# print("\t2. 4 legs")
# print("\t3. 8 legs")
# print("\t4. 12 legs")

# res = input("Your answer? ")
# ans = str(res)
# if ans != "1" and ans != '2' and ans != '3' and ans != '4':
#     res = input("Invalid option. Choose again: ")
#     ans = str(res)

# if ans == "1" or ans == "2" or ans == "4":
#     print('wrong. Answer is 3')
# else:
#     print("You win")

# res = input('Enter a word: ')
# word = str(res)
# wordArr = list(word)
# while len(wordArr) > 0:
#     index = randint(0, len(wordArr) - 1)
#     char = wordArr[index]
#     print(char)
#     wordArr.pop(index)

# words = ['abcd', 'qwer', 'played', 'python']
# ask = randint(0, len(words) - 1)
# word = words[ask]
# wordArr = list(word)
# char = []
# while len(wordArr) > 0:
#     index = randint(0, len(wordArr) - 1)
#     char.append(wordArr[index])
#     wordArr.pop(index)
# print(*char, sep = ' ')
# res = input("Guess: ")
# ans = str(res)
# if ans == words[ask]:
#     print('Dung')
# else: print('Sai')

# for i in range(6):
#     for i in range(360):
#         forward(2)
#         left(1)

#     left(60)

# speed(1)

# mainloop()

import datetime
import pyglet
from pyglet.media import Source, Player, load

alarm = int(input("alarm: "))
m = datetime.datetime.now().minute
while True:
    if m == alarm:
        mp3File = "crowd-cheering.mp3"

        player = Player()
        source = load(mp3File)
        player.queue(source)
        player.play()
        while True:
            interact = (input("play, pause or stop:"))
            if interact == "play":
                player.play()
            elif interact == "pause":
                player.pause()
            elif interact == "stop":
                player.pause()
                break
        break
    else:
        m = datetime.datetime.now().minute
    


    
    
    





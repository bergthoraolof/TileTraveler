#1. Which implementation was easier and why?
#   Mér fannst auðaveldara að gera forritið án falla einfaldlega af því að ég
#   hef gert fleiri forrit svoleiðis og skil það mun betur.

#2. Which implementation is more readable and why?
#   Seinni útgáfan er klárlega auðlæsilegri því lykkjan/aðalkóðinn er styttri og búið er að
#   skilgreina allar aðgerðir áður enn lykkjan byrjar og ef nöfnin á föllunum eru skýr 
#   á að vera frekar einfallt að skilja lykkjuna.
#3. Which problems in the first implementations were you able 
#   to solve with the latter implementation?
#   Stærsta vandamálið við fyrri útgáfuna er hvað kóðinn er langur og flókinn.
#   Föllin í seinni útgáfunni hjálpa til við að leysa þetta vandamál með
#   að gera kóðann skýrari og auðlæsilegri.


def travel(x_y, t):
    if x_y == (1, 1):
        t = tile_1
    elif x_y == (1, 2):
        t = tile_2
    elif x_y == (1, 3):
        t = tile_3
    elif x_y == (2, 1):
        t = tile_4
    elif x_y == (2, 2):
        t = tile_5
    elif x_y == (2, 3):
        t = tile_6
    elif x_y == (3, 1):
        t = tile_7
    elif x_y == (3, 2):
        t = tile_8
    elif x_y == (3, 3):
        t = tile_9
    print("You can travel: ",t)

def way():
    way = input("Direction: ")
    way = way.lower()
    return way

def notvalid():
    print("Not a valid direction!")

def move(a, b, c):
    if a == "n":
        b = b
        c = c + 1
    elif a == "s":
        b = b
        c = c - 1
    elif a == "e":
        c = c
        b = b + 1
    elif a == "w":
        c = c
        b = b - 1
    return b, c

def validmove(m):
    if m == (1, 1):
        valid = "n"
    elif m == (1, 2):
        valid = "nes"
    elif m == (1, 3):
        valid = "es"
    elif m == (2, 1):
        valid = "n"
    elif m == (2, 2):
        valid = "sw"
    elif m == (2, 3):
        valid = "ew"
    elif m == (3, 2):
        valid = "ns"
    elif m == (3, 3):
        valid = "sw"
    return valid

x = 1
y = 1
position = (x, y)
valid = ""

tile_1 = "(N)orth."
tile_2 = "(N)orth or (E)ast or (S)outh."
tile_3 = "(E)ast or (S)outh."
tile_4 = "(N)orth."
tile_5 = "(S)outh or (W)est."
tile_6 = "(E)ast or (W)est."
tile_7 = "victory!"
tile_8 = "(N)orth or (S)outh."
tile_9 = "(S)outh or (W)est."
tile = ""

while position != (3, 1):
    travel(position, tile)
    while True:
        direction = way()
        if direction in validmove(position):
            x, y = move(direction, x, y)
            position = (x, y)
            break
        else:
            notvalid()
print("Victory!")
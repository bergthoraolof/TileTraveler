#Athuga hvar leikmaðurinn er staðsettur og hvert hann getur farið
#Taka við inputi sem segir í hvaða átt leikmaðurinn vill fara
#Ath hvort hægt er að fara í áttina sem leikmaðurinn setti inn
#Ef ekki er hægt að fara þá átt prenta: Not a valid direction!
#Annars færa staðsetningu leikmannsins í þá átt og breyta núverandi staðsetingu hans.
#Ef staðseting leikmanns er (3,1) er leikmaðurinn búinn að vinna og forritið á að hætta að keyra.
#Áður en forritið hættir að keyra á að láta leikmanninn vita að hann er búinn að vinna leikinn með því að prenta Victory!.

position_x = 1
position_y = 1

while position_x != 3 or position_y != 1:
    if position_x == 1:
        if position_y == 1:
            possible_directions = 'n'
            print("You can travel: (N)orth.")
        elif position_y == 2:
            possible_directions = 'nes'
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif position_y == 3:
            possible_directions == 'se'
            print("You can travel: (E)ast or (S)outh.")
    elif position_x == 2:
        if position_y == 1:
            possible_directions = 'n'
            print("You can travel: (N)orth.")
        elif position_y == 2:
            possible_directions == 'ws'
            print("You can travel: (S)outh or (W)est.")
        elif position_y == 3:
            possible_directions == 'we'
            print("You can travel: (E)ast or (W)est.")
    elif position_x == 3:
        if position_y == 2:
            possible_directions = 'ns'
            print("You can travel: (N)orth or (S)outh.")
        if position_y == 3:
            possible_directions = 'ws'
            print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    direction = direction.lower()
    if direction in possible_directions:
        if direction == 'n':
            position_y += 1
        elif direction == 's':
            position_y -= 1
        elif direction == 'e':
            position_x += 1
        elif direction == 'w':
            position_x -= 1
    else:
        print("Not a valid direction!")
        direction = input("Direction: ")
        direction = direction.lower()
        if direction in possible_directions:
            if direction == "n":
                position_y += 1
            elif direction == "e":
                position_x += 1
            elif direction == "s":
                position_y -= 1
            elif direction == "w":
                position_x -= 1
        
        
        
print("Victory!")


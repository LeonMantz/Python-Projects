import random

b = 0
g = [0, 1, 2]  # grammes
s = [0, 1, 2]  # sthles

for i in range(100):

    tablo = []  # 3x3 teragwno
    win = False
    pl = 0
    kapakia = []

    for j in range(9):
        kapakia.append(0)  # mikro
        kapakia.append(1)  # mesaio
        kapakia.append(2)  # megalo

    for z in range(3):
        row = []
        for w in range(3):
            row.append(-1)  # to -1 sumbolizei to keno
        tablo.append(row)

    while win == False and len(kapakia) > 0:

        choice = kapakia.pop(random.randrange(len(kapakia)))
        gram = random.choice(g)
        sthlh = random.choice(s)

        if (tablo[gram][sthlh]) == -1 or (tablo[gram][sthlh] < choice):

            tablo[gram][sthlh] = choice
            pl = pl + 1

            if ((tablo[gram][0]) == (tablo[gram][1]) == (tablo[gram][2]) and (tablo[gram][0] != -1) and (tablo[gram][1] != -1) and (tablo[gram][2] != -1)) or (tablo[gram][0]) < (tablo[gram][1]) < (tablo[gram][2]):
                win = True

            elif ((tablo[0][sthlh] == tablo[1][sthlh] == tablo[2][sthlh]) and (tablo[0][sthlh] != -1) and (tablo[1][sthlh] != -1) and (tablo[2][sthlh] != -1)) or (tablo[0][sthlh] < tablo[1][sthlh] < tablo[2][sthlh]):
                win = True

            elif ((tablo[0][0] == tablo[1][1] == tablo[2][2]) and (tablo[0][0] != -1) and (tablo[1][1] != -1) and (tablo[2][2] != -1) and (gram == sthlh)) or (tablo[0][0] < tablo[1][1] < tablo[2][2]):
                win = True

            elif ((tablo[2][0] == tablo[1][1] == tablo[0][2]) and (tablo[2][0] != -1) and (tablo[1][1] != -1) and (tablo[0][2] != -1) and (gram + sthlh == 2)) or (tablo[2][0] < tablo[1][1] < tablo[0][2]):
                win = True

            elif (tablo[gram][0]) == (tablo[gram][1]) == (tablo[gram][2] == -1):
                win = False
            elif (tablo[0][sthlh] == tablo[1][sthlh] == tablo[2][sthlh] == -1):
                win = False
            elif (tablo[0][0] == tablo[1][1] == tablo[2][2] == -1) and gram == sthlh:
                win = False
            elif (tablo[2][0] == tablo[1][1] == tablo[0][2] == -1) and (gram + sthlh == 3):
                win = False
            else:
                win = False
    b = pl + b

print(b / 100)



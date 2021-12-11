from sys import stdin, stdout

def main():
    kerites, emberek = map(int, stdin.readline().split())
    festek = []
    zold = 0
    piros = 0
    for i in range(kerites):
        festek.append([])
    szinek = []
    for i in range(emberek):
        sor = list(map(str, stdin.readline().split()))
        sor2 = []
        sor2.append(sor[0])
        sor2.append(int(sor[1]))
        sor2.append(int(sor[2]))
        szinek.append(sor2)
    for i in range(emberek):
        for j in range(szinek[i][1]-1, szinek[i][2]):
            festek[j].append(szinek[i][0])
    for i in range(kerites):
        j = len(festek[i])
        if len(festek[i]) == 0:
            continue
        if len(festek[i]) == 1:
            if festek[i][0] == "Z":
                zold += 1
            else:
                piros += 1
        elif festek[i][j-1] == "Z" and festek[i][j-2] == "Z":
            zold += 1
        elif festek[i][j-1] == "P" and festek[i][j-2] == "P":
            piros += 1
    stdout.write(str(piros) + " " + str(zold))
main()
from sys import stdin, stdout
def main():
    elsoszam = int(stdin.readline())
    elsoszin = str(stdin.readline())
    masodikszam = int(stdin.readline())
    masodikszin = str(stdin.readline())
    pirosszam = 0
    zoldszam = 0
    megoldas = 0
    for i in range(elsoszam):
        if elsoszin[i] == "z":
            zoldszam += 1
        else:
            pirosszam += 1
    for i in range(masodikszam):
        if masodikszin[i] == "z":
            if pirosszam != 0:
                pirosszam -= 1
                megoldas += 1
        elif zoldszam != 0:
            zoldszam -= 1
            megoldas += 1
    stdout.write(str(megoldas))

main()
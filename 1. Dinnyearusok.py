from sys import stdin, stdout

def main():
    arus = int(stdin.readline())
    lakhely = list(map(int, stdin.readline().split()))
    aruszam = int(stdin.readline())
    aruhely = list(map(int, stdin.readline().split()))
    tavolsag = int(stdin.readline())
    megoldas = 0
    for i in range(arus):
        for j in aruhely:
            if tavolsag >= abs(lakhely[i] - j):
                megoldas += 1
                aruhely.remove(j)
                break
        if len(aruhely) == 0:
            break
    stdout.write(str(megoldas))
main()
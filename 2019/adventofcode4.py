laveste = 284639
hoyeste = 748759

tall = laveste
antall = 0


def to_paa_rad(tall):
    tall = str(tall)
    for i in range(10):
        a = tall.count(str(i))
        if a != 2:
            pass
        else:
            for u in range(5):
                if tall[u] == tall[u+1]:
                    return True


def okende(tall):
    tall = str(tall)
    lav = int(tall[0])
    for u in range(len(tall)):
        if lav <= int(tall[u]):
            lav = int(tall[u])
        else:
            return False
    return True


while tall <= hoyeste:
    if len(str(tall)) == 6:
        if laveste < tall < hoyeste:
            if to_paa_rad(tall):
                if okende(str(tall)):
                    antall += 1
                    print(f"{tall}, {to_paa_rad(tall), okende(tall)}")
    tall += 1

print(antall)
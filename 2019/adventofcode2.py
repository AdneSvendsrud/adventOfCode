adress = 0
noun = 0
verb = 0

for i in range(100):
    for j in range(100):
        with open("adventofcode2.txt", "r") as f:
            tall = f.readline()
            liste = tall.split(",")
            liste[1] = i
            noun = i
            liste[2] = j
            verb = j

        while True:
            try:
                if liste[adress] == "1":
                    adress += 1
                    tall1address = liste[adress]
                    tall1 = liste[int(tall1address)]
                    adress += 1
                    tall2address = liste[adress]
                    tall2 = liste[int(tall2address)]
                    adress += 1
                    tall3address = liste[adress]
                    tall3 = int(tall1) + int(tall2)
                    liste[int(tall3address)] = tall3
                    adress += 1
                elif liste[adress] == "2":
                    adress += 1
                    tall1address = liste[adress]
                    tall1 = liste[int(tall1address)]
                    adress += 1
                    tall2address = liste[adress]
                    tall2 = liste[int(tall2address)]
                    adress += 1
                    tall3address = liste[adress]
                    tall3 = int(tall1) * int(tall2)
                    liste[int(tall3address)] = tall3
                    adress += 1
                elif liste[adress] == "99":
                    print(liste[0], noun, verb, 100*noun+verb)
                    break
                else:
                    pass
            except ValueError:
                print("ValueError")
                break

print("Svaret:")
print(liste[0], noun, verb)
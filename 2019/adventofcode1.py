sumn = 0

with open("adventofcode1.txt", "r") as f:
    while True:
        try:
            mass = int(f.readline())
            fuel = (mass//3)-2
            sumn += fuel
            while ((fuel//3)-2) > 0:
                fuel = (fuel // 3) - 2
                sumn += fuel
                print(fuel)
        except:
            break

print()
print(sumn)

'''
This was another fun task, I ended up using globals to simulate the execution process, but I think it's fine in this case
There is however something wrong with my execution, as either task 1 or task 2 is correct, but not at the same time

The task was to read a bunch of operation, either noop or addx, which incremented the counter by 1 and 2 respecitvely
During operation addx was supposed to not increase the register, but then task 1 was wrong
addx was supposed to increment the register after the second cycle
'''
cycle = 1
register_X = 1
sumn = 0
cur_row = ""


def increment_cycle():
    # Globals aren't cool, but I'm using them to simulate "during execution
    global cycle, sumn, cur_row

    # Task 2, during the execution
    # print((cycle - 1) % 40, register_X)
    if register_X - 2 < ((cycle - 1) % 40) <= register_X or register_X < ((cycle-1) % 40) < register_X + 2:
        cur_row += "#"
    else:
        cur_row += "."
    if cycle % 40 == 0:
        print(f"Cycle\t {cycle - 39} ->\t {cur_row}\t <- Cycle {cycle}")
        cur_row = ""

    # Task 1 and cycle increment
    cycle += 1
    if (cycle - 20) % 40 == 0:
        sumn += cycle * register_X


with open('data/day10') as file:
    for line in file:
        command = line.strip().split()
        if command[0] == 'noop':
            increment_cycle()
        else:
            increment_cycle()
            # To solve part 1 uncomment the line below
            # register_X += int(command[1])
            increment_cycle()
            # To solve part 1 comment out the line below
            register_X += int(command[1])

print(f"Task 1: \t{sumn}")
print("If task 2 is readable then task 1 is wrong")


def check_length(input, threshold):
    return len(input) >= threshold


with open('data/day6') as file:
    data = file.read()

    # This is basically a set, because every element is unique
    searchBuffer = ""

    T1 = False
    T2 = False
    for index, char in enumerate(data):
        # This is possible to do with a ternery operator, but I think it's more readable as an if-statement
        # searchBuffer = searchBuffer + char if char not in searchBuffer else searchBuffer[searchBuffer.index(char) + 1:] + char
        if char not in searchBuffer:
            searchBuffer += char
        else:
            searchBuffer = searchBuffer[searchBuffer.index(char) + 1:] + char

        # Task 1
        if check_length(searchBuffer, 4) and not T1:
            print("Task 1:\t", index + 1)
            T1 = True

        # Task 2
        elif check_length(searchBuffer, 14) and not T2:
            print("Task 2:\t", index + 1)
            T2 = True

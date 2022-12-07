import sys

'''
Today's task was to create/traverse a filesystem, for this I decided to do some class-based action
Folders and files are represented as nodes and the tasks are solved by recursive functions with too long names
Task 1 was to find all folders with sizes under a given threshold, then sum the sizes
Task 2 was to find all folders with sizes above a given threshold, then return the smallest of these
The tasks could probably be solved using one function(a, b) where a > b, with task 1 having the threshold at a
and task 2 having the threshold at b. But since they return different values I'd rather split these into two
'''


class Node:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size


class File(Node):
    pass


class Folder(Node):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent
        self.children = {}

    def add_child(self, name, size=0):
        if size == 0:
            newFile = Folder(name, self)
        else:
            newFile = File(name, size)
            self.size += size
            parent = self.parent
            while parent:
                parent.size += size
                parent = parent.parent
        self.children[name] = newFile
        return newFile

    def change_directory(self, path):
        if path == '/':
            return self

        if path == '..' and self.parent:
            return self.parent

        # if we have no parent and try to move up, don't
        if path == '..':
            return self

        # Try to find child, if it does not exist, create it
        try:
            tmp = self.children[path]
            return tmp
        except KeyError:
            return self.add_child(path)


# Function to print the file directory tree, not necessary for the task
def print_tree(f, level):
    print('\t' * level, end='')

    if isinstance(f, File):
        print(f.name, f"(file, size={f.size})")
        return
    print(f.name, f'(dir, size={f.size})')
    for child in f.children:
        print_tree(child, level + 1)


# Function for task 1
def sum_folders_under_size_threshold(f, threshold):
    if isinstance(f, File):
        return 0

    sumn = 0
    for child in f.children.values():
        sumn += sum_folders_under_size_threshold(child, threshold)

    if f.size < threshold:
        return sumn + f.size

    return sumn


# Function for task 2
def find_folders_above_size_threshold(f, threshold):
    if isinstance(f, File):
        return

    folders = []
    for child in f.children.values():
        tmp = find_folders_above_size_threshold(child, threshold)
        if tmp:
            folders = tmp + folders[:]

    if f.size > threshold:
        folders.append(f)

    return folders


with open('data/day7') as file:
    root = None
    current_folder = None
    for line in file:
        stripped = line.strip().split()
        if stripped[0] == "$":
            if stripped[1] != 'ls':
                if not current_folder:
                    current_folder = Folder(stripped[2], current_folder)
                    root = current_folder

                current_folder = current_folder.change_directory(stripped[2])
        else:
            size = stripped[0]
            if stripped[0] == 'dir':
                current_folder.add_child(stripped[1])
            else:
                current_folder.add_child(stripped[1], int(size))

current_folder = root
# print_tree(cur, 0)
print(f"Task 1:\t{sum_folders_under_size_threshold(current_folder, 100000)}")

# Part 2
totalSpace = 70000000
neededSpace = 30000000
currentSpaceAvailable = neededSpace - (totalSpace - current_folder.size)

folders = find_folders_above_size_threshold(current_folder, currentSpaceAvailable)
lowest = sys.maxsize
for folder in folders:
    if folder.size < lowest:
        lowest = folder.size

print(f"Task 2:\t{lowest}")

import queue
print("\tKEY:\n\n\tS-111 = 1\n\tS-105 = 5\n\tBathrooms = R\n\tS-117 = 7\n\tS-118 = 8\n\tS-123 = 3\n")

#X will be defined later as an input of what room they want to go to from the main enterance
X = ""
#the map is created as a function to be able to have the value be used later on in the code instead of the map itself
#H's in the map signify walls, each room has its own number that corresponds to it, and yo uare able to walk through spaces
def createMap():
    map = []
    map.append(["H", "H", "H", "E", "H", "H", "H", "H", "H"])
    map.append(["H", "1", " ", " ", " ", " ", " ", " ", "H"])
    map.append(["H", "H", " ", " ", " ", " ", " ", "H", "H"])
    map.append(["H", "H", " ", " ", " ", " ", " ", "7", "H"])
    map.append(["H", "5", " ", " ", " ", " ", " ", "H", "H"])
    map.append(["H", "H", " ", " ", " ", " ", " ", "8", "H"])
    map.append(["H", "R", " ", " ", " ", " ", " ", "H", "H"])
    map.append(["H", "H", " ", " ", " ", " ", " ", "3", "H"])
    map.append(["H", "H", "H", "H", "H", "H", "H", "H", "H"])

    return map


def printMap(map, moves=""):
    #whenever enumerate is called for an item, it gives first the location and then the content after it, need it to find location, and thus needs 2 arguments in the for loop
    for x, pos in enumerate(map[0]):
        #checks if the specific block at the top row is the enterance, or E
        if pos == "E":
            #start, a local variable, is then set to the location of the enterance, which becomes a, or the x coordinate
            start = x
#see above comment
    a = start
    #b, or the y coordinate, starts off as 0 because you start off at the zero spot at the top
    b = 0
    pos = set()
    for move in moves:
        if move == "L":
            a -= 1

        elif move == "R":
            a += 1

        elif move == "U":
            b -= 1

        elif move == "D":
            b += 1
        pos.add((b, a))
#reformatting the map to be printable, end commands call to prevent a new line, (*)'s are the path markings towards where you need to go, and then finished printing
    for b, row in enumerate(map):
        for a, col in enumerate(row):
            if (b, a) in pos:
                #end="" calls for the line to not end by leaving it blank, would normally be \n
                print("* ", end="")
            else:
                print(col + " ", end="")
        print()

#valid checks to see if the latest move that
def valid(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "E":
            start = x

    a = start
    b = 0
    for move in moves:
        if move == "L":
            a -= 1

        elif move == "R":
            a += 1

        elif move == "U":
            b -= 1

        elif move == "D":
            b += 1
#if the a coordinate or the b coordinate end outside the map or on an H (walls), it returns the otherwise true function as false
        if not (0 <= a < len(map[0]) and 0 <= b < len(map)):
            return False
        elif (map[b][a] == "H"):
            return False

    return True


def findEnd(map, moves):
    for x, pos in enumerate(map[0]):
        if pos == "E":
            start = x

    a = start
    b = 0
    for move in moves:
        if move == "L":
            a -= 1

        elif move == "R":
            a += 1

        elif move == "U":
            b -= 1

        elif move == "D":
            b += 1
#if the area that you are moving to has the  same coordinates as the X variable, or the goal, it returns true and the loop at the bottom is broken
    if map[b][a] == str(X):
        print("\nPath: " + moves + "\n")
        printMap(map, moves)
        return True

    return False

def roompicker():
    global X
    X = input("Where would you like to go from the main enterance? ")
    if X == "1" or X == "5" or X == "R" or X == "7" or X == "8" or X == "3":
        pass
    else:
        roompicker()

# MAIN ALGORITHM
roompicker()
steplst = queue.Queue()
steplst.put("")

add = ""
map = createMap()
#this loop is broken when you find the end above,
while not findEnd(map, add):
    add = steplst.get()
    #adds each one of those directions to the queue, keeps running because of the while loop until the godal is reached
    for step in ["L", "R", "U", "D"]:
        put = add + step
        #runs through the valid function
        if valid(map, put):
            steplst.put(put)
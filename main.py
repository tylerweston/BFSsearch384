###########################################
# BFS for water jug problem
# CSC384 - Intro to AI
###########################################
# Tyler Weston, 2019

jug1size = 0
jug2size = 0

def do_main():

    # get jug sizes from user
    global jug1size
    jug1size = int(input("Jug 1 size:"))
    global jug2size
    jug2size = int(input("Jug 2 size:"))

    # get starting state
    startstate1 = input("Starting state jug 1:")
    startstate2 = input("Starting state jug 2:")

    #get goal state
    goalstate1 = input("Goal state jug 1:")
    goalstate2 = input("Goal state jug 2:")

    #pack tuples
    startstate = (int(startstate1), int(startstate2))
    goalstate = (int(goalstate1), int(goalstate2))

    # make our starting open list
    openlist = []
    openlist.append([startstate])

    # display starting info
    print("Jug sizes: " + str(jug1size) + ", " + str(jug2size))
    print("Starting state: " + str(startstate))
    print("Goal state: " + str(goalstate))

    while(1):   # main loop

        # check if we have anything left in open list
        # if not, there are no valid solutions
        if len(openlist) == 0:
            print("No solution found")
            exit(0)

        # get first entry from our open list
        curnode = openlist.pop(0)

        # check if this is a valid goal state
        if curnode[-1] == goalstate:
            print("Found solution:")
            print(curnode)
            exit(0)

        # add possible new nodes to our open list
        openlist += S(curnode)


# generate all possible actions that will not result in no-ops or cycles
# return a list of valid states
def S(node):
    # possible actions
    # ----------------
    # dump out jug1
    # dump out jug2
    # fill jug1
    # fill jug2
    # jug1 -> jug2
    # jug2 -> jug1

    # setup vars
    returnlist = []
    state = node[-1]
    jug1, jug2 = state

    # dump jug1
    if (0, jug2) != state:
        if not (0, jug2) in node:
            new_node = node.copy()
            new_node.append((0, jug2))
            returnlist.append(new_node)
    # dump jug2
    if (jug1, 0) != state:
        if not (jug1, 0) in node:
            new_node = node.copy()
            new_node.append((jug1, 0))
            returnlist.append(new_node)

    # fill jug1
    if (jug1size, jug2) != state:
        if not (jug1size, jug2) in node:
            new_node = node.copy()
            new_node.append((jug1size, jug2))
            returnlist.append(new_node)

    #fill jug2
    if (jug1, jug2size) != state:
        if not (jug1, jug2size) in node:
            new_node = node.copy()
            new_node.append((jug1, jug2size))
            returnlist.append(new_node)

    #jug1 -> jug2
    jug2space = jug2size - jug2
    pouramount = min(jug1, jug2space)
    jug2new = jug2 + pouramount
    jug1new = jug1 - pouramount
    if (jug1new, jug2new) != state:
        if not (jug1new, jug2new) in node:
            new_node = node.copy()
            new_node.append((jug1new, jug2new))
            returnlist.append(new_node)

    #jug2 -> jug1
    jug1space = jug1size - jug1
    pouramount = min(jug2, jug1space)
    jug1new = jug1 + pouramount
    jug2new = jug2 - pouramount
    if (jug1new, jug2new) != state:
        if not (jug1new, jug2new) in node:
            new_node = node.copy()
            new_node.append((jug1new, jug2new))
            returnlist.append(new_node)

    return returnlist

if __name__ == "__main__":
    print("Water jug problem solver")
    do_main()

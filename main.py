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

    #get goal state
    goalstate1 = input("Goal state jug 1:")
    goalstate2 = input("Goal state jug 2:")

    #pack tuples
    startstate = (0, 0)
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

    # setup vars
    returnlist = []
    state = node[-1]
    jug1, jug2 = state


    def checkState(new_state, old_state):
        if new_state != old_state:
            if not new_state in node:
                new_node = node.copy()
                new_node.append(new_state)
                returnlist.append(new_node)

    # possible actions
    # ----------------
    # dump out jug1
    # dump out jug2
    # fill jug1
    # fill jug2
    # jug1 -> jug2
    # jug2 -> jug1

    # possible next states:
    # ---------------------
    # (jug1, 0)
    # (0, jug2)
    # (jug1size, jug2)
    # (jug1, jug2size)
    # (jug1 - min(jug1, jug2size - jug2), jug2 + min(jug1, jug2size - jug2))
    # (jug1 + min(jug2, jug1size - jug1), jug2 - min(jug2, jug1size - jug1))

    slist = [(jug1, 0), (0, jug2), (jug1size, jug2), (jug1, jug2size),
             (jug1 - min(jug1, jug2size - jug2), jug2 + min(jug1, jug2size - jug2)),
             (jug1 + min(jug2, jug1size - jug1), jug2 - min(jug2, jug1size - jug1))]
    for s in slist:
        checkState(s, state)

    return returnlist

if __name__ == "__main__":
    print("Water jug problem solver")
    do_main()

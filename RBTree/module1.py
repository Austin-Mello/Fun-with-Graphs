""" Simple test class for Lab 3 """

from random import randint, shuffle
from mealticket import *
from amello3_Lab4 import *  # FIXME change this to your duckID!


def generateMealTickets(size):
    """ Generates an array of mealtickets based on the integer <size> """
    mealtickets = []
    for i in range(size):
        ticket = MealTicket("Jared's Meal " + str(i))
        ticket.addItem(("Item 1", round(uniform(0, 30), 2)))
        ticket.addItem(("Item 2", round(uniform(0, 30), 2)))
        ticket.addItem(("Item 3", round(uniform(0, 30), 2)))
        mealtickets.append(ticket)

    # randomize the list of tickets
    IDs = {}
    for ticket in mealtickets:
        newID = randint(1, size)
        while newID in IDs:
            newID = randint(1, size)
        IDs[newID] = newID
        ticket.ticketID = newID
    return mealtickets


def main():
    size = 8
    rbt = RedBlackTree()
    tickets = generateMealTickets(size)

    print("=== Testing Binary Search Tree ===")
    print("Test 1: Inserting tickets")
    for ticket in tickets:
        print("Result", str(ticket.ticketID) + ":", rbt.insert(ticket))
        print("In-order:", rbt.traverse("in-order"))
        print("Pre-order:", rbt.traverse("pre-order"))
        print("Post-order:", rbt.traverse("post-order"))
    print()

    print("Test 2: Traversals")

    print("In-order:", rbt.traverse("in-order"))
    print("Pre-order:", rbt.traverse("pre-order"))
    print("Post-order:", rbt.traverse("post-order"))
    print()

    print("Test 3: Deleting tickets")
    # generate a list of random ids of random length
    ids = [i for i in range(1, size + 1)]
    #shuffle(ids)
    # change the below line if you want to delete a certain number of nodes
    length = randint(1, size)
    ids = ids[:length]  # shorten list to random length 1..size
    for i in ids:
        res = rbt.delete(i)
        print("Remove", str(i) + ":", res)
    print()

    print("Test 4: Traversals Revisited")

    print("In-order:", rbt.traverse("in-order"))
    print("Pre-order:", rbt.traverse("pre-order"))
    print("Post-order:", rbt.traverse("post-order"))
    print()

    return


if __name__ == "__main__":
    main()
import copy
import sys

TOTAL_DISKS = 5 

SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """Runs a single game of The Tower of Hanoi."""
    print(
        """THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    """The towers dictionary has keys "A", "B", and "C" and values
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of
    the list is the bottom of the tower. For a game with 5 disks,
    the list [5, 4, 3, 2, 1] represents a completed tower. The blank
    list [] represents a tower of no disks. The list [1, 3] has a
    larger disk on top of a smaller disk and is an invalid
    configuration. The list [3, 1] is allowed since smaller disks
    can go on top of larger ones."""
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True: 
        displayTowers(towers)

        fromTower, toTower = getPlayerMove(towers)

        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)  
            print("You have solved the puzzle! Well done!")
            sys.exit()


def getPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True:  
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to move a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA, or CB.")
            continue  

        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            print("You selected a tower with no disks.")
            continue 
        elif len(towers[toTower]) == 0:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue  
        else:
            return fromTower, toTower


def displayTowers(towers):
    """Display the three towers with their disks."""

    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0) 
            else:
                displayDisk(tower[level]) 
        print()

    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))


def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        # Display the disk:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    main()
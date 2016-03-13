from myFunctions import *

uSet = ""
sets = []
setNames = []

print("Set Notation\nType '?' for help")




def commands():
    print("Set Notation commands")
    printCenter("NOTES\n")
    print("Make sure to put spaces in your commands")
    print("All set names are CAPITALISED")
    print("")
    printCenter("ASSIGNMENT\n")
    print("A = {x, y, z} | Make a new set called 'A' which contains X, Y and Z")

    print()
    printCenter("DISPLAY\n")
    print("A             | Display set A")
    print("P             | Show all sets")
    print("A u B         | A Union B show elements which belong to A OR B")
    print("A n B         | A Intersect B show elements which belong to A AND B")
    print("A'            | A Complement show all elements not in A")

def displaySet():
    print("Type the name of the set you want to display or '*' to display all sets")
    p = input("-> ").upper()
    if p == "*":
        for i in range(len(setNames)):
            print(setNames[i]+" = "+str(sets[i+1]).replace("[", "{").replace("]", "}").replace("'", ""))
    else:
        try:
            print(sets[setNames.index(p)+1])
        except ValueError:
            print("set '"+p+"' does not exist")


def main():
    global sets, setNames
    p = input("'?' for help\n-> ").upper()
    if p == "?":
        commands()
    elif "{" in p and "}" in p:
        setNames.append(p[:p.index(" ")])
        p = p[p.index("{"):p.index("}")].replace("{", "").replace("}", "").replace(" ", "")
        sets.append(p.split(","))
    elif p == "D":
        displaySet()



def makeSet():
    global uSet, sets
    print("Please create a universal set, separating each element by a comma\nElements can be any alphanumeric character")
    print("Type 'd' for default universal set (integers 0-100) and 2 small sets (A and B)")
    uSet = input("-> ").replace(" ", "")
    if uSet == "d" or uSet == "D":
        tl = []
        uSet = ""
        for i in range(101):
            tl.append(str(i))
            if i == 0:
                uSet += str(i)
            else:
                uSet += ", "+str(i)
        sets.append(tl)
        setNames.append("A")
        setNames.append("B")
        sets.append(["1", "2", "4", "6"])
        sets.append(["1", "3", "5", "8"])
    else:
        sets.append(uSet.split(","))
        uSet = uSet.replace(",", ", ")


makeSet()

while True:
    main()
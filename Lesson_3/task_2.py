def Romb(size, iterator=1):
    if iterator <= size:
        print(" "*(size-iterator) + "* "*iterator)
        Romb(size, iterator + 1)
    elif iterator <= 2*size:
        print(" "*(iterator-size) + "* "*(2*size - iterator))
        Romb(size, iterator + 1)
Romb(6)
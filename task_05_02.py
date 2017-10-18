def get_quadrant_number(x, y):

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        raise ValueError

if (__name__=="__main__"):
    print(get_quadrant_number(0, 1))

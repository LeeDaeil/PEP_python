
GLOVE_VAL = []


def add_val(val):
    GLOVE_VAL.append(val)


if __name__ == '__main__':
    for i in range(0,10):
        add_val(i)

    print(GLOVE_VAL)
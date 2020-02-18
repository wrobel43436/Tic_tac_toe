

def build_tree(t):
    for i in range(1, t + 1):
        y = t - i
        x = (2 * i) - 1
        print(" " * y, x * '*')


def build_core(t):
    y = t - 1
    print(' ' * y, '*')
    print(' ' * y, '*')


t = int(input('input: '))

build_tree(t)
build_core(t) 
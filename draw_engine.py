
def create_map():

    map = [[' ' for i in range(1, 12)] for j in range(1, 12)]
    for i in range(11):
        for j in range(11):
            if i == 3:
                map[i][j] = "*"
            elif i == 7:
                map[i][j] = '*'
            elif j == 3:
                map[i][j] = '*'
            elif j == 7:
                map[i][j] = '*'
            else:
                map[i][j] = ' '

    return map


def create_map_two(size_one, size_two):


    map_two = [[' ' for i in range(size_one * 4)] for j in range(size_two * 4)]
    for i in range((size_one * 4) - 1):
        for j in range((size_two * 4) - 1):
            if (i + 1) % 4 == 0 and i != 0:
                map_two[i][j] = '*'
            elif (j + 1) % 4 == 0 and j != 0:
                map_two[i][j] = '*'
            else:
                map_two[i][j] = ' '


    return map_two






def update_map(map, x, y, sign):

    if sign == "circle":

        map[0 + (4 * y)][1 + (4 * x)] = "x"
        map[1 + (4 * y)][0 + (4 * x)] = "x"
        map[1 + (4 * y)][2 + (4 * x)] = 'x'
        map[2 + (4 * y)][1 + (4 * x)] = "x"

    if sign == "cross":

        map[0 + (4 * y)][0 + (4 * x)] = "x"
        map[0 + (4 * y)][2 + (4 * x)] = "x"
        map[2 + (4 * y)][2 + (4 * x)] = "x"
        map[2 + (4 * y)][0 + (4 * x)] = "x"
        map[1 + (4 * y)][1 + (4 * x)] = "x"



    








if __name__ == "__main__":

    #map = create_map()
    #update_map(map, 1, 2, "cross")
    #update_map(map, 2, 2, "circle")
    #update_map(map, 0, 0, "cross")
    #for lists in map:
        #print(lists)

    #map = [[' ' for i in range(3)] for j in range(3)]

    #list = [[5, 4, 3, 2],[4, 3, 2, 1]]

    #print(len(list[0]))

    #print(len(list))
    create_map_two(2, 2)

    print('\n'.join(map(str,  create_map_two(4, 4))))

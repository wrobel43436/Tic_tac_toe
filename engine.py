class Validator:

    def __init__(self, map, x, y):

        self.map = map
        self.x = x
        self.y = y


    def verify_horizontally(self, map, x, y):
        flag = False
        for i in range(x):
            for j in range(y - 1):
                if map[i][j] == ' ':
                    flag = False
                    break
                if map[i][j] == map[i][j + 1]:
                    flag = True
                else:
                    flag = False
            if flag == True:
                return True
        return False


    def verify_vertically(self, map, x, y):
        flag = False
        for j in range(y):
            for i in range(x - 1):

                if map[i][j] == ' ':
                    flag = False
                    break
                if map[i][j] == map[i + 1][j]:
                    flag = True
                else:
                    flag = False
            if flag == True:
                return True
        return False

    def verify_diagonal_one(self, map, x, y):
        valid_counter = 0
        for i in range(y):
            for j in range(x):
               if i == j:
                   if map[i][j] != ' ':
                       valid_counter += 1
               if valid_counter == x:
                    return True
        return False

    def verify_diagonal_two(self, map, x, y):
        valid_counter_two = 0
        for i in range(y - 1):
            for j in range(x - 1, 0, -1):
                if map[i][j] == map[i + 1][j - 1] and map[i][j] != ' ':
                    valid_counter_two +=1
                if valid_counter_two == x - 1:
                    return True
        return False

    def validate(self):

        x = len(map)
        y = len(map)


        if self.verify_horizontally(map, x, y):
            print('horizontally true')
            return True

        elif self.verify_vertically(map, x, y):
            print("vertically true)")
            return True

        elif self.verify_diagonal_one(map, x ,y):
            print('diagonal one true')
            return True

        elif self.verify_diagonal_two(map, x, y):
            print("diagonal two true")
            return True

        else:
            return False



if __name__ == "__main__":


    map = [[' ' for i in range(3)] for j in range(3)]

    validator_one = Validator(map, 3, 3)

    map[0][2] = ' '
    map[0][1] = ' '
    map[0][0] = 'o'
    map[1][1] = 'o'
    map[2][0] = ' '
    map[2][2] = 'o'
    for list in map:
        print(list)
    print(validator_one.validate())





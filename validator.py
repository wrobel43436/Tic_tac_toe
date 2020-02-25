class Validator:

    def __init__(self, map):

        self.map = map
        self.x = len(map[0])
        self.y = len(map)

    def verify_horizontally(self):
        valid_counter_four = 0
        flag = False
        for i in range(self.y):
            for j in range(self.x - 1):
                if self.map[i][j] == ' ':
                    flag = False
                    break
                if self.map[i][j] == self.map[i][j + 1]:
                    valid_counter_four += 1
                if valid_counter_four == self.x:
                    flag = True
                else:
                    flag = False
            if flag == True:
                return True
        return False


    def verify_vertically(self):
        print(self.x, self.y)
        valid_counter_three = 0
        flag = False
        for j in range(self.x):
            for i in range(self.y - 1):

                if self.map[i][j] == ' ':
                    flag = False
                    break
                if self.map[i][j] == self.map[i + 1][j]:
                    valid_counter_three += 1
                if valid_counter_three == self.y:
                    flag = True
                else:
                    flag = False
            if flag == True:
                return True
        return False

    def verify_diagonal_one(self):
        valid_counter = 0
        for i in range(self.y - 1):
            for j in range(self.x - 1):
               if i == j:
                   if self.map[i][j] == self.map[i + 1][j + 1] and self.map[i][j] != ' ':
                       valid_counter += 1
               if valid_counter == self.x:
                    return True
        return False

    def verify_diagonal_two(self):
        valid_counter_two = 0
        for i in range(self.y - 1):
            for j in range(self.x - 1, 0, -1):
                if self.map[i][j] == self.map[i + 1][j - 1] and self.map[i][j] != ' ':
                    valid_counter_two +=1
                if valid_counter_two == self.x - 1:
                    return True
        return False

    def validate(self):




        if self.verify_horizontally():
            print('horizontally true')
            return True

        elif self.verify_vertically():
            print("vertically true")
            return True

        elif self.verify_diagonal_one():
            print('diagonal one true')
            return True

        elif self.verify_diagonal_two():
            print("diagonal two true")
            return True

        else:
            return False









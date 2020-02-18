
line = ''
list_one = [1,2,3,4,5]
print(list_one[3])
list_two = [[1,2,3], [4,5,6], [7,8,9]]
print(list_two[1][1])
print(list_two[2][2])
print(list_two[0][0])


for i in range(5):

    for j in range(5):

        if i == 2 and 0 <= j <= 4:
            line += '.'
        elif 0 <= i <= 4 and j == 2:
            line += '.'
        elif 0 < i < 4 and 0 < j < 4:
            line += ' '
        else:
            line += 'x'

    print(line)
    line = ''




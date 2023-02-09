def compareOrder(left, right):
    for i in range(len(right) + 1):
        if len(left) == i and len(right) == i:
            return None
        if len(left) != i and len(right) == i:
            return False
        if len(left) == i and len(right) != i:
            return True
        if type(left[i]) == list and type(right[i]) == list:
            order = compareOrder(left[i], right[i])
            if order == None:
                continue
            return order
        if type(right[i]) == list:
            leftList = [left[i]]
            order = compareOrder(leftList, right[i])
            if order == None:
                continue
            return order
        if type(left[i]) == list:
            rightList = [right[i]]
            order = compareOrder(left[i], rightList)
            if order == None:
                continue
            return order
        if left[i] > right[i]:
            return False
        if left[i] < right[i]:
            return True

with open("data.txt", "r") as f:
    data = f.read()
    left = 0
    right = 0
    indices = 0
    indicesSum = 0
    for i in data.split("\n"):
        i.strip('\n\'')
        if i == "":
            left = 0
            right = 0
            continue
        i = eval(i)
        if left == 0:
            left = i
            continue
        indices += 1
        correctOrder = True
        right = i
        correctOrder = compareOrder(left, right)
        if correctOrder or correctOrder == None:
            print(indices)
            indicesSum += indices
print(indicesSum)
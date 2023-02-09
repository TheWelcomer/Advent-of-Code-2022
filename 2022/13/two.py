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
    twoDiv = [[2]]
    sixDiv = [[6]]
    twoIndices = 0
    sixIndices = 0
    for i in data.split("\n"):
        i.strip('\n\'')
        if i == "":
            continue
        i = eval(i)
        compare = compareOrder(i, twoDiv)
        if compare or compare == None:
            twoIndices += 1
    for i in data.split("\n"):
        i.strip('\n\'')
        if i == "":
            continue
        i = eval(i)
        compare = compareOrder(i, sixDiv)
        if compare or compare == None:
            sixIndices += 1
print(twoIndices, sixIndices)
print((twoIndices + 1) * (sixIndices + 2))
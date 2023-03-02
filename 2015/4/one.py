import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

with open("data.txt", "r") as f:
    data = f.read()
    hashDecimal = 0
    while True:
        hash = computeMD5hash(data + str(hashDecimal))[:5]
        if hash == "00000":
            break
        hashDecimal += 1
    print(hashDecimal)

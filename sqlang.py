''' library that creates the basis for the Square Language '''
''' operates on capital A-Z letters '''
''' by Karl Zander '''

def nums_to_letters(n):
    ldict = {}
    for x in range(26):
        ldict[x] = chr(x + 65)
    nlist = list(str(n))
    for x in range(len(nlist)):
        nlist[x] = int(nlist[x])
    sqr = []
    while len(nlist) > 0:
        if len(nlist) >= 2:
            tmp = nlist[:2]
            l1 = str(tmp[0])
            l2 = str(tmp[1])
            num = int(str(l1 + l2))
            if num >= 0 and num <= 25:
                letter = chr(num + 65)
                sqr.append(letter)
                for x in range(2):
                    nlist.pop(0)
            else:
                tmp = nlist[:1]
                num = int(tmp[0])
                letter = chr(num + 65)
                sqr.append(letter)
                nlist.pop(0)
        elif len(nlist) == 1:
            tmp = nlist[:1]
            num = int(tmp[0])
            letter = chr(num + 65)
            sqr.append(letter)
            nlist.pop(0)
    return "".join(sqr)

def letters_to_nums(string):
    nstring = ""
    for x in range(len(string)):
        num = ord(string[x]) - 65
        nstring += str(num)
    return int(nstring)

def sqr_string(string):
    n = letters_to_nums(string)
    x = n * n
    s = nums_to_letters(x)
    return s

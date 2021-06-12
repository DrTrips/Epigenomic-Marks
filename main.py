f = open("1.txt", 'r')
f1 = open("out.txt", 'w')
num_of_tests = int(f.readline())

for _i in range(num_of_tests):
    d = {}
    marks = []
    index = 1
    codes = []
    cur_seq = ""
    res = ""
    inp = f.readline()
    space = inp.find(" ")
    n = int(inp[:space])
    end = inp.find('\n')
    length = int(inp[space + 1: end])
    for _ in range(n):
        marks.append(f.readline().strip('\n'))
    for i in range(length):
        for elem in marks:
            cur_seq = cur_seq + elem[i]
        if not d:
            d[index] = cur_seq
            codes.append(index)
            index += 1
            cur_seq = ""
        else:
            if cur_seq not in d.values():
                d[index] = cur_seq
                codes.append(index)
                index += 1
                cur_seq = ""
            else:
                for key, value in d.items():
                    if cur_seq == value:
                        codes.append(key)
                        cur_seq = ""
    f1.write(str(index - 1) + '\n')
    for elem in codes:
        res += str(elem) + " "
    f1.write(res[:-1] + '\n')
    del codes
f.close()

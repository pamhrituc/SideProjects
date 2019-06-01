def readFile(fileName):
    f = open(fileName, 'r')
    n0 = f.readline()
    n1 = n0.split("=")
    n = int(n1[1].split('\n')[0])
    #print(n)
    ciii = []
    for i in range(0, n):
        f.readline()
        s0 = f.readline()
        #print(s0)
        s1 = s0.split("=")
        s = int(s1[1].split('\n')[0])
        #print(s)
        p0 = f.readline()
        p1 = p0.split("=")
        p = int(p1[1].split('\n')[0])
        #print(p)
        d0 = f.readline()
        d1 = d0.split("=")
        d = int(d1[1].split('\n')[0])
        #print(d)
        tp0 = f.readline()
        tp1 = tp0.split("=")
        tp = int(tp1[1].split('\n')[0].split('%')[0])/100
        #print(tp)
        c0 = f.readline()
        c1 = c0.split("=")
        c = c1[1].split('\n')[0].split(' ')
        #print(c)
        ci = []
        for i in c:
            ci.append(int(i))
        #print(ci)
        cii = profit(s, p, d, tp, ci)
        ciii.append(cii)
    return ciii


def profit(s, p, d, tp, ci):
    cj = []
    x1 = int(p * tp)
    cj.append(x1)
    x = 0 - int(tp * (p + x1))
    cj.append(x)
    #print(cj)
    while (abs(x) - abs(x1) > 0):
        x = 0 - int(tp * (p + abs(x1) - abs(x)))
        #print(x)
        #y = input()
        if x != 0:
            cj.append(x)
    print(cj)

    n = len(cj)
    cii = []
    currentPoz = 0
    k = 0

    ciS = sorted(ci)
    maxCi = ciS[d - n + 1:]
    for i in range(0, d):
        if k < len(cj):
            if s < ci[i] * cj[k]:
                cii.append(0)
            elif ci[i] in maxCi:
                cii.append(cj[k])
                k += 1
            elif s > ci[i] * cj[k]:
                cii.append(abs(cj[k]))
                k += 1
            else:
                cii.append(0)
        else:
            cii.append(0)

    '''
    for i in range(0, d):
        if s < ci[i] * cj[0]:
            cii.append(0)
        else:
            cii.append(cj[0])
            currentPoz = i
            break
    if len(cii) == d:
        return cii

    k = 1

    #print(maxCi)

    for i in range(currentPoz + 1, d):
        if ci[i] in maxCi:
            if k < len(cj):
                cii.append(cj[k])
                k += 1
            else:
                cii.append(0)
        else:
            cii.append(0)
    '''
    print(cii)
    return cii
    '''
    diff = 0
    min = ci[0]
    for i in range(1, n):
        #if min > ci[i]:
            #min = ci[i]
        if diff < ci[i] - min:
            diff = ci[i] - min
            iM = i
    print(str(diff) + " " + str(iM))
    '''

def writeFile(fileName, x):
    f = open(fileName, 'a')
    for i in x:
        for j in i:
            f.write(str(j) + " ")
        f.write("\n")
    f.close()

def main():
    x = readFile("input_v0.in")
    #x = maxProfit(a)
    writeFile("output.out", x)

main()

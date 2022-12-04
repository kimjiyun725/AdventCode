def p1():
    tsum = 0
    with open('data/d3.txt') as f:
        lines = f.readlines()
        for line in lines:
            d = {}
            half1 = line[:len(line)//2]
            half2 = line[len(line)//2:]
            
            for i in range(len(line)//2):
                if half1[i] not in d:
                    d[half1[i]] = {1:True,  2:False}
                else:
                    d[half1[i]][1] = True
                
                if half2[i] not in d:
                    d[half2[i]] = {1:False,  2:True}
                else:
                    d[half2[i]][2] = True

            for row in d:
                if d[row][1] == True and d[row][2] == True:
                    if ord(row) - 96 >= 1:
                        tsum += (ord(row) - 96)
                    else:
                        tsum += (ord(row) - 64 + 26)
                    break
                
    return tsum

def p2():
    tsum = 0
    with open('data/d3.txt') as f:
        lines = f.readlines()
        d = {}
        for i in range(len(lines)):
            if i % 3 == 0:
                d.clear()
            
            line = lines[i]
            for j in range(len(line)-1):
                if line[j] not in d:
                    d[line[j]] = [False, False, False]
                
                if line[j] in d:
                    d[line[j]][i % 3] = True
                    
            if (i + 1) % 3 == 0:
                for row in d:
                    if d[row][0] != True:
                        continue
                    if d[row][1] != True:
                        continue
                    if d[row][2] != True:
                        continue
                    
                    if ord(row) - 96 >= 1:
                        tsum += (ord(row) - 96)
                    else:
                        tsum += (ord(row) - 64 + 26)
                    break

    return tsum          

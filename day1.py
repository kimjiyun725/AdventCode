def CalorieCounting():
    most_cals = 0
    with open('data/d1q1.txt') as f:
        lines = f.readlines()
        cals = 0
        for line in lines:
            if line == '\n':
                if most_cals < cals:
                    most_cals = cals
                cals = 0
                continue
            
            cals += int(line[:-1])
    
    return most_cals

def TopThree():
    top_three = [0, 0, 0]
    with open('data/d1q1.txt') as f:
        lines = f.readlines()
        cals = 0
        for line in lines:
            if line == '\n':
                if cals >= top_three[2]:
                    top_three.pop(0)
                    top_three.append(cals)
                elif cals >= top_three[1]:
                    top_three[0] = top_three[1]
                    top_three[1] = cals
                elif cals >= top_three[0]:
                    top_three[0] = cals
                    
                cals = 0
                continue
            
            cals += int(line[:-1])
            
    return top_three[0] + top_three[1] + top_three[2]
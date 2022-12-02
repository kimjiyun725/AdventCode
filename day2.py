def RPS():
    total_score = 0
    win =  {"A": "Y", "B": "Z", "C": "X"}
    draw = {"A": "X", "B": "Y", "C": "Z"}
    rps_vals = {"X": 1, "Y": 2, "Z": 3}
    with open('data/d2.txt') as f:
        lines = f.readlines()
        for line in lines:
            if win[line[0]] == line[2]:
                total_score += 6
            elif draw[line[0]] == line[2]:
                total_score += 3
                
            total_score += rps_vals[line[2]]
    
    return total_score

def PartTwo():
    total_score = 0
    win = {"A": 2, "B": 3, "C": 1}
    draw = {"A": 1, "B": 2, "C": 3}
    loss = {"A": 3, "B": 1, "C": 2}
    with open('data/d2.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line[2] == "Y":
                total_score += 3 + draw[line[0]]
            elif line[2] == "Z":
                total_score += 6 + win[line[0]]
            else:
                total_score += loss[line[0]]
                
    return total_score
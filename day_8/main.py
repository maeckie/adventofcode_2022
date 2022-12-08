from functools import reduce
matrix = []
for line in open('./day_8/input.txt').read().splitlines():
    row = []
    for c in line:
        row.append(int(c))
    matrix.append(row)


def validate(x,y):
    val = matrix[y][x]
    left = matrix[y][:x]
    right = matrix[y][x+1:]
    column = [row[x] for row in matrix]
    top = column[:y]
    bottom = column[y+1:]
    if (x == 0 or x == len(matrix[y])) or (y == 0 or y == len(matrix)):
        return True
    
    if (all(x < val for x in left)) or (all(x < val for x in right)):
        return True
    
    if (all(x < val for x in top)) or (all(x < val for x in bottom)):
        return True

def validate2(x,y):
    val = matrix[y][x]
    left = matrix[y][:x]
    right = matrix[y][x+1:]
    
    column = [row[x] for row in matrix]    
    top = column[:y]
    bottom = column[y+1:]
    
    if len(left) > 0: 
        left.reverse()
    if len(top) > 0: 
        top.reverse()

    directions = [left, right, top, bottom]
    scores = []
    for direc in directions:
        score = 0 
        for i in direc:
            score += 1
            if i >= val:
                break
        scores.append(score)
    
    return reduce(lambda x, y: x * y, scores)
    

        

visible = 0
max_score = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if validate(x,y):
            visible += 1
        score = validate2(x,y)
        max_score = score if score > max_score else max_score
            
print(visible)
print(max_score)

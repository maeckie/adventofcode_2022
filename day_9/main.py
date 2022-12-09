import pprint
steps=open('./day_9/input.txt').read().splitlines()
h = [0,0]
t = [0,0]
snake = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

direction = {'R': [1,0], 'L': [-1,0], 'U': [0,1], 'D': [0,-1]}
visited = []
visited.append((0,0))
snake_visit = []
snake_visit.append((0,0))

def move_tail(dir):
    
    if abs(h[0]- (t[0])) > 1 or abs(h[1] - t[1]) > 1:
        if h[0] == t[0] or h[1] == t[1]:
            t[0] = t[0]+ dir[0]
            t[1] = t[1]+ dir[1]
        else:
            if h[0] > t[0]:
                t[0]+=1
            else:
                t[0]-=1

            if h[1] > t[1]:
                t[1]+=1
            else:
                t[1]-=1

        visited.append((t[0],t[1]))

def move_tail2(dir, head, me):
    
    if abs(head[0]- (me[0])) > 1 or abs(head[1] - me[1]) > 1:
        if head[0] > me[0]:
            me[0]+=1
        elif head[0] < me[0]:
            me[0]-=1

        if head[1] > me[1]:
            me[1]+=1
        elif head[1] < me[1]:
            me[1]-=1

    return (me[0],me[1])




for step in steps:
    d,r = step.split(' ')
    dir = direction[d]

    for i in range(int(r)):
        h[0] = h[0]+ dir[0]
        h[1] = h[1]+ dir[1]   

        move_tail(dir)
        snake[0][0] += dir[0]
        snake[0][1] += dir[1]
        for j in range(1,len(snake)):
            p = move_tail2(dir, snake[j-1],snake[j])
            snake[j][0] = p[0]
            snake[j][1] = p[1]
        snake_visit.append(p)

print(len(set(visited)))
print(len(set(snake_visit)))

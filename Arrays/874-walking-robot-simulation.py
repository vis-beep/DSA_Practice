class Solution(object):
def robotSim(self, commands, obstacles):
# Directions: North, East, South, West
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0

```
    x, y = 0, 0
    max_dist = 0
    
    # Convert obstacles to set
    obstacle_set = set(map(tuple, obstacles))
    
    for cmd in commands:
        if cmd == -1:
            d = (d + 1) % 4
        elif cmd == -2:
            d = (d + 3) % 4
        else:
            dx, dy = dirs[d]
            
            for _ in range(cmd):
                nx = x + dx
                ny = y + dy
                
                if (nx, ny) in obstacle_set:
                    break
                
                x, y = nx, ny
                max_dist = max(max_dist, x*x + y*y)
    
    return max_dist
```

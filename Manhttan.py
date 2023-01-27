from collections import deque

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(points, start):
    distances = []
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        current = queue.popleft()
        for point in points:
            if point not in visited:
                distance = manhattan_distance(current, point)
                distances.append(distance)
                visited.add(point)
                queue.append(point)
    return distances

points = [(1, 2), (2, 3), (3, 4), (4, 5)]
start = points[0]
distances = bfs(points, start)

print("Sum of Manhattan distances:", sum(distances))

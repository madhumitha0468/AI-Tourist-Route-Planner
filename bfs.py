from collections import deque
from places import places


def bfs_route(start, destination):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == destination:
            return path

        if current not in visited:
            visited.add(current)

            for neighbour in places[current]["nearby"]:
                if neighbour not in visited:
                    new_path = path + [neighbour]
                    queue.append(new_path)

    return None
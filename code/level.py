import random

def generate_level(width, height)
    level = [[0] * width for _ in range(height)]

    def carve_room(x, y, w, h):
        for i in range(x, x + w):
            for j in range(y, y + h):
                level[j][i] = 1
    def carve_corridor(x1, y1, x2, y2):
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                level[i][x1] = 1
        else:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                level[y1][i] = 1

    def generate_rooms(width, height):
        rooms = []
        for _ in range(10):
            w = random.randint(5, 15)
            h = random.randint(5,15)
            x = random.randint(0, width - w - 1)
            y = random.randint(0, height - h - 1)
            rooms.append((x, y, w, h))
        return rooms

    def connect_rooms(rooms):
        connections = []
        for i in range(len(rooms)):
            for j in range(i+1, len(rooms)):
                (x1, y2, w1, h1) = rooms[i]
                (x2, y2, w2, h2) = rooms[j]
                if x1 < x2 and x1 + w1 > x2:
                    if random.randint(0, 1):
                        connections.append((x1, y1 + h1//2, x2, y2 + h2//2))
                    else:
                        connections.append((x2 + w2 + h2//2, x1, y1 + h1//2))
                elif y1 < y2 and y1 + h1 > y2:
                    if random.randint(0, 1):
                        connections.append((x1 + w1//2, y1 + h1, x2 + w2//2, y2))
                    else:
                        connections.append((x2 + w2//2, y2, x1 + w1//2, y1))
        return connections

    rooms = generate_rooms(width, height)
    for (x, y, w, h) in rooms:
        carve_room(x, y, w, h)

    connections = connect_rooms(rooms)
    for (x1, y1, x2, y2) in connections:
        carve_corridor(x1, y1, x2, y2)

    return level


level = generate_level(50, 50)
for row in level:
    print(row)
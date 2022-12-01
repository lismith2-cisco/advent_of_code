from datetime import datetime

startTime = datetime.now()

f = open("2021_5_vents_input.txt")

lines = (line.strip() for line in f)
line_ends = (line.split(' -> ') for line in lines if line)
coordinates = ([int(coordinate)
                for coordinate in x.split(',') + y.split(',')]
               for x, y in line_ends)


class DangerPoints:
    def __init__(self):
        self.points_with_a_line = set()
        self.points_with_multiple_lines = set()

    def add(self, point):
        if point in self.points_with_a_line:
            self.points_with_multiple_lines.add(point)
        else:
            self.points_with_a_line.add(point)


danger_points = DangerPoints()

for x1, y1, x2, y2 in coordinates:
    # vertical line
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            danger_points.add((x1, y))
    # horizontal line
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            danger_points.add((x, y1))
    # positive diagonal
    elif x1 - x2 == y1 - y2:
        for x, y in zip(range(min(x1, x2), max(x1, x2)+1), range(min(y1, y2), max(y1, y2)+1)):
            danger_points.add((x, y))
    # negative diagonal
    else:
        for x, y in zip(range(min(x1, x2), max(x1, x2)+1), range(max(y1, y2), min(y1, y2)-1, -1)):
            danger_points.add((x, y))


print(len(danger_points.points_with_multiple_lines))
print(datetime.now() - startTime)

import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    point1 = (1, 2)
    point2 = (6, 6)
    print('The distance between the two points:', distance(point1, point2))

if __name__ == "__main__":
    main()
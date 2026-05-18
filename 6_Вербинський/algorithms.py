import random
from shapely.geometry import Point, Polygon

def gauss_area(polygon: Polygon) -> float:
    x, y = polygon.exterior.xy
    n = len(x) - 1 
    area = 0.0
    for i in range(n):
        area += (x[i] * y[i + 1]) - (x[i + 1] * y[i])
    return abs(area) / 2.0

def monte_carlo_area(polygon: Polygon, num_points: int) -> float:
    minx, miny, maxx, maxy = polygon.bounds
    box_area = (maxx - minx) * (maxy - miny)
    points_inside = 0
    for _ in range(num_points):
        pt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(pt):
            points_inside += 1
    return box_area * (points_inside / num_points)
import random

from point import Point

# Create 10 random points and add them to the Point class `points` ClassVar list
for _ in range(4):
    Point(random.uniform(-100, 100), random.uniform(-100, 100))  # noqa: S311


# Create all possible combinations of points
combinations = []

for idx, point in enumerate(Point.points):
    if len(Point.points) == idx:
        break
    combinations.extend([(point, i) for i in Point.points[idx + 1 :]])


# Print possible combinations
print("Possible combinations:")
for combination in combinations:
    print(*combination)


# Variables to store minimum and maximum distances and corresponding point pairs
min_distance = float("inf")
max_distance = float("-inf")

min_distant = ()
max_distant = ()


# Calculate the distances between all combinations of points
for combination in combinations:
    dist = Point.distance_between_points(*combination)
    if dist > max_distance:
        max_distance = dist
        max_distant = combination
    if dist < min_distance:
        min_distance = dist
        min_distant = combination


# Print the maximum and minimum distant point pairs
print("Max distant points:", *max_distant, f"distance: {max_distance}")
print("Min distant points:", *min_distant, f"distance: {min_distance}")

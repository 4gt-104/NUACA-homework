import random

from point import Point

# Create 10 random points and add them to the Point class `points` ClassVar list
for _ in range(10):
    Point(random.uniform(-100, 100), random.uniform(-100, 100))  # noqa: S311

# Ask the user for the minimum distance
min_distance = float(input("Min distance:"))


# Iterate over all points and print distances greater than the minimum distance
for point in Point.points:
    if (distance := point.distnance_from_0) > min_distance:
        print(f"{distance=} for point with coordinates: {point}")

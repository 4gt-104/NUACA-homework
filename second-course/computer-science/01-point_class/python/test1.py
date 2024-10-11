import random

from point import Point

# Generate random coordinates for point1
point1 = Point(random.uniform(-100, 100), random.uniform(-100, 100))  # noqa: S311

print(f"{point1.x_coord=}")
print(f"{point1.y_coord=}")
print(f"{point1.coordinates=}")


# Generate new random coordinates and set them for point1
print(
    f"setting coordinates to {(new_coord := (random.uniform(-100, 100), random.uniform(-100, 100)))}",  # noqa: S311
)
point1.coordinates = new_coord
print("coordinates are: ", point1)


# Display the sector of point1
print(f"{point1.sector=}")


# Distance from origin
print(f"{point1.distnance_from_0=}")


# Move on X axis
print(f"Moving on X axis by {(move_by_x := random.uniform(-100, 100))}")  # noqa: S311
point1.move_on_x(move_by_x)


# Move on Y axis
print(f"Moving on Y axis by {(move_by_y := random.uniform(-100, 100))}")  # noqa: S311
point1.move_on_y(move_by_y)


# Print final coordinates
print("coordinates are: ", point1)


# Create point2 and calculate the distance between point1 and point2
point2 = Point(random.uniform(-100, 100), random.uniform(-100, 100))  # noqa: S311
print(f"{Point.distance_between_points(point1, point2)=}")


# Check equality
print("point1 eq to point2:", point1 == point2)
print("point1 not eq to point2:", point1 != point2)


# Test __str__ dunder method
print(point1)

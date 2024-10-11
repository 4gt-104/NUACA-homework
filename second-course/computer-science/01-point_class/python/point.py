from __future__ import annotations

from math import sqrt
from typing import ClassVar, Literal


class Point:
    points: ClassVar[list[Point]] = []

    def __init__(self, x_coord: float = 0, y_coord: float = 0) -> None:
        self._x_coord = x_coord
        self._y_coord = y_coord
        print(f"Point created, coordinates: {self.coordinates}")
        Point.points.append(self)

    def __del__(self) -> None:
        Point.points.remove(self)
        print(f"Point with '{self.coordinates}' deleted.")

    def __str__(self) -> str:
        return str(self.coordinates)

    def __eq__(self, other: Point) -> bool:
        return self.coordinates == other.coordinates

    def copy(self) -> Point:
        return Point(*self.coordinates)

    @property
    def x_coord(self) -> float:
        return self._x_coord

    @x_coord.setter
    def x_coord(self, value: float) -> None:
        self._x_coord = value

    def move_on_x(self, value: float) -> None:
        self._x_coord += value

    @property
    def y_coord(self) -> float:
        return self._y_coord

    @y_coord.setter
    def y_coord(self, value: float) -> None:
        self._y_coord = value

    def move_on_y(self, value: float) -> None:
        self._y_coord += value

    @property
    def coordinates(self) -> tuple[float, float]:
        return self.x_coord, self.y_coord

    @coordinates.setter
    def coordinates(self, coord: tuple[float, float]) -> None:
        self.x_coord, self.y_coord = coord

    @staticmethod
    def distance_between_points(pt1: Point, pt2: Point) -> float:
        x_dist = abs(pt1.x_coord - pt2.x_coord)
        y_dist = abs(pt1.y_coord - pt2.y_coord)
        return sqrt(x_dist**2 + y_dist**2)

    @property
    def sector(
        self,
    ) -> Literal[
        "Point is on both Axis",
        "Point is on X Axis",
        "Point is on Y Axis",
        "Point is in First Sector",
        "Point is in Second Sector",
        "Point is in Third Sector",
        "Point is in Fourth Sector",
        "ERROR",
    ]:
        match self.coordinates:
            case x_coord, y_coord if x_coord == 0 and y_coord == 0:
                return "Point is on both Axis"
            case x_coord, _ if x_coord == 0:
                return "Point is on X Axis"
            case _, y_coord if y_coord == 0:
                return "Point is on Y Axis"
            case x_coord, y_coord if x_coord > 0 and y_coord > 0:
                return "Point is in First Sector"
            case x_coord, y_coord if x_coord < 0 and y_coord > 0:
                return "Point is in Second Sector"
            case x_coord, y_coord if x_coord < 0 and y_coord < 0:
                return "Point is in Third Sector"
            case x_coord, y_coord if x_coord > 0 and y_coord < 0:
                return "Point is in Fourth Sector"
            case _:
                return "ERROR"

    @property
    def distnance_from_0(
        self,
    ) -> float:
        return sqrt(self.x_coord**2 + self.y_coord**2)

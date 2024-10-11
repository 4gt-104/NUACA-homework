#include <iostream>
#include <cstdlib>
#include <ctime>
#include "point.hpp"

int main() {
    // Initialize random seed
    std::srand(std::time(0));

    // Generate random coordinates for point1
    float x1 = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    float y1 = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    Point point1(x1, y1);

    std::cout << "point1.x_coord = " << point1.get_x() << std::endl;
    std::cout << "point1.y_coord = " << point1.get_y() << std::endl;
    std::cout << "point1.coordinates = (" << point1.get_coordinates().first << ", " 
              << point1.get_coordinates().second << ")\n";

    // Generate new random coordinates and set them for point1
    float new_x = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    float new_y = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    std::cout << "Setting coordinates to (" << new_x << ", " << new_y << ")\n";
    point1.set_coordinates(new_x, new_y);
    std::cout << "coordinates are: (" << point1.get_x() << ", " << point1.get_y() << ")\n";

    // Display the sector of point1
    std::cout << "point1.sector = " << point1.sector() << std::endl;

    // Distance from origin
    std::cout << "point1.distnance_from_0 = " << point1.distance_from_0() << std::endl;

    // Move on X axis
    float move_by_x = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    std::cout << "Moving on X axis by " << move_by_x << std::endl;
    point1.move_on_x(move_by_x);

    // Move on Y axis
    float move_by_y = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    std::cout << "Moving on Y axis by " << move_by_y << std::endl;
    point1.move_on_y(move_by_y);

    // Print final coordinates
    std::cout << "coordinates are: (" << point1.get_x() << ", " << point1.get_y() << ")\n";

    // Create point2 and calculate the distance between point1 and point2
    float x2 = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    float y2 = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
    Point point2(x2, y2);
    std::cout << "Distance between point1 and point2 = " 
              << Point::distance_between_points(point1, point2) << std::endl;

    // Check equality
    std::cout << "point1 eq to point2: " << (point1 == point2) << std::endl;
    std::cout << "point1 not eq to point2: " << !(point1 == point2) << std::endl;

    // Test out operator
    std::cout << point2 << " " << point1;

    return 0;
}

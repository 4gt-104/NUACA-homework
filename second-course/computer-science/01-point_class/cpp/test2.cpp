#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "point.hpp"

int main() {
    // Initialize random seed
    std::srand(std::time(0));

    // Create 10 random points and add them to the Point class static list
    for (int i = 0; i < 10; ++i) {
        float x = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
        float y = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
        new Point(x, y);  // Dynamically create and store the point
    }

    // Ask the user for the minimum distance
    float min_distance;
    std::cout << "Min distance: ";
    std::cin >> min_distance;

    // Iterate over all points and print distances greater than the minimum distance
    for (const Point& point : Point::points) {
        float distance = point->distance_from_0();
        if (distance > min_distance) {
            std::cout << "distance = " << distance 
                      << " for point with coordinates: (" 
                      << point->get_x() << ", " << point->get_y() << ")\n";
        }
    }

    return 0;
}

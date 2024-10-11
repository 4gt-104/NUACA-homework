#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <limits>
#include <utility>
#include "point.hpp"

int main() {
    // Initialize random seed
    std::srand(std::time(0));

    // Create 4 random points and add them to the Point class static list
    for (int i = 0; i < 4; ++i) {
        float x = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
        float y = (static_cast<float>(std::rand()) / RAND_MAX) * 200 - 100;
        new Point(x, y);  // Dynamically create and store the point
    }

    std::vector<std::pair<Point*, Point*> > combinations;

    // Create all possible combinations of points
    for (size_t i = 0; i < Point::points.size(); ++i) {
        for (size_t j = i + 1; j < Point::points.size(); ++j) {
            combinations.push_back(std::make_pair(Point::points[i], Point::points[j]));
        }
    }

    // Print possible combinations
    std::cout << "Possible combinations:\n";
    for (const auto& combination : combinations) {
        std::cout << "(" << combination.first->get_x() << ", " << combination.first->get_y() << ") and "
                  << "(" << combination.second->get_x() << ", " << combination.second->get_y() << ")\n";
    }

    // Variables to store minimum and maximum distances and corresponding point pairs
    float min_distance = std::numeric_limits<float>::infinity();
    float max_distance = -std::numeric_limits<float>::infinity();

    std::pair<Point*, Point*> min_distant;
    std::pair<Point*, Point*> max_distant;

    // Calculate the distances between all combinations of points
    for (const auto& combination : combinations) {
        float dist = Point::distance_between_points(*combination.first, *combination.second);
        if (dist > max_distance) {
            max_distance = dist;
            max_distant = combination;
        }
        if (dist < min_distance) {
            min_distance = dist;
            min_distant = combination;
        }
    }

    // Print the maximum and minimum distant point pairs
    std::cout << "Max distant points: (" << max_distant.first->get_x() << ", " << max_distant.first->get_y() << ") and ("
              << max_distant.second->get_x() << ", " << max_distant.second->get_y() << "), distance: " 
              << max_distance << std::endl;

    std::cout << "Min distant points: (" << min_distant.first->get_x() << ", " << min_distant.first->get_y() << ") and ("
              << min_distant.second->get_x() << ", " << min_distant.second->get_y() << "), distance: " 
              << min_distance << std::endl;

    return 0;
}

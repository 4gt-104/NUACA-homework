#include <iostream>
#include <cmath>
#include <vector>
#include <string>

class Point 
{
private:
    float x_coord;
    float y_coord;

public:
    // A class-level list to hold all points
    static std::vector<Point*> points;

    // Constructor
    Point(float x = 0, float y = 0) : x_coord(x), y_coord(y) {
        points.push_back(this);
        std::cout << "Point created, coordinates: (" << x_coord << ", " << y_coord << ")\n";
    }

    // Destructor
    ~Point() {
        points.erase(std::remove(points.begin(), points.end(), this), points.end());
        std::cout << "Point with coordinates (" << x_coord << ", " << y_coord << ") deleted.\n";
    }

    // Copy constructor
    Point(const Point& oth)
    {
        x_coord = oth.x_coord;
        y_coord = oth.y_coord;

        points.push_back(this);
    };

    // Getters and setters for x_coord
    float get_x() const { return x_coord; }
    void set_x(const float value)  { x_coord = value; }
    void move_on_x(const float value) { x_coord += value; }

    // Getters and setters for y_coord
    float get_y() const { return y_coord; }
    void set_y(const float value) { y_coord = value; }
    void move_on_y(const float value) { y_coord += value; }

    // Get coordinates as a pair
    std::pair<float, float> get_coordinates() const {
        return std::make_pair(x_coord, y_coord);
    }

    // Set coordinates
    void set_coordinates(const float x, const float y) {
        set_x(x);
        set_y(y);
    }

    // Distance between two points
    static float distance_between_points(const Point& pt1, const Point& pt2) {
        float x_dist = std::abs(pt1.get_x() - pt2.get_x());
        float y_dist = std::abs(pt1.get_y() - pt2.get_y());
        return std::sqrt(x_dist * x_dist + y_dist * y_dist);
    }

    // Calculate distance from origin (0, 0)
    float distance_from_0() const {
        return std::sqrt(x_coord * x_coord + y_coord * y_coord);
    }

    // Sector calculation
    std::string sector() const {
        // TODO(Tigran Grigoryan): maybe convert to switch case?
        if (x_coord == 0 && y_coord == 0)
            return "Point is on both Axis";
        else if (x_coord == 0)
            return "Point is on X Axis";
        else if (y_coord == 0)
            return "Point is on Y Axis";
        else if (x_coord > 0 && y_coord > 0)
            return "Point is in First Sector";
        else if (x_coord < 0 && y_coord > 0)
            return "Point is in Second Sector";
        else if (x_coord < 0 && y_coord < 0)
            return "Point is in Third Sector";
        else if (x_coord > 0 && y_coord < 0)
            return "Point is in Fourth Sector";
        else
            return "ERROR";
    }

    // Equality and Non-Equality operators overloading
    bool operator==(const Point& other) const {
        return x_coord == other.get_x() && y_coord == other.get_y();
    }

    bool operator != (const Point& other) const
    {
        return ! (*this == other);
    }
};

// Definition of static class member
std::vector<Point*> Point::points;


// Overloading out operator
std::ostream & operator << (std::ostream& out, Point & p1)
{
    out << p1.get_x() << " " << p1.get_y() << std::endl;

    return out;
}

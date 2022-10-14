#include <iostream>
#include <String>
using namespace std;
class Cuboid;
class Sphere
{
private:
    int radius;
    double volume;

public:
    void Acceptdata()
    {
        cout << "Enter the radius:";
        cin >> radius;
    }
    void CalculateVolume()
    {
        volume = 4 / 3.0 * 3.14 * radius * radius * radius;
    }
    void Display()
    {
        cout << "The volume of Sphere is :" << volume << endl;
    }
    friend void AddVolume(Sphere sph, Cuboid cbd);
};

class Cuboid
{
private:
    int length, breadth, height;
    double volume;

public:
    void AcceptData()
    {
        cout << "Enter the length:";
        cin >> length;
        cout << "Enter the breadth:";
        cin >> breadth;
        cout << "Enter the height:";
        cin >> height;
    }
    void CalculateVolume()
    {
        volume = length * breadth * height;
    }
    void Display()
    {
        cout << "The volume of Sphere is:" << volume << endl;
    }
};

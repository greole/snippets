#include <iostream>          // for cout and cin


// class 
class Cat                    // begin declaration of the class
{
  public:                    // begin public section
    Cat(int initialAge);     // constructor
    int GetAge();            // accessor function
  private:                   // begin private section
    int age;                 // member variable
};

Cat::Cat(int initialAge) {age = initialAge;}

int Cat::GetAge() {return age;}


// functions
int timestwo(int x) {return 2*x;}

double timestwo(double x) {return 2*x;}

float timestwo(float x) {return 2*x;}

std::string return42() {return "fortytwo";}

//string returnHello()  {return "Hello";}

namespace my_func {
    double timestwo(double x) {return 2*x;}
}

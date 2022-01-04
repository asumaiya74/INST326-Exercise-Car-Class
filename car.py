import math 

class Car:
    def __init__(self, x=0, y=0,heading=0):
        """ Construct a data type car and sets the initial values 
        
        attrubutes: x = horizontal position of the car 
                    y = vertical position of the car 
                    heading = turning angle
        
        Returns: none
        """

        self.x = x
        self.y = y
        self.heading = heading

    
    def turn(self,degree):
        """ Takes a value and turns the car corresponding to set value 
            and updates the attribute of headings with a new value  
        
        Args: 
               degree(float):  represents heading angle in degrees 
               arg_name(data type): description
        
        Returns: none 
        side effects: changes the heading attribute
        """
        self.heading = (self.heading + degree) % 360
       
  
    def drive(self,distance):
        """ takes a distance and moves the car forward according to the distance entered 
            updates the attributes x and y according to the distance entered and the value of heading 
        
        Args: 
               degree(float):  represents heading angle in degrees 
               arg_name(data type): description
               
        Returns: none 
        side effect: changes the x and y postion of the car
        """
        self.x += distance * math.sin(math.radians(self.heading))
        self.y -= distance * math.cos(math.radians(self.heading))

  


def sanity_check():
    """ checks to ensure that the method and class is working properly by turning the car and moving it 
        
        Args: none
        
        Returns: none
        side effect: changes the car postion x and y and the angle of turning heading 
        """
    car_one = Car()
    car_one.turn(90)
    car_one.drive(10)
    car_one.turn(30)
    car_one.drive(20)
    print("Location: ", car_one.x, ',', car_one.y)
    print("Heading:", car_one.heading)
    return car_one
 

if __name__== "__main__":
    sanity_check()

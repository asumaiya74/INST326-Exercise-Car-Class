# Background

For this exercise you will develop a module containing a Car class. Instances of the class will be able to turn and drive forward. They will have three attributes: x, y and heading. x and y will be the coordinates of the car object. For this assignment, x coordinates will increase as a car moves east; y coordinates will increase as a car moves south. Heading  indicates  the  direction  in  which  the  car  will  drive,  in  degrees.  For  this  assignment,  a heading of 0 indicates due north; a heading of 90 is due east; etc.

# Instructions
Car class
Create a class called Car. Define the following methods:
__init__() method
Define  a  method  called  __init__()  (note  the  double  underscores).  Your  method  should  have  one
required parameter (self) and three optional parameters as follows (please use these exact names):
- x: the starting x coordinate of the car, as a float.[1] Default: 0.
- y: the starting y coordinate of the car, as a float. Default: 0.
- heading: the starting heading, as a float. Default: 0.
Your  __init__()  method  should  set  three  attributes  (x,  y,  and  heading)  to  the  values  of  their
corresponding parameters.

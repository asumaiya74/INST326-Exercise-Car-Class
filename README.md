## Background

For this exercise you will develop a module containing a Car class. Instances of the class will be able to turn and drive forward. They will have three attributes: x, y and heading. x and y will be the coordinates of the car object. For this assignment, x coordinates will increase as a car moves east; y coordinates will increase as a car moves south. Heading  indicates  the  direction  in  which  the  car  will  drive,  in  degrees.  For  this  assignment,  a heading of 0 indicates due north; a heading of 90 is due east; etc.

## Instructions
**Car class**

Create a class called Car. Define the following methods:
__init__() method
Define  a  method  called  __init__()  (note  the  double  underscores).  Your  method  should  have  one
required parameter (self) and three optional parameters as follows (please use these exact names):
- x: the starting x coordinate of the car, as a float.[1] Default: 0.
- y: the starting y coordinate of the car, as a float. Default: 0.
- heading: the starting heading, as a float. Default: 0.

Your  __init__()  method  should  set  three  attributes  (x,  y,  and  heading)  to  the  values  of  their
corresponding parameters.

turn() method

Define  a  method  called  turn()  that  has  two  required  parameters,  self  and  a  number  of  degrees
expressed as a float.[2] A positive number of degrees indicates a clockwise turn; a negative number
of  degrees  indicates  a  counterclockwise  turn.  Use  the  following  steps  to  assign  a  new  value  to  the
heading attribute (these can be combined into a single expression):

- Add the specified number of degrees to the previous value of heading.
- Reduce the result of step 1 modulo 360 (this ensures that heading is between 0 and 360).

For  example,  if  heading  is  270  and  the  number  of  degrees  is  100,  the  turn()  method  should  set
heading to (270 + 100) mod 360, which is 10.

drive() method

Define a method called drive() that has two required parameters, self and a distance expressed as
a float.

In  the  formulas  below,  d  is  the  distance;  h  is  the  heading  in  radians  (you  will  need  to  convert  the
heading from degrees to radians).

Update  the  x  attribute  by  adding  d sin(h)  to  the  attribute’s  current  value.  (Hint:  the  +=  operator  is
your friend).

Update  the  y  attribute  by  subtracting  d  cos(h)  from  the  attribute’s  current  value.  (Hint:  the  -=
operator is your friend).

sanity_check() function

Define a sanity_check() function that takes no arguments. This function is not supposed to be part
of the Car class—please de-indent the function header accordingly.
Inside this function, create an instance of the Car class. Have your instance follow these steps:
- Turn 90 degrees.
- Drive 10 units.
- Turn 30 degrees.
- Drive 20 units.

Print  the  location  of  your  instance  on  one  line  and  the  heading  on  the  next  line,  in  the  following
format:
Location: 41.34235262, 17.999999999
Heading: 75

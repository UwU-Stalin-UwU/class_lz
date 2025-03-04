#UwU-Stalin-UwU
#Class lab

#import libs
import matplotlib.pyplot as plt
from math import pi, cos, sin

#class in lab
class Octagon:
    #initialization of object in class
    #setting arguments
    def __init__(self, side, corner, k):            
        self.side=side                              
        self.corner=135
        self.k=1+2**0.5
    
    #funcs to count radius and square of out circle
    def rad_out_circle(self, side):              
        rad_out=(((1+2**0.5)/2**0.5)**0.5)*side
        return(rad_out)
    
    def sq_out_circle(self, rad_out1):
        sq_out=3.14*rad_out1*rad_out1
        return(sq_out)
    
    #funcs to count radius and square of in circle
    def rad_in_circle(self, side, k=1+2**0.5):   
        rad_in=(side/2)*k
        return(rad_in)
    
    def sq_in_circle(self, rad_in1):
        sq_in=rad_in1*rad_in1*3.14
        return(sq_in)

    #func to count square and perimeter of octagon
    def sq_per_oct(self, side, k=1+2**0.5):         
        sq_oct=2*side**2*k
        per_oct=side*8
        return(sq_oct, per_oct)
    
    def versh(self, side) -> list:
        #lists of versh
        versh_x = [] 
        versh_y = [] 

        #creating lists of versh
        for i in range(8): 
            x = self.rad_out_circle(side) * cos((pi/8) + i * (pi/4))
            y = self.rad_out_circle(side) * sin((pi/8) + i * (pi/4))
            versh_x.append(x)
            versh_y.append(y)

        #adding first ccord to the end to connect first and last versh
        versh_x.append(versh_x[0]) 
        versh_y.append(versh_y[0]) 
        return versh_x, versh_y


    def draw_octagon_circles(self, side_length1, versh_x1, versh_y1):
        #OUT CIRCLE DRAWING!!!
        circle1 = plt.Circle((0, 0 ), self.rad_out_circle(side_length1), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle1)

        #IN CIRCLE DRAWING!!!
        circle2 = plt.Circle((0,0 ), self.rad_in_circle(side_length1), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle2)

        #F*cking octagon
        x,y = self.versh(side_length1)
        plt.plot(x, y)

        #display
        plt.axis('scaled')
        plt.show()

#Oct_make func
def oct_make():
    return(Octagon(None, None, None))

#Oct_Count func
def oct_count(oct):
    oct1 = oct
    side_length = input("Please, enter length of side: ")
    side_length = float(side_length)
    Rad_out = oct1.rad_out_circle(side_length)
    Sq_out = oct1.sq_out_circle(Rad_out)
    print("Radius of out circle:", Rad_out, "   Square of out circle:", Sq_out)
    Rad_in = oct1.rad_in_circle(side_length)
    Sq_in = oct1.sq_in_circle(Rad_in)
    print("Radius of in circle:", Rad_in, "   Square of in circle:", Sq_in)
    Sq_oct, Per_oct = oct1.sq_per_oct(side_length)
    print("Square of octagon:", Sq_oct, "   Perimeter of octagon:", int(Per_oct))
    vershx, vershy = oct1.versh(side_length)
    oct1.draw_octagon_circles(side_length, vershx, vershy)

def main():
    oct2=oct_make()
    oct_count(oct2)
    
if __name__=="__main__":
    main()
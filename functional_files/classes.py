#UwU-Stalin-UwU
#Class lab

#import libs
import turtle as tr


#class in lab
class Octagon:
    def __init__(self, side, corner, k):            #initialization of object in class
        self.side=side                              #setting arguments
        self.corner=135
        self.k=1+2**0.5
    
    def rad_sq_out_circle(self, side):              #func to count radius and square of out circle
        rad_out=(((1+2**0.5)/2**0.5)**0.5)*side
        sq_out=3.14*rad_out*rad_out
        return(rad_out, sq_out)
    
    def rad_sq_in_circle(self, side, k=1+2**0.5):   #func to count radius and square of in circle
        rad_in=(side/2)*k
        sq_in=rad_in*rad_in*3.14
        return(rad_in, sq_in)
    
    def sq_per_oct(self, side, k=1+2**0.5):         #func to count square and perimeter of octagon
        sq_oct=2*side**2*k
        per_oct=side*8
        return(sq_oct, per_oct)
    
    # def drawing(self, side):
    #     ws = tr.Screen()
 
    #     # defining a turtle instance
    #     turt = tr.Turtle()
 
    #     # iterating the loop 8 times
    #     for i in range(8):
   
    #         # moving turtle 100 units forward
    #         turt.forward(side)
     
    #         # turning turtle 45 degrees so 
    #         # as to make perfect angle for an octagon
    #         turt.left(45)
        

#Oct_make func
def oct_make():
    return(Octagon(None, None, None))

#Oct_Count func
def oct_count(oct):
    oct1 = oct
    side_length = input("Please, enter length of side: ")
    side_length = float(side_length)
    Rad_out, Sq_out = oct1.rad_sq_out_circle(side_length)
    print("Radius of out circle:", Rad_out, "   Square of out circle:", Sq_out)
    Rad_in, Sq_in = oct1.rad_sq_in_circle(side_length)
    print("Radius of in circle:", Rad_in, "   Square of in circle:", Sq_in)
    Sq_oct, Per_oct = oct1.sq_per_oct(side_length)
    print("Square of octagon:", Sq_oct, "   Perimeter of octagon:", int(Per_oct))
    #oct1.drawing(side_length)

def main():
    oct2=oct_make()
    oct_count(oct2)
    
if __name__=="__main__":
    main()
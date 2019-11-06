class circle:
    def __init__(self, center=(0,0), radius=1):
        if radius < 0:
            raise ValueError("negative radius")
        self.center = center
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def get_center(self):
        return self.center
    
    def get_area(self):
        from math import pi
        return pi*self.radius*self.radius
    
    def get_circumference(self):
        from math import pi
        return 2*pi*self.radius
    
    def move(self,pt):
         self.center(pt)
         
    def grow(self):
         self.radius+=1
         
    def shrink(self):
        if self.radius>0:
            self.radius -= 1
def main():            
    c1=circle((2,4),5)
    print(c1,dir(c1))
    c2=circle((0,0),1)

    print(c1.get_radius())
    print(c1.get_center())
    print(c1.get_area())
    print(c1.get_circumference())


    print(c2.get_radius())
    print(c2.get_center())
    print(c2.get_area())
    print(c2.get_circumference())
main()    

from custom1 import *
c=circle((0,0),4)
c.get_radius()







            
            
    
         
         
    
    
    
    
    
        

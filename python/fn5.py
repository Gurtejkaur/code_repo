def midpoint(pt1,pt2):
    x1,y1 = pt1
    x2,y2 = pt2
    return(x1+x2)/2, (y1+y2)/2
point1 = float(input("enter first point's x:")),\
         float(input("enter first point's y:"))
point2 = float(input("enter second point's x:")),\
         float(input("enter seccond point's y:"))

mid = midpoint(point1,point2)
print("midpoint of",point1,'and',point2, 'is',mid)

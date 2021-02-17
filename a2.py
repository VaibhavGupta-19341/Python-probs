import a1

def checkCollinearity(p1,p2,p3):
    if p1.x * ( p2.y - p3.y ) + p2.x * ( p3.y - p1.y ) + p3.x * ( p1.y - p2.y ) == 0:   #if area of triangle formed by the points = 0, then they are collinear
        return True
    else:
        return False

def checkPointInRect(p,r):
    if ( r.bottom_left_point.x <= p.x <= r.top_right_point.x ) and ( r.bottom_left_point.y <= p.y <= r.top_right_point.y ):
        return True
    else:
        return False

def findIntersection(r1,r2):
    a=max(r1.bottom_left_point.x,r2.bottom_left_point.x)
    b=max(r1.bottom_left_point.y,r2.bottom_left_point.y)
    c=min(r1.top_right_point.x,r2.top_right_point.x)
    d=min(r1.top_right_point.y,r2.top_right_point.y)
    i=a1.Point(a,b)
    j=a1.Point(c,d)
    r_int=a1.Rectangle(i,j)
    return ( r_int.bottom_left_point.x,r_int.bottom_left_point.y ) ,( r_int.top_right_point.x,r_int.top_right_point.y )


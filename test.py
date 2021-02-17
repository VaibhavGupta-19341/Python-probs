# 2 test cases passed each for collinearity, point in rectangle and intersection

import a1
import a2
import introcs

p1=a1.Point(1,1)
p2=a1.Point(3,3)
p3=a1.Point(5,5)

p4=a1.Point(2,2)
p5=a1.Point(2,4)
p6=a1.Point(2,7)

p7=a1.Point(3,7)

r1=a1.Rectangle(p1,p2)
r2=a1.Rectangle(p4,p3)
r3=a1.Rectangle(p1,p7)

if not introcs.assert_equals(a2.checkCollinearity(p1,p2,p3),True,'Points not collinear') and not introcs.assert_equals(a2.checkCollinearity(p4,p5,p6),True,'Points not collinear') and not introcs.assert_equals(a2.checkPointInRect(p4,r1),True,'point not in rectangle') and not introcs.assert_equals(a2.checkPointInRect(p5,r2),True,'Point not in rectangle') and not introcs.assert_equals(a2.findIntersection(r1,r2),((2,2),(3,3)),'Rectangles do not intersect') and not introcs.assert_equals(a2.findIntersection(r3,r2),((2,2),(3,5)),'Rectangles do not intersect'):
    print('DONE')

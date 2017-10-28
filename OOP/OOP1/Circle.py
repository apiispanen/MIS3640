from Point1 import *
import copy


class Circle:
    circle.center = Point()
class box:
    box = Rectangle()
    box.corner = Point()


def point_in_circle(point, circle):
    distance = ((point.x-circle.center.x)**2 + (point.y-circle.center.y)**2)**(1/2)
    if distance > circle.radius:
        return False
    else:
        return True

    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """



def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    point1.x= box.corner.x 
    point1.x= box.corner.y + box.height
    point4.x= box.corner.x + box.width
    point4.x= box.corner.y
    point3.x= box.corner.x + box.width
    point3.x= box.corner.y
    point2.x= box.corner.x 
    point2.x= box.corner.y + box.height
    
    if point_in_circle(point1, circle):
        return 'True for point1'
    else:
        return 'False for point1'

    if point_in_circle(point2, circle):
        return 'True for point2'
    else:
        return 'False for point2'

    if point_in_circle(point3, circle): 
        return 'True for point3'
    else:
        return 'False for point3'

    if point_in_circle(point4, circle):
        return 'True for point4'
    else:
        return 'False for point4'



def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    point1.x= box.corner.x 
    point1.x= box.corner.y + box.height
    point4.x= box.corner.x + box.width
    point4.x= box.corner.y
    point3.x= box.corner.x + box.width
    point3.x= box.corner.y
    point2.x= box.corner.x 
    point2.x= box.corner.y + box.height
    
    if point_in_circle(point1, circle) or  point_in_circle(point2, circle) or  point_in_circle(point3, circle) or  point_in_circle(point4, circle):
        return True
    else:
        return False




def main():
    
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()

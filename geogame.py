from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rect(self, rectangle):
            min_x = min(rectangle.point1.x, rectangle.point2.x)
            max_x = max(rectangle.point1.x, rectangle.point2.x)
            min_y = min(rectangle.point1.y, rectangle.point2.y)
            max_y = max(rectangle.point1.y, rectangle.point2.y)

            if min_x <= self.x <= max_x and min_y <= self.y <= max_y:
                return True
            else:
                return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)
class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)  # Move to top-left corner
        canvas.pendown()
        canvas.goto(self.point2.x, self.point1.y)  # Draw to top-right corner
        canvas.goto(self.point2.x, self.point2.y)  # Draw to bottom-right corner
        canvas.goto(self.point1.x, self.point2.y)  # Draw to bottom-left corner
        canvas.goto(self.point1.x, self.point1.y)  # Complete rectangle

class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
              Point(randint(10, 400), randint(10, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Enter x coordinate: ")), float(input("Enter y coordinate: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rect(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
myturtle=turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()



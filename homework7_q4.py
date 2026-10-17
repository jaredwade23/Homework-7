from graphics import GraphWin, Line, Point, Circle, Text
import time


def moveball(ball, win, distance, steps):
    step = distance / steps

    for i in range(steps):
        ball.move(0, step)
        time.sleep(0.1)


def main():
    height = float(input("Enter the initial height in meters: "))

    if height <= 0:
        print("Height must be greater than zero.")
        return

    win = GraphWin("Bouncing Ball", 500, 500)
    win.setCoords(0, 0, 10, 10, height)

    radius = height * 0.025
    x = 5

    ground = Line(Point(0, 0), Point(10, 0))
    ground.draw(win)

    ball = Circle(Point(x, height), radius)
    ball.setFill("red")
    ball.draw(win)

    time.sleep(0.5)

    # Drop the ball to the ground.
    moveball(ball, win, height, 10)

    bounce_height = height * 0.60

    while bounce_height >= 0.001:
        # Move the ball up to the bounce height.
        moveball(ball, win, bounce_height - radius, 30)

        # Move the ball back down to the ground. 
        moveball(ball, win, bounce_height - radius, 30)

        bounce_height = bounce_height * 0.60

    Text(Point(5, height * 0.1), "Bouncing Finished!").draw(win)

    win.getMouse()
    win.close()


main()

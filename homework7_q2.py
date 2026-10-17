
from graphics import *


class Button:
    """A labeled rectangular button drawn in a graphics window."""

    def __init__(self, p1, p2, text):
        self.shape = Rectangle(p1, p2)
        self.shape.setFill("lightblue")
        self.label = Text(Point((p1.getX() + p2.getX()) / 2,
                                (p1.getY() + p2.getY()) / 2), text)

    def draw(self, window):
        self.shape.draw(window)
        self.label.draw(window)
        return self

    def contains(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        return (p1.getX() <= point.getX() <= p2.getX() and
                p1.getY() <= point.getY() <= p2.getY())


def clickedButton(click, button):
    return button.contains(click)


def main():
    win = GraphWin("Button Example", 400, 300)

    button = Button(Point(150, 120), Point(250, 170), "Click Me")
    button.draw(win)

    message = Text(Point(200, 220), "Click the button to continue")
    message.draw(win)

    click = win.getMouse()

    while not clickedButton(click, button):
        click = win.getMouse()

    message.setText("Button clicked!")

    win.getMouse()
    win.close()


main()


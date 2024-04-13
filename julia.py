import turtle
import math

def julia(z, c, n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return julia(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

# screen size (in pixels)
screenx, screeny = 800, 600
# complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-2.0, 2.0)
# discretization step
step = 2

# turtle config
turtle.tracer(0, 0)
screen = turtle.Screen()
screen.title("Julia Fractal (discretization step = %d)" % (int(step)))

jTurtle = turtle.Turtle()
jTurtle.penup()

# px * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny
# Julia constant
julia_constant = complex(-0.7, 0.27015)
# plot
for px in range(-int(screenx/2), int(screenx/2), int(step)):
    for py in range(-int(screeny/2), int(screeny/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        z = complex(x, y)
        m = julia(z, julia_constant)
        if not math.isnan(m.real):
            r = int(abs(math.sin(m.imag)) * 255)
            g = int(abs(math.sin(m.imag + (2 * math.pi / 3))) * 255)
            b = int(abs(math.sin(m.imag + (4 * math.pi / 3))) * 255)
            color = (r, g, b)
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            jTurtle.color(hex_color)
            jTurtle.dot(2.4, hex_color)
            jTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()

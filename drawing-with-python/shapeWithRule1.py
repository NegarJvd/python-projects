import stddraw

xScale = 35
yScale = 35
axis = 30

stddraw.setXscale(-xScale, xScale)
stddraw.setYscale(-yScale, yScale)

stddraw.line(-axis, 0, axis, 0)
stddraw.line(0, axis, 0, -axis)

for i in range(1, axis+1):
    stddraw.setPenColor(stddraw.RED)
    stddraw.line(i, 0, 0, axis+1-i)
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.line(-i, 0, 0, axis+1- i)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.line(i, 0, 0, i-axis-1)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.line(-i, 0, 0, i-axis-1)
    stddraw.show(100)

stddraw.show()
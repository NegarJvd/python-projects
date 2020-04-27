import stddraw

stddraw.setXscale(-2, 12)
stddraw.setYscale(-2, 12)

stddraw.line(0, 0, 10, 0)
stddraw.line(10, 0, 5, 10)
stddraw.line(5, 10, 0, 0)
i = 0
j = 10
while i<10 and j>0:
    stddraw.line(i, 0, -i/2 + 10, i)
    stddraw.line(i, 0, j/2, j)
    i += 1
    j -= 1
    stddraw.show(300)
stddraw.show()


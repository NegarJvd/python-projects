import stddraw

def nesting(x1, y1, x2, y2, x3, y3, x4, y4):
    stddraw.setPenColor(stddraw.WHITE)
    if x1 < 0.5 and x2 < 0.5 and x3 < 0.5 and x4 < 0.5:
        stddraw.line(x1, y1, x2, y2)
        stddraw.line(x2, y2, x3, y3)
        stddraw.line(x3, y3, x4, y4)
        stddraw.line(x4, y4, x1, y1)
    else:
        stddraw.line(x1, y1, x2, y2)
        stddraw.line(x2, y2, x3, y3)
        stddraw.line(x3, y3, x4, y4)
        stddraw.line(x4, y4, x1, y1)
        stddraw.show(100)
        x5 = (x1 + x2) / 2
        y5 = (y1 + y2) / 2
        x6 = (x2 + x3) / 2
        y6 = (y2 + y3) / 2
        x7 = (x3 + x4) / 2
        y7 = (y3 + y4) / 2
        x8 = (x4 + x1) / 2
        y8 = (y4 + y1) / 2
        nesting(x5, y5, x6, y6, x7, y7, x8, y8)

def main():
    r = 8
    stddraw.setXscale(-(r+2), r+2)
    stddraw.setYscale(-(r+2), r+2)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledSquare(0,0,r+2)
    xH1 = r
    yH1 = r
    xH2 = -r
    yH2 = r
    xH3 = -r
    yH3 = -r
    xH4 = r
    yH4 = -r

    nesting(xH1, yH1, xH2, yH2, xH3, yH3, xH4, yH4)
    stddraw.show()

if __name__ == '__main__':
     main()



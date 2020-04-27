import stddraw
import math


def centers(x,y,r):
    centerArray = [[0.0 for i in range(2)]for j in range(6)]
    centerArray[0][0] = x+r
    centerArray[0][1] = y
    centerArray[1][0] = x+(r/2)
    centerArray[1][1] = y+(r * math.sin(math.pi/3))
    centerArray[2][0] = x-r/2
    centerArray[2][1] = y+(r * math.sin(math.pi/3))
    centerArray[3][0] = x-r
    centerArray[3][1] = y
    centerArray[4][0] = x-(r/2)
    centerArray[4][1] = y-(r * math.sin(math.pi/3))
    centerArray[5][0] = x+r/2
    centerArray[5][1] = y-(r * math.sin(math.pi/3))
    return centerArray


def main():
    R = 3
    stddraw.setXscale(-5*R,5*R)
    stddraw.setYscale(-5*R,5*R)
    stddraw.setCanvasSize(700,700)
    stddraw.circle(0,0,R)
    centerPointArray1 = centers(0,0,R)

    # stddraw.setPenColor(stddraw.RED)
    # for i in range(-6*R,6*R):
    #     for j in range(-6*R,6*R):
    #         stddraw.line(i,j,i,(6*R)-j)
    #         stddraw.line(i, j, (6*R)-i, j)

    # stddraw.setPenColor(stddraw.BLACK)
    for i in range(6):
        stddraw.circle(centerPointArray1[i][0], centerPointArray1[i][1], R)
        stddraw.show(50)

    for i in range(6):
        centerPointArray2 = centers(centerPointArray1[i][0], centerPointArray1[i][1], R)
        for j in range(6):
            stddraw.circle(centerPointArray2[j][0], centerPointArray2[j][1], R)
            # stddraw.picture('python.png' ,centerPointArray2[j][0], centerPointArray2[j][1] )
            for k in range(6):
                centerPointArray3 = centers(centerPointArray2[k][0], centerPointArray2[k][1], R)
                for p in range(6):
                    stddraw.circle(centerPointArray3[p][0], centerPointArray3[p][1], R)
                    # stddraw.picture('python.png', centerPointArray3[p][0], centerPointArray3[p][1])
                    stddraw.show(15)

    # for i in range(6):
    #     centerPointArray3 = centers(centerPointArray2[i][0], centerPointArray2[i][1], R)
    #     for j in range(6):
    #         stddraw.circle(centerPointArray3[j][0], centerPointArray3[j][1], R)
    #         stddraw.show(50)

    stddraw.show()


if __name__ == '__main__':
    main()
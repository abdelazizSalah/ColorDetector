import cv2
import pandas as pd

# reading image
img_path = r"C:/GitHub/Colors/colorpic.jpg"
img = cv2.imread(img_path)

# declare some global variables
X = Y = r = g = b = 0
Clicked = False

# read from csv file
myArr = ['Color', 'ColorName', 'Hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=myArr)


def draw(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONUP:
        global X, Y, r, g, b, Clicked
        Clicked = True
        X = x
        Y = y
        b, g, r = img[y, x]
        b = int(b)
        r = int(r)
        g = int(g)


cv2.namedWindow('ColorDetector')
cv2.setMouseCallback('ColorDetector', draw)


def GetColorName(R, G, B):
    min = 1000000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G -
                                                int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))

        if d <= min:
            min = d
            cname = csv.loc[i, 'ColorName']

    return cname


while True:
    cv2.imshow('ColorDetector', img)

    if Clicked:
        cv2.rectangle(img, (0, 20), (600, 60), (b, g, r),  -1)
        text = GetColorName(r, g, b) + ' R = ' + str(r) + \
            ' G = ' + str(g) + ' B = ' + str(b)

        if r + g + b >= 500:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, text, (50, 50), 2, 0.8,
                        (255, 255, 255), 2, cv2.LINE_AA)
    Clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

import cv2

img = cv2.imread('images/image.png')

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))


# img[0:100, 0:150]
cv2.imshow('Result', img)

# print(img.shape)

cv2.waitKey(0)


# cap = cv2.VideoCapture('videos/ffSupra.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# cap = cv2.VideoCapture(0)
# cap.set(3, 500)
# cap.set(4, 300)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


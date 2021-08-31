import cv2

image = cv2.imread("minions.webp")
cv2.imshow("minion", image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New minion",gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.imshow("Inverted",inverted_image)
cv2.waitKey(0)

blur = cv2.GaussianBlur(inverted_image,(21,21),0)

inverted_blur = 255 - blur
pencil_sketch = cv2.divide(gray_image,inverted_image, scale=256.0)
cv2.imshow("Sketch",pencil_sketch)
cv2.waitKey(0)

cv2.imshow("original image", image)
cv2.imshow("pencil sketch",pencil_sketch)
cv2.waitKey(0)
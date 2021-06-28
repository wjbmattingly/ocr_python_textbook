#https://nanonets.com/blog/ocr-with-tesseract/
#COVERED IN THIS VIDEO:
#


def remove_borders(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    cnt = cntsSorted[-1]
    print (len(contours))
    x,y,w,h = cv2.boundingRect(cnt)
    crop = img[y:y+h,x:x+w]
    return (crop)





no_borders = remove_borders(no_noise)
cv2.imwrite("temp/no_borders.jpg", no_borders)
display("temp/no_borders.jpg")

color = [255, 255, 255] # 'cause purple!

# border widths; I set them all to 150
top, bottom, left, right = [150]*4

img_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

cv2.imwrite("temp/image_border.jpg", img_with_border)
display("temp/image_border.jpg")




















# image = cv2.imread('data/page_01.jpg', 0)
# clahe = cv2.createCLAHE().apply(image)
#
# sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# sharpen = cv2.filter2D(clahe, -1, sharpen_kernel)
#
# thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# cv2.imshow('clahe', clahe)
# cv2.imshow('sharpen', sharpen)
# cv2.imshow('thresh', thresh)
#
# cv2.waitKey()

# # get grayscale image
# def get_grayscale(image):
#     return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# # noise removal
# def remove_noise(image):
#     return cv.medianBlur(image,5)
# img = cv.imread('data/page_01.jpg')
# img = get_grayscale(img)
# # img = remove_noise(img)
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
#
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

import cv2

class ImageProcessing:
    def __init__(self, image_path='./image/src.png', save_path='./image/test.png'):
        self.image_path = image_path
        self.save_path = save_path
        self.img = None
        self.point1 = None
        self.point2 = None

    def on_mouse(self, event, x, y, flags, param):
        img2 = self.img.copy()
        if event == cv2.EVENT_LBUTTONDOWN:         
            self.point1 = (x,y)
            cv2.circle(img2, self.point1, 10, (0,255,0), 5)
            cv2.imshow('image', img2)
        elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):   
            cv2.rectangle(img2, self.point1, (x,y), (255,0,0), 5)
            cv2.imshow('image', img2)
        elif event == cv2.EVENT_LBUTTONUP:         
            self.point2 = (x,y)
            cv2.rectangle(img2, self.point1, self.point2, (0,0,255), 5) 
            cv2.imshow('image', img2)
            self.crop_and_resize()

    def crop_and_resize(self):
        min_x = min(self.point1[0], self.point2[0])     
        min_y = min(self.point1[1], self.point2[1])
        width = abs(self.point1[0] - self.point2[0])
        height = abs(self.point1[1] -self.point2[1])
        cut_img = self.img[min_y:min_y+height, min_x:min_x+width]
        resize_img = cv2.resize(cut_img, (28,28))
        ret, thresh_img = cv2.threshold(resize_img,127,255,cv2.THRESH_BINARY) 
        cv2.imshow('result', thresh_img)
        cv2.imwrite(self.save_path, thresh_img)  

    def main(self):
        self.img = cv2.imread(self.image_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.on_mouse)
        cv2.imshow('image', self.img)
        cv2.waitKey(0)

if __name__ == '__main__':
    ImageProcessing().main()

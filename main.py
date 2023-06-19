# This is a sample Python script.
import cv2
def main(fname):
    """Загрузка видео и сохранение кадров в формате jpg"""
    if fname.endswith('mp4') or fname.endswith('mov') or fname.endswith('avi') or fname.endswith('mpeg') or fname.endswith('mpg'):
        cap = cv2.VideoCapture(fname)
        cadr = 0
        while cap.isOpened():
            ret, frame = cap.read()
            cadr += 1
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            cv2.imshow('frame', frame)
            cv2.imwrite('shirokoe_frame_%d.jpg' % cadr, frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    fname = 'shirokoe_stars.mov'
    main(fname)
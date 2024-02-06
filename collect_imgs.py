import os
import cv2
import warnings
warnings.filterwarnings("ignore")

# Data directory to save the words
# choose 'data' for words that have one hand        or 'data_two' for words that have two hands
DATA_DIR = './data_two'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Number of words to collect
number_of_classes = 5

# Number of images to collect per word
dataset_size = 100

# Start collecting images from (ns) word
ns = 16

cap = cv2.VideoCapture(0)

for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j + ns))):
        os.makedirs(os.path.join(DATA_DIR, str(j + ns)))

    print('Collecting data for class {}'.format(j + ns))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" or "N" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        key = cv2.waitKey(25)

        if key == ord('q'):
            done = True
            break
        elif key == ord('n'):
            break

    if done:
        break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        key = cv2.waitKey(25)

        # Save image only when a numeric key is pressed (0-9)
        if key >= ord('0') and key <= ord('9'):
            class_index = key - ord('0') + ns
            image_path = os.path.join(DATA_DIR, str(class_index), '{}.jpg'.format(counter))
            cv2.imwrite(image_path, frame)
            print('Saved image {} for class {}'.format(counter, class_index))
            counter += 1

cap.release()
cv2.destroyAllWindows()

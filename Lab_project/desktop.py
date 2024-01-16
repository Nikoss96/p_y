import PySimpleGUI as sg
import cv2
import numpy as np

prototxt_path = 'voc/MobileNetSSD_deploy.prototxt'
model_path = 'voc/MobileNetSSD_deploy.caffemodel'
min_confidence = 0.2

classes = ['background','aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor']
np.random.seed(543210)
colors = np.random.uniform(0,255,size = (len(classes),3))

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

#'DefaultNoMoreNagging', 
#'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 
#'HotDogStand', 'Kayak', 'LightBlue'

def main():
    
    sg.theme('DarkBrown6')
    info = "lab_info: "
    filling = ""
    # define the window layout
    layout = [
      [sg.Text('Image from 713', size=(60, 1), justification='center')],
      [sg.Image(filename='', key='-IMAGE-')],
      [sg.Text(info + filling, size=(90, 1), justification='center',key = '-UPDLAB-')],
      [sg.Radio('None', 'Radio', True, size=(10, 1))],
      [sg.Radio('blur', 'Radio', size=(10, 1), key='-BLUR-'),
       sg.Slider((1, 11), 1, 1, orientation='h', size=(40, 15), key='-BLUR SLIDER-')],
      [sg.Radio('hue', 'Radio', size=(10, 1), key='-HUE-'),
       sg.Slider((0, 225), 0, 1, orientation='h', size=(40, 15), key='-HUE SLIDER-')],
      [sg.Button('Exit', size=(10, 1))]
    ]

    window = sg.Window('Monitoring lab', layout, location=(800, 400))

    cap = cv2.VideoCapture(0)

    while True:
        event, values = window.read(timeout=20)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break

        ret, image = cap.read()

  
        if values['-BLUR-']:
            image = cv2.GaussianBlur(image, (21, 21), values['-BLUR SLIDER-'])
        elif values['-HUE-']:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image[:, :, 0] += int(values['-HUE SLIDER-'])
            image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        #_, image = cap.read()

        height,width = image.shape[0],image.shape[1]
        blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007,(300,300),130)
        
        net.setInput(blob)
        detected_objects = net.forward()
        height,width = image.shape[0],image.shape[1]
        blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007,(300,300),130)
        
        net.setInput(blob)
        detected_objects = net.forward()
        filling = ""
        map_filling = {}
        for i in range(detected_objects.shape[2]):
            confidence = detected_objects[0][0][i][2]
            
            if confidence > min_confidence:
                class_index = int(detected_objects[0,0,i,1])
                map_filling[classes[class_index]] = map_filling.get(classes[class_index],0) + 1
                #print(classes[class_index],confidence)
                #filling = filling + str(classes[class_index])
                upper_left_x = int(detected_objects[0,0,i,3] * width)
                upper_left_y = int(detected_objects[0,0,i,4] * height)
                lower_right_x = int(detected_objects[0,0,i,5] * width)
                lower_right_y = int(detected_objects[0,0,i,6] * height)
                
                prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
                cv2.rectangle(image, (upper_left_x,upper_left_y),(lower_right_x,lower_right_y),colors[class_index],3)
                cv2.putText(image,prediction_text,(upper_left_x,
                            upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15),
                            cv2.FONT_HERSHEY_SIMPLEX,0.6,colors[class_index],2)
            #cv2.imshow("Detected Objects", image)
        for i in map_filling.keys():
            filling = filling + " " + str(i) + ": " + str(map_filling[i])
        imgbytes = cv2.imencode('.png', image)[1].tobytes()
        window['-UPDLAB-'].update(info + filling)
        window['-IMAGE-'].update(data=imgbytes)

    window.close()


main()
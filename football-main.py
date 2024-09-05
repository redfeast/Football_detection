from infer_detector import Infer
inf=Infer()
#Initialise and Load the mode

model_name='yolov3'
f=open('classes.txt')
class_list=f.readlines()
f.close()

weights = "best_yolov3_football.pt"
usage_mode=int(input("choose execution mode 1 or 2\n1 . CPU\n2 . GPU\n(default:1)\n"))
if usage_mode==2:
    print("Executing Using GPU")
    use_gpu=True
else:
    print("Executing using CPU")
    use_gpu=False
               
inf.Model(model_name, class_list, weights, use_gpu=use_gpu, input_size=416)


while True:

    try :

        input_mode=int(input("Choose one inference mode by entering 1 or 2\n1.image\n2. video\n"))
        if input_mode==1:
            img_path=input('Enter path to Image\n')
            inf.Predict_On_Image(img_path,conf_thresh=0.3,iou_thresh=0.5)
        else:
            print("Beginning video inference, press keyboard interupt after video input to close\n")
            video_path=input('Enter the path to video\n')
            out_name=video_path.split(sep='.')[0]+'_out.mp4'
            inf.video_detection(video_path,out_name)

    except KeyboardInterrupt:
        break

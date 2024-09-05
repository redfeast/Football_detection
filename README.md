# OVERVIEW

>Football detection system is implemented using ObjectDetection AI model. Objectdetection is defined as detecting the position of objects with coordinates and also identifying the type of objects. In comparision with image classification it has in addition the ability to locate the objects in scene. 

>Here our objective is to specifically detect football in image and video input. It is achieved by training Deep learning model with Convolutional Neural Networks for object detection using the yolov3 architecture. 

>The Model is trained using football images and annotations from OpenImages Dataset and initialised using coco weights on pytorch framework. Image inference and Video inference are built on top of pytorch model.

>Source Code is developed with reference and basing on Ultralytics YoloV3. It took lot of code creation  and  changes to make the video inference .

>test images and videos are collected from license free sources on internet 

> The Main Apllication executes in either GPU mode or CPU mode . I recommend First execute in CPU mode and later GPU MOde to feel the differnece. It can inference both on Image and Video input. 

## Tools and Frameworks used

python 3.11
conda package Environment
pytorch with CUDA
opencv-python
numpy
matplotlib
jupyter-notebook


# Installation 

1. for GPU execution Install nvidia and CUDA drivers  using following instructions at

    https://gist.github.com/bennyistanto/46d8cfaf88aaa881ec69a2b5ce60cb58

   CUDA version really depends on GPU variant 

   Also GPU execution might terminate abrubtly becuase of full memory

i recommend first setting up a conda environment as suggested above using python 3.11.

2. Activate the cuda environment in conda (Anaconda prompt) using following command

    conda activate <name-given-by-you>

3. Install requirements in the activated environment using

    pip install -r requirements.txt


# Execution

after succesfully installing everything in conda environment run the football detection using following command

    python football-main.py

It will prompt for GPU or cpu mode and also for Image or Video Input.

>Image outout will be stored in 'output' folder in image and text format

>As of now Video has only frame by frame live output , it doesnt save anywhere

>Application will execute in continuous loop unless encountered by or interrupted with keyboard  ctrl-C

# Test files
input1.jpg - gives output in out folder
test1.mp4 - dynamic output



# Methodology

Objectdetection is one of most popular problems of  computer vision with  applications in multiple fields . There are multiple approaches to solve this problem inlcuiding tradtional methods like Haar CAscades that are trained with sets of positive and negative samples whereas they can only work with simple features like face detection

However the predominant methods  are
    1. Regions based methods like R-CNNs (Regional- COnvolutional Neural Networks)
    2. Single Shot MEthods like YOLO (You look Only Once)

 Region based algorithms detect in multiple stages , region by region whereas SingleShot method detects the entire input in one go.

 Region based methods have better accuracy but SingleSHot method have great speed in detection


 So deciding factor will be what matters more to you and resource availabilty based on used case


 There are advanced algorithms which are cobination of both worlds like Efficientdet . These ObjectDetection is also being implemented with Transformers.

# Reason to choose Singleshot method

 In this Problem of Football detection Singleshot has been given priority as speed of detection and resouces needed are less also yolov3 has multiscale detection with three detection heads which also helps in easily detecting objexts at different scales which is very needed in sports

## Training MEthodology
The pretrained weights used in this project are trained to detect only one object which is "Ball" using BAll images from "OpenIMages Datset" . This is achieved using transferred learning from yolov3 base weights trained on COCO Dataset . trainnig is performed 

##  inference methodology

Detecion in yolov3 happens based on Anchor boxes and objectness score. the model divides the entire image into anchor boxes with objects and each box will have objecnessscore to figureout likelyhood of having object, probability of class and IoU. Based on these three parameter Non Macimal Supression is perfomred to detect final boxes. 

## Metrics
MEan Average Precision(mAP) is used to measure the performance of  object Detection models it is mean  classwise  AVerage Precison, which is arrived at by calcualting recall for all classes using IOU threshold.

The used pretrained model is said to have mAP of 0.85 @ IOU 0.5


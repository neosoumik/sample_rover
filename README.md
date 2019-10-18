# B_help
## Challenge : To help visually-impaired people and to serve military purposes.


We are aimed to provide blind people the reliable way to move aroud

  - using computer vision.
  - reliable than any living persons if correctly executed.
  - We also aim to use it as a robot to send it to the nearest store be it a grocery or a medical one ofcourse with a prescription.
  
# New Features added!

  - We have implemented an audio output to indicate the blind about the object detected.
  - We have automated the robot to pass around an obstacle at the moment. 
  - We are trying to establish communication with the navigation APIs to make it self driven.
  - Trying to use out rover as a surviallence to patrol the city, to use it in the military if weapon detection is implemented and probably use it as a package delivery and garbage collecting truck prototype.... 
#### Note: Maps API implementation will be done soon............

<img src="https://i.ibb.co/2ggKRjn/IMG-20190124-012650-HHT.jpg" width="40%">

### Tech


* [Cuda] -GPU calculation for image processing
* [OpenCV] - Object detection
* [Tensorflow-GPU] - To run Machine Learning in GPU
* [Yolo V3] - pretrained module for object detection
* [python code] - interfacing with raspberrypi and detection




### Development

We have currently successfully streamed a realtime video with the help of the pi camera by running the pi_steam.py. We have successfully loaded the distance measured from the rasapberry pi onto the laptop by the use of servers and client connection establishment with the help of sockets.

We are currently trying to automate our device to bypass an obstacle and hope to achieve it soon.

To execute the code ,you are supposed to run the pi_stream.py,pigpiod and ultra.py as super user on the raspberrypi

On the lapto,edit the lan connections you are connected to the raspberrypi into the rov.py and detect.py so that you can stream the video and control the GPIO pin of the raspberrypi

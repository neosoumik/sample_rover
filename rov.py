import curses
from gpiozero import Motor
from gpiozero import Servo
from gpiozero import LED
from time import sleep
#1 and 2 forward and backward 3 right and left
motor1 = Motor(forward=17, backward=4)
motor2 = Motor(forward=22, backward=27)
motor3 = Motor(forward=23, backward=24)
cam_mov= Servo(2)
red = LED(25)
red.on()
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
def my_front():
    motor1.forward()
    motor2.forward()
    motor3.stop()
def my_back():
    motor1.backward()
    motor2.backward()
    motor3.stop()
def my_break():
    motor1.stop()
    motor2.stop()
    motor3.stop()
def my_left():
    motor3.forward()
def my_right():
    motor3.backward()
def cam_left():
    cam_mov.max()
def cam_right():
    cam_mov.min()
def cam_stable():
    cam_mov.mid()
	

import curses
import socket
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
def my_frontr():
    motor3.backward()
    motor1.forward()
    motor2.forward()
def my_frontl():
    motor3.forward()
    motor1.forward()
    motor2.forward() 
def my_backl():
    motor3.backward()
    motor1.backward()
    motor2.backward()
def my_backr():
    motor3.forward()
    motor1.backward()
    motor2.backward()    
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
def cvcheck():
            global detc
            s = socket.socket()
            host = socket.gethostname()
            port = 12316
            s.connect((host, port))
            detc = s.recv(1024)
            print(detc)
            s.close
def ulcheck():
            global detu
            u = socket.socket()
            u.connect(('192.168.43.202',118))
            detu = u.recv(1024)
            print(detu)
            u.close

	
try:
  while True:
            cvcheck()
            ulcheck()

            if detu == b'blocked' and detc == b'obstruction':
               my_break()
               char = curses.KEY_DOWN
               cam_left()
               sleep(2.5)
               cvcheck()
               print(detc)
               

               if detc == b'obstruction':
                   cam_right()
                   sleep(2.5)
                   cvcheck()
                   print(detc)
                   my_break()
                   char = curses.KEY_DOWN
                   
                   if detc == b'obstruction':
                      cam_stable()
                      char = curses.KEY_DOWN
                      my_break()
                   else:
                     my_frontr()
                     sleep(0.6)
                     my_frontl()
                     sleep(0.2)
                     my_break()
                     my_front()
                   #  my_right()
                     sleep(0.2)
                     my_break()
                     cam_stable()
               else:
                   my_frontl()
                   sleep(0.6)
                   my_frontr()
                   sleep(0.2)
                   my_break()
                   my_front()
                 #  my_left()
                   sleep(0.2)
                   my_break()
                   cam_stable()

            elif detu == b'blocked':
                   my_break()
                   char = curses.KEY_DOWN

            else :
               curses.flushinp()
               char = screen.getch()



            
            if char == ord('q'):
                break
            if char == ord('S'): # Added for shutdown on capital S
                os.system ('sudo shutdown now') # shutdown right now!
            elif char == curses.KEY_UP :
                my_front()
                sleep(0.05)
                my_break()
            elif char == curses.KEY_DOWN : 
                my_break()
            elif char == curses.KEY_RIGHT:
                my_frontr()
                sleep(0.05)
                my_break()
            elif char == curses.KEY_LEFT:
                my_frontl()
                sleep(0.05)
                my_break()
            elif char == ord('x'):
                my_back()
                sleep(0.05)
                my_break()
            elif char == ord('z'):
                my_backl()
                sleep(0.05)
                my_break()
            elif char == ord('c')
                my_backr()
                sleep(0.05)
                my_break()
            elif char == ord('w'):
                cam_stable()
            elif char == ord('a'):
                cam_left()
            elif char == ord('d'):
                cam_right()



finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

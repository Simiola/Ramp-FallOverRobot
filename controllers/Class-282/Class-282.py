from controller import Robot
from controller import Motor
from controller import Altimeter
from controller import LED
import math

class MyController(Robot):
    def __init__(self):
        super(MyController,self).__init__()
        self.timestep=32
        #get Devices tags
        self.altimeter= self.getDevice("altimeter")
        self.altimeter.enable(self.timestep)
        
        self.distanceSensor=self.getDistanceSensor("ds0")
        self.distanceSensor.enable(self.timestep)
        
        self.distanceSensor=self.getDistanceSensor("ds1")
        self.distanceSensor.enable(self.timestep)
        
        self.left_motor=self.getDevice("left wheel motor")
        self.right_motor=self.getDevice("right wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor.setPosition(math.inf)
        
        self.direction_switch=False
   
        
    def run(self):
        while self.step(self.timestep) != -1:
            altitude= self.altimeter.getValue()
            print(altitude)
            
            if(not self.direction_switch):
                self.left_motor.setVelocity(2.0)
                self.right_motor.setVelocity(2.0)
                if(altitude<=0.05):
                    self.direction_switch=True
            else:
                self.left_motor.setVelocity(-2.0)
                self.right_motor.setVelocity(-2.0)
                if(altitude>=0.25):
                    self.direction_switch=False
                
        
   
control_robot=MyController()
control_robot.run()
print(control_robot)
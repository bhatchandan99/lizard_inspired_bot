# -*- coding: utf-8 -*-
"""
Created on Fri Oct 04 17:35:10 2019

@author: bhatc
"""

import vrep
import sys
import math
import time
import matplotlib.pyplot as plt


vrep.simxFinish(-1)
def phase(b):
    
    
    tf=(3*math.pi/20)*(math.sin((math.pi/2)*b-(math.pi)));
    tm = (math.pi/30)*(math.sin((math.pi/2)*b));
    tr=(3*math.pi/20)*(math.sin((math.pi/2)*b));
    return tf,tr,tm

 # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID != -1:
    print ('done')
    
else:
    print('not sucess')
    sys.exit('could not')
    

res,servo_front=vrep.simxGetObjectHandle(clientID,'Front_rev',vrep.simx_opmode_blocking)
res,servo_back=vrep.simxGetObjectHandle(clientID,'Back_rev',vrep.simx_opmode_blocking)
res,servo_middle=vrep.simxGetObjectHandle(clientID,'Middle_rev',vrep.simx_opmode_blocking)
res,body_back=vrep.simxGetObjectHandle(clientID,'Back',vrep.simx_opmode_blocking)

print('dude')
t = time.time()
z= 0;
v= 0;
while (time.time()-t ) <= 100:
   
    res,linearVelocity,angularVelocity = vrep.simxGetObjectVelocity(clientID,body_back,vrep.simx_opmode_streaming)
   
    print('vy' , linearVelocity[1])
    
    z = z+1;
    v= v+ (linearVelocity[1]);
    
    #plt.plot(time.time(),linearVelocity[1],'go--')
    #plt.xlabel('time(s)')
    #plt.ylabel('velocity(m/s)')
    #plt.grid(True)
    
    #plt.hold(True)
    

    tf,tr,tm= phase(time.time())
    vrep.simxSetJointTargetPosition(clientID,servo_front, tf,vrep.simx_opmode_oneshot)
    
    vrep.simxSetJointTargetPosition(clientID,servo_back, tr,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,servo_middle, tm,vrep.simx_opmode_oneshot)


print(v/z);

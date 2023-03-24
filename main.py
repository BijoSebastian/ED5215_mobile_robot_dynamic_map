#!/usr/bin/env python

"""
Mobile robot simulation setup
@author: Bijo Sebastian 
"""

#Import libraries
import time

#Import files
import sim_interface
import control

def main():
    if (sim_interface.sim_init()):

        #Obtain handles to sim elements
        sim_interface.get_handles()

        #Start simulation
        if (sim_interface.start_simulation()):
            
            #Stop robot
            sim_interface.setvel_pioneers(0.0, 0.0)

            #Set goal state
            goal_state = [9, 0]

            #Obtain robots position
            robot_state = sim_interface.localize_robot()

            while not control.at_goal(robot_state, goal_state):
                [V,W] = control.gtg(robot_state, goal_state)
                sim_interface.setvel_pioneers(V, W)
                time.sleep(0.5)
                robot_state = sim_interface.localize_robot()
                sim_interface.localize_bills()
                
            #Stop robot
            sim_interface.setvel_pioneers(0.0, 0.0)

        else:
            print ('Failed to start simulation')
    else:
        print ('Failed connecting to remote API server')
    
    #stop robots
    sim_interface.setvel_pioneers(0.0, 0.0)
    sim_interface.sim_shutdown()
    time.sleep(2.0)
    return

#run
if __name__ == '__main__':

    main()                    
    print ('Program ended')
            

 
'''
paulsWatch.py

    Current Author:     Tanner Mathew Utz
    Date:               8/18/2022
    Original Author:    Tanner Mathew Utz

    Description:
                        This script is intended to handle all time related tasks
    Credited Links:  
                        N/A
'''
import paulsMemory
import time

class StopWatch:

    def start(self):
        paulsMemory.startTime = time.time()

    def stop(self):
        paulsMemory.stopTime = time.time()

    def setElapsedTime(self):
        paulsMemory.elapsedTime = round(paulsMemory.stopTime - paulsMemory.startTime)
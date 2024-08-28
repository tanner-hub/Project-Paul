'''
paulsMemeory.py

    Current Author:     Tanner Mathew Utz
    Date:               8/21/2022
    Original Author:    Tanner Mathew Utz

    Description:
                        This is the global variable decloration for all the scripts of PAUL
    Credited Links:  
                        N/A
'''
def initialize():

    # Global Declorations
    global startTime
    global stopTime
    global elapsedTime
    global stopWatchVerbs
    global stopWatchNouns

    # Variable Initializations
    startTime = 0
    stopTime = 0
    elapsedTime = 0
    stopWatchVerbs = ['start', 'stop', 'begin']
    stopWatchNouns = ['stopwatch', 'timer', 'clock']

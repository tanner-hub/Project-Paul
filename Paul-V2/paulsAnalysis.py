'''
paulsAnalysis.py

    Current Author:     Tanner Mathew Utz
    Date:               8/18/2022
    Original Author:    Tanner Mathew Utz

    Description:
                        This script is intended to handle the concept of choice selection for the flow in pauls brain
    Credited Links:  
                        N/A
'''
from urllib.parse import _NetlocResultMixinStr
import paulsWatch
import paulsMemory

stopWatchInstance = paulsWatch.StopWatch()

class Analysis:

    # This function just searches its param for a verb in the global list
    def findVerb(self, strIn):
        wordArr = strIn.split()
        for word in wordArr:
            if word in paulsMemory.stopWatchVerbs:
                print('I have detected a Verb: ', word)
                return word
        print('No noun has been detected')
        return ''

    # This function just searches its param for a noun in the global list
    def findNoun(self, strIn):
        wordArr = strIn.split()
        for word in wordArr:
            if word in paulsMemory.stopWatchNouns:
                print('I have detected a Noun: ', word)
                return word
        print('No noun has been detected')
        return ''

    def makeDecision(self, strIn):

        returnStr = ''
        
        verb = self.findVerb(strIn)
        noun = self.findNoun(strIn)

        # Prob for the object we can utilize - then when its understood prob for what we can do with that object
        if noun in paulsMemory.stopWatchNouns:
            if verb == paulsMemory.stopWatchVerbs[0]:
                print('This is a thing we can do. The noun is ', noun, '. The verb is ', verb, '.')

        return returnStr

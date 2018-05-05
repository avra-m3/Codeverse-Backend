##
# This class is responsible for instantiating the sphere engine python client
#
# Using this class eliminates the need to deal with sphere engine calls and logic
# and makes easier to focus on the functional requirements
#
# Usage: see bottom of file
# 
##
import config as cfg #config.py
from sphere_engine import CompilersClientV3

class Submission:

    # sphere engine API client
    client = CompilersClientV3(cfg.accessToken, cfg.endpoint)

    # Begin processing a given piece of code with some input
    # @param source         : code to be executed
    # @param input          : provided as stdin to the source code
    # @param lang (optional): default python, more codes below:
    # https://sphere-engine.com/docs/other/languages
    
    # @return submissionId  : unique identifier of sphere engine submission

    @classmethod
    def processSubmission(self, source, input, lang=4):

        # The result needs time to be processed
        response = Submission.client.submissions.create(source, lang, input)

        challengeId = response['id']

        # for now we want to keep track of a challengeId
        if not challengeId > 0: 
            print 'Submission was not uploaded successfully'

        return challengeId

    # Get the result of a particular submission
    # @param submissionId    : submissionId of a previous submission
    #
    # @return (success, stdout, stderr, time, memory)
    @classmethod
    def getSubmissionResult(self, submissionId):
        
        response = self.client.submissions.get(submissionId, with_output=True, with_stderr=True)

        if response['status'] == 0:
            success = True
        else:
            success = False

        return (
            success,
            response['output'],
            response['stderr'],
            response['time'],
            response['memory']
        )
        


if __name__ == "__main__":

    # sample submissions for testing
    print Submission.getSubmissionResult(68637730)

    print Submission.getSubmissionResult(68637726)

    source = '''
    import sys

    def plusfive(a):
        return a+5

    print sys.stdin
    data = sys.stdin.readlines()
    print plusfive(3)
    '''
    testinput = 135

    # Test submission, dont use up our free compiles!!
    # challengeId = Submission.processSubmission(source, testinput)


    # some sort of timeout thing...
    # success, stdout, stderr, time, memory = Submission.getSubmissionResult(challengeId)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """Create a survey and set a responses for use in all test methods"""
        question = "what language did you learn to speak first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
        #each of the responses is prefixed by self, so you can use it
        #anywhere in the class.
        
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
        
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)  
unittest.main()
import unittest
import main
class BasicTests(unittest.TestCase):

    #Testing News Search Api
    def NewsSearchApiReq(self):
        result=main.NewsSearchApiReq("Quatar")
        self.assertNotEqual(result,[])
    
    #Testing Reddit News Search Api
    def RedditSearchApiReq(self):
        result=main.RedditSearchApiReq("Quatar")
        self.assertNotEqual(result,[])
    
    #Testing Reddit News Api
    def RedditApiReq(self):
        result=main.RedditApiReq()
        self.assertNotEqual(result,[])
    
    #Testing News Api
    def NewsApiReq(self):
        result=main.NewsApiReq()
        self.assertNotEqual(result,[])
        
 
if __name__ == "__main__":
    unittest.main()
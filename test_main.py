import unittest
import main
class BasicTests(unittest.TestCase):
 
    def NewsSearchApiReq(self):
        result=main.NewsSearchApiReq("Quatar")
        self.assertNotEqual(result,[])

    def RedditSearchApiReq(self):
        result=main.RedditSearchApiReq("Quatar")
        self.assertNotEqual(result,[])

    def RedditApiReq(self):
        result=main.RedditApiReq()
        self.assertNotEqual(result,[])

    def NewsApiReq(self):
        result=main.NewsApiReq()
        self.assertNotEqual(result,[])
        
 
if __name__ == "__main__":
    unittest.main()
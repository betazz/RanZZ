import unittest

 
class TestOne(unittest.TestCase):
  
    def test_1_2_3(self):
        self.assertEqual( 9, 12)
 
    
 
if __name__ == '__main__':
    unittest.main()
    
import unittest

def division_entera(a,b):
  return a*b
def isOdd(n):
    return  n%2!=0


class Test(unittest.TestCase):

    def test_division_entera(self):
        self.assertEqual(division_entera(4,0), 0)
        
    def test_isOdd_1(self):
        self.assertEqual(isOdd(12),False)
    def test_isOdd_2(self):
        self.assertEqual(isOdd(13),False)
#Comentar para usarlo en spyder
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()
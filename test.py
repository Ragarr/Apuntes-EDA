from examenes.parcial_1_2020.dato_Slist import SList

class SList2(SList):
   
    def removeSmaller(self, x):
        
        prev = None
        node = self.head

        while node!=None:     
            if node.elem < x:
               #borrar el nodo node 
                if node == self.head: #prev==None
                    self.head = self.head.next
                else:
                    prev.next = node.next
                    node=prev
                self.size -= 1

                

            prev = node
            node = node.next

import unittest

class Test(unittest.TestCase):
    def setUp(self):
      
      self.x1=0
      self.input=SList2()
      self.output1=SList2()
      
      for e in [7,3,2,10,0,2,8,0,0,4,1,1,10,6,0,3,0,5,3,1]:
        self.input.addLast(e)
        self.output1.addLast(e)

      self.x2=8
      self.output2=SList2()
      for e in [10,8,10]:
        self.output2.addLast(e)
    
      self.x3=100

    def test_removeSmaller1(self):
      print()
      print('Caso 1: borramos menores que ', self.x1,' en una lista vacía')
      lEmpty=SList2()
      lEmpty.removeSmaller(self.x1)
      self.assertEqual(len(lEmpty),0)
     
    def test_removeSmaller2(self):
      print()
      print('Caso 2: no existen valores menores a ', self.x1, 'en la lista')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x1)
      print('Después:',self.input)
      print('Lista esperada:',self.output1)
      self.assertEqual(len(self.input),len(self.output1))

      for i in range(len(self.input)):
        self.assertEqual(self.input.getAt(i),self.output1.getAt(i))

    def test_removeSmaller3(self):
      print()
      print('Caso 3: si existen menores que ', self.x2, ' en la lista')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x2)
      print('Después:',self.input)
      print('Lista esperada:',self.output2)
      print()
      self.assertEqual(len(self.input),len(self.output2))

      for i in range(len(self.input)):
        self.assertEqual(self.input.getAt(i),self.output2.getAt(i))

    def test_removeSmaller4(self):
      print()
      print('Caso 4: todos son menores que ', self.x3, '')
      print('Antes de llamar a removeSmaller: ', self.input)
      self.input.removeSmaller(self.x3)
      print('Después:',self.input)
      print('Lista esperada:',SList2())
      print()
      self.assertEqual(len(self.input),0)

    

#Comentar para usarlo en spyder
#unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()

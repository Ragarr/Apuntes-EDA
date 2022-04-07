# -*- coding: utf-8 -*-

# Raúl Aguilar Arroyo

class DNode:
  def __init__(self,elem,next=None,prev=None ):
    self.elem = elem
    self.next = next
    self.prev = prev
    
class MyDList():  
    
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
     
    def append(self,e):
        """Add a new element, e, at the end of the list"""
        #create the new node
        newNode=DNode(e)
        
        if self._size==0:
            self._head=newNode
        else:
            newNode.prev=self._tail
            self._tail.next=newNode
        
        #update the reference of head to point the new node
        self._tail=newNode
        #increase the size of the list  
        self._size+=1
        
    def __len__(self):
        return self._size
    
    
   
    def __str__(self):
        """Returns a string with the elements of the list"""
        nodeIt=self._head
        result='['
        while nodeIt:
            result+= str(nodeIt.elem)+ ", "
            nodeIt=nodeIt.next
        
        if len(result)>1:
            result=result[:-2]

        result+=']'
        return result


    def removeSmaller(self, x):
        """removes those nodes whose elements are lower than x"""
        current=self._head
        while current:
            if current.elem<x:
                if current.prev and current.next: # ni primer ni ultimo elemento
                    current.prev.next=current.next
                    current.next.prev=current.prev
                    self._size-=1
                elif current.prev: # es el ultimo
                    current.prev.next=current.next
                    self._tail= current.prev
                    self._size-=1
                elif current.next: # es el primero
                    self._head = current.next
                    current.next.prev=current.prev
                    self._size-=1
                else: # es el unico elemento
                    self._head=None
                    self._tail=None
                    self._size=0
            current=current.next


    
# In[9]:

import random 
l = MyDList()
#for i in range(20):
for i in [7,3,2,10,11,0,2,8,0,0,4,1,1,10,12,6,0,3,0,5,3,7]:
    l.append(i)
    

    
print("Original list:\n",l)
value=8
l.removeSmaller(value)
print("Eliminar elementos menores a {}:\n{}".format(value, l))

print("Original list:\n",l)
value=12
l.removeSmaller(value)
print("Eliminar elementos menores a {}:\n{}".format(value, l))

class test():
    def __init__(self ):
        super(test, self).__init__()
        
        
        
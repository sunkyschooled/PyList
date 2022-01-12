import time
import random
class PyList:
    def __init__(self,contents=[], size=10):
        # The contents allows the programmer to construct a list with
        # the initial contents of this value. The initial_size
        # lets the programmer pick a size for the internal size of the 
        # list. This is useful if the programmer knows he/she is going 
        # to add a specific number of items right away to the list.
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        self.appendCount = 0
        
        for e in contents:
            self.append(e)
          
    def __getitem__(self,index):

        if index < self.numItems:
            return self.items[index]
        else:
          raise IndexError("PyList index out of range")
    
    def __setitem__(self,index,val):
        raise NotImplementedError
        if index < self.numItems:
            self.items[index] = val
            return
        raise IndexError("PyList assignment index out of range")
    
    def insert(self,index,item):
        if self.numItems == self.size:
            self.__makeroom()
           
        if index < self.numItems:
            for n in range(self.numItems-1, index-1,-1):
                self.items[n+1] = self.items[n]
            self.numItems += 1
            self.items[index] = item
            return
        else:
            self.append(item)
            return
            
    def currentAppendCount(self):
      return self.appendCount
    def resetAppendCount(self):
      self.appendCount = 0

    def __add__(self,other):
        result = PyList()
        
        for i in range(self.numItems):
            result.append(self.items[i])
            pass
            
        for i in range(other.numItems):
            result.append(other.items[i])
            pass
            
        return result
    
    
    def __contains__(self,item):
        for i in range(self.numItems):
            if self.items[i] == item:
              return True
            pass

        return False
    
    def __delitem__(self,index):
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1 # same as writing self.numItems = self.numItems - 1
            
    def __eq__(self,other):
        if type(other) != type(self):
            return False
        
        if self.numItems != other.numItems:
            return False
        
        for i in range(self.numItems):
          if self.items[i] == other.items[i]:
            pass
          else:
            return False
            
        return True
  
    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]  
            
    def __len__(self):
        return self.numItems
    
    # This method is hidden since it starts with two underscores. 
    # It is only available to the class to use. 
    def __makeroom(self):
        # increase list size by 1/4 to make more room.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]
            
        self.items = newlst
        self.size = newlen        

    def append(self,item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1
        self.appendCount += 1
        pass

    def __str__(self):
        s = "["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "]"
        return s
    
    def __repr__(self):
        s = "PyList(["
        for i in range(self.numItems):
            s = s + str(self.items[i])
            if i < self.numItems - 1:
                s = s + ", "
        s = s + "])"
        return s        
            
    def sort(self):
        pass
    def swap(self, index1, index2):
      if index1 >= self.numItems:
        raise IndexError("PyList index out of range")
      if index2 >= self.numItems:
        raise IndexError("PyList index out of range")
      if index1 == index2:
        return


      item = self[index1]
      self[index1] = self[index2]
      self[index2] = item

    def bubbleSort(self):
      while not self.sorted():
        for i in range(self.numItems-1):
          if self[i] > self[i+1]:
            self.swap(i,i+1)
    def maxIndex(self,last=-1):
        if last < 0:
            last = self.numItems + last
        index = 0
        for i in range(last + 1):
            if self[i] > self[index]:
                index = i
        return index
    def insertionSort(self):
      for i in list(range(self.numItems))[::-1]:
        maxI = self.maxIndex(i)
        maxE = self[maxI]
        del self[maxI]
        self.insert(i,maxE)
      return self

    def sorted(self):
      for i in range(self.numItems-1):
        if self[i]>self[i+1]:
           return False
      return True           

    def merge(self,other):
      merger= []
      PyMerger = PyList(merger)
      for i in range(self.numItems + other.numItems):
        if (self.numItems-1) < i:
          PyMerger.append(other[i])
        elif (other.numItems-1) < i:
          PyMerger.append(self[i])
        else:
          if self.items[i] < other.items[i]:
            PyMerger.append(self.items[i])
            other.insert(0,0)
          else:
            PyMerger.append(other[i])
            self.insert(0,0)
      return PyMerger


      
      
def main():
    lst = PyList()
    
    for i in range(100):
        lst.append(i)
    
    lst2 = PyList(lst)
    
    print(lst)
    print(lst2)
    
    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
    
    lst3 = lst + lst2
    
    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        
    
    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")        
    
    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")        
    
    del lst[1]
    
    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")        
    
    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")        
        
    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")        
    
    del lst2[2]
    
    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")  
        
    
    lst4 = PyList(lst)
    lst.insert(0,100)
    lst4 = PyList([100]) + lst4
    
    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")
        
    lst.insert(1000,333)
    lst4.append(333)

    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")  
        
    print(lst)
    print(lst4)

if __name__ == "__main__":
    pass
def reverseTest():
  f = open("random.csv", "w")
  lhst = []
  for i in range(1,1001):
    lhst.append(int(1001-i))
    lesht = PyList(lhst)
    thime = time.thread_time()
    lesht.insertionSort()
    thime = time.thread_time()-thime
    f.write("{},{}\n".format(i,thime))
    print(i)
  f.close()
lyest = [1,2,3,4,5,6,7,8,9]
ljest = [0,3,5,6,7,8.5,9.1,13]
lyest2 = PyList(lyest)
ljest2 = PyList(ljest)
print(lyest2.merge(ljest2))
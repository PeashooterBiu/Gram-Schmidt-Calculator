#This is a GramSchmidt Calculator
#Created: 10/19/2022
#Author: Sijing Zhu

import math

'''GramSchmidt class holds the methods for gram schmidt process'''
class GramSchmidt:

    # default constructor that does nothing
    def __init__(self) -> None:
        pass


    '''return the euclidean length of the tuple'''
    def size(self, v1):
        sum = 0
        for i in range(len(v1)):
            sum += v1[i]* v1[i]
        return (math.sqrt(sum))


    '''return the dot product of given two tuples'''
    def dotProduct(self, v1, v2):
        sum = 0 
        for i in range(len(v1)):
            sum += (v1[i] * v2[i])
        return sum


    '''add the given two tuples'''
    def add(self, v1, v2):
        v = []
        for i in range(len(v1)):
            v.append(v1[i] + v2[i])            
        return v
    

    '''substract the given two tuples'''
    def substract(self, v1, v2):
        v = []
        for i in range(len(v1)):
            v.append(v1[i] - v2[i])            
        return v


    '''scale the given tuple by given scale factor'''
    def scale(self, a, v1):
        v = []
        for i in range(len(v1)):
            v.append(a * v1[i])            
        return v


    '''return orthogonal projection of Z with respect to given orthonormal list'''
    def orthoProjection(self, Z, vlist):
        v = [0]*len(vlist[0])
        for i in range(len(vlist)):
            c = self.dotProduct(vlist[i], Z)
            xi = self.scale(c, vlist[i])
            v = self.add(xi, v)
        return v


    '''compare two tuples and see if they are equal (compare up to 5 digits)'''
    def compareList(self, v1, v2):
        if (len(v1) != len(v2)):
            return False
        for i in range(len(v1)):
            if round(v1[i], 5) != round(v2[i], 5) :
                return False
        return True

    
    '''determine whether Z is a linear combination of the given orthonormal list'''
    '''vlist must be orthonormal list'''
    def isLinearCombo(self, Z, vlist):
        if self.compareList(Z, self.orthoProjection(Z, vlist)):
            return True
        return False


    '''determine whether the given tuple is nil'''
    def isNil(self, v1):
        for i in v1:
            if i != 0:
                return False
        return True


    '''create a nill tuple with n terms'''
    def Nil(self, n):
        v = []
        for i in range(n):
            v.append(0)
        return v


    '''normalize the given tuple if the tuple is not nill'''
    def normalize(self, v1):
        if self.isNil(v1) == False:
            return self.scale(1 / self.size(v1), v1)
        return v1


    '''orthogonalize the given list and return the new list'''
    def orthogonalize(self, vlist):
        #number of rows:
        n = len(vlist[0])
        
        #if the first column is a nil tuple, the return None
        if self.isNil(vlist[0]):
            return None

        #append the normalized first column 
        orthoList = []
        orthoList.append(self.normalize(vlist[0]))

        # loop through all the rest of the columns
        for i in range(1, len(vlist)):

            # if a column is a linear combination of the previous ones, add a nil tuple
            if self.isLinearCombo(vlist[i], orthoList[0: (i)]):
                orthoList.append(self.Nil(n))

            # if not, then append normalized (Z - ortho projection) 
            else:
                x = self.substract(vlist[i], self.orthoProjection(vlist[i], orthoList[0: (i)]))
                w = self.normalize(x)
                orthoList.append(w)
        
        # round each number in the orthoList
        for i in range(len(orthoList)):
            for j in range(len(orthoList[0])):
                orthoList[i][j] = round(orthoList[i][j],2)

        return orthoList



    '''transpose the given matrix'''
    def transpose(self, vlist):
        new = []
        for i in range(len(vlist[0])):
            v = []
            for j in range(len(vlist)):
                v.append(vlist[j][i])
            new.append(v)
        return new


    '''print the matrix as columns'''
    def toString(self, vlist):
        for i in vlist:
            print(i)
        print("\n")




'''main method that calls the calculation'''
if __name__ == '__main__':
    list1 = [[-3,-2,4,3,1,2],[1,-5,3,1,3,-2], [4,-1,2,-2,4,1],[8,2,5,-6,-2,-13],[0,5,5,-1,-2,0],[-3,3,-3,-3,-2,2]]
    list2 = [[-1,-5,-5,3,2,-3,2],[5,-5,-5,1,4,3,5],[7,5,5,-5,0,9,1],[-2,-1,5,2,5,5,1],[3,-4,4,-1,2,2,1]]
    list3 = [[1,-2,0,5],[-4,1,5,-1],[-8,7,12,5],[0,4,-1,-4],[-2,-1,-3,1],[-2,1,4,1]]

    test = [[1,2],[3,4],[5,6]]
    
    g1 = GramSchmidt()

    c1 = g1.orthogonalize(list1)
    c2 = g1.orthogonalize(list2)
    c3 = g1.orthogonalize(list3)

    g1.toString(c1)
    g1.toString(c2)
    g1.toString(c3)
    print(g1.transpose(test))

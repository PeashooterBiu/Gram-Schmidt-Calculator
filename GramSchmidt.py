from math import sqrt
from tokenize import Double


class GramSchmidt:

    def __init__(self) -> None:
        pass

    def size(self, v1):
        sum = 0
        for i in range(len(v1)):
            sum += v1[i]**2
        return (sqrt(sum))


    def dotProduct(self, v1, v2):
        sum = 0 
        for i in range(len(v1)):
            sum += (v1[i] * v2[i])
        return sum


    def add(self, v1, v2):
        v = []
        for i in range(len(v1)):
            v.append(v1[i] + v2[i])            
        return v
    

    def substract(self, v1, v2):
        v = []
        for i in range(len(v1)):
            v.append(v1[i] - v2[i])            
        return v


    def scale(self, a, v1):
        v = []
        for i in range(len(v1)):
            v.append(a * v1[i])            
        return v


    def orthoProjection(self, Z, vlist):
        v = [0]*len(vlist[0])
        
        for i in range(len(vlist)):
            c = self.dotProduct(vlist[i], Z)
            xi = self.scale(c, vlist[i])
            v = self.add(xi, v)
        return v


    def compareList(self, v1, v2):
        if (len(v1) != len(v2)):
            return False
        for i in range(len(v1)):
            if v1[i] != v2[i]:
                return False
        return True

    
    def isLinearCombo(self, Z, vlist):
        if self.compareList(Z, self.orthoProjection(Z, vlist)):
            return True
        else:
            return False


    def isNil(self, v1):
        for i in v1:
            if i != 0:
                return False

    def Nil(self, n):
        v = []
        for i in range(n):
            v.append(0)
        return v


    def normalize(self, v1):
        if self.isNil(v1) == False:
            return self.scale(1 / self.size(v1), v1)
        return v1


    def extension(self, vlist):
        #number of rows:
        n = len(vlist[0])
        
        if self.isNil(vlist):
            return None
        orthoList = []
        orthoList.append(self.normalize(vlist[0]))

        for i in range(1, len(vlist)):
            if self.isLinearCombo(vlist[i], vlist[0: (i)]):
                orthoList.append(self.Nil(n))
            else:
                x = self.substract(vlist[i], self.orthoProjection(vlist[i], vlist[0: (i)]))
                w = self.normalize(x)
                orthoList.append(w)
        
        return orthoList



if __name__ == '__main__':
    ortho = [[1,0,0],[2,0,0],[0,1,0],[0,0,1]]
    ortho2 = [[1,2,3],[4,5,6],[7,8,9]]
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    list3 = [3, 4, 5]
    
    g1 = GramSchmidt()

    #print(g1.orthoProjection([1,2,3], ortho))
    print(g1.extension(ortho))
    # print(g1.compareList(list3,list2))
    # print(g1.isLinearCombo(list1, ortho))

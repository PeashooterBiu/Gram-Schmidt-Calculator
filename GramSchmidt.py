import math


class GramSchmidt:

    def __init__(self) -> None:
        pass

    def size(self, v1):
        sum = 0
        for i in range(len(v1)):
            sum += v1[i]* v1[i]
        return (math.sqrt(sum))


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
            if round(v1[i], 3) != round(v2[i], 3) :
                return False
        return True

    
    def isLinearCombo(self, Z, vlist):
        if self.compareList(Z, self.orthoProjection(Z, vlist)):
            return True
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
        
        if self.isNil(vlist[0]):
            return None
        orthoList = []
        orthoList.append(self.normalize(vlist[0]))

        for i in range(1, len(vlist)):
            # if len(orthoList) >= len(vlist[0]):
            #     orthoList.append(self.Nil(n))
            if self.isLinearCombo(vlist[i], orthoList[0: (i)]):
                orthoList.append(self.Nil(n))
            else:
                x = self.substract(vlist[i], self.orthoProjection(vlist[i], orthoList[0: (i)]))
                w = self.normalize(x)
                orthoList.append(w)
        
        for i in range(len(orthoList)):
            for j in range(len(orthoList[0])):
                orthoList[i][j] = round(orthoList[i][j],3)

        return orthoList


    def toString(vlist):
        



if __name__ == '__main__':
    ortho = [[-3,-2,4,3,1,2],[1,-5,3,1,3,-2], [-3,3,-3,-3,-2,2], [4,-1,2,-2,4,1],[8,2,5,-6,-2,-13],[0,5,5,-1,-2,0]]
    st = [[1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,0,0,1,0], [0,0,0,0,0,1]]
    st2 = [[2,0,0,0,0,1], [0,3,0,0,0,1], [0,0,4,0,1,0], [0,0,0,2,0,1], [0,3,0,0,4,0], [0,1,0,0,0,2]]
    ortho2 = [[1,2,3],[2,3,4], [2,4,6], [10,11,12]]
    asdf = [[1,2,3],[1,2,4],[1,5,3],[0,0,3]]
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    list3 = [3, 4, 5]
    
    
    g1 = GramSchmidt()

    c = g1.extension(ortho)
    print(c)

    # print(g1.isLinearCombo([1,2,3,4,5,6], c))
    #print(g1.orthoProjection([1,2,3], ortho))
    # print(g1.compareList(list3,list2))
    # print(g1.isLinearCombo(list1, ortho))

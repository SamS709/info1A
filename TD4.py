import matplotlib.pyplot as plt
import numpy as np
class Hashtable:

    def __init__(self, hash, N):
        self.N = N
        self.hash = hash
        self.table = [[] for i in range(self.N)]
        self.tot = 0

    def put(self,key,value):
        if self.tot>=1.2*self.N:
            self.resize()
        ind = self.hash(key)%self.N
        set_ = self.table[ind]
        for i in range(len(set_)):
            [k,v] = set_[i]
            if key == k:
                set_[i]=[k,value]
                return
        set_.append([key,value])
        self.tot +=1

    def get(self,key):
        ind = self.hash(key)%self.N
        set_ = self.table[ind]
        for [k,v] in set_:
            if key==k:
                return v

    def repartition(self):
        y = [len(set_) for set_ in self.table]
        x = np.linspace(0,self.N-1,self.N)
        print(x)
        plt.figure()
        plt.bar(x,y,width=0.5)
        plt.show()

    def resize(self):
        table = self.table.copy()
        self.N = 2*len(table)
        self.table = [[] for i in range(self.N)]
        for set_ in table:
            for [k,v] in set_:
                self.put(k,v)



if __name__ == '__main__':
    def hash(c):
        h = 0
        for i in c:
            h += ord(i)
        return h

    def hash2(c):
        h=0
        for c in key:
            h += ord(c)
            h += (h << 10)
            h ^= (h >> 6)
        h += (h << 3)
        h ^= (h >> 11)
        h += (h << 15)
        return h

    '''print(hash('abc'))
    print(hash('abcde')%6)

    hashtable = Hashtable(hash,6)
    hashtable.table = [[], [], [], [['ab', 4]], [], []]
    hashtable.put('abcde',3)
    print(hashtable.table)
    print(hashtable.get("abcd"))
    hashtable.repartition()'''
    L = open("mots.sansaccent.txt", "r").read().splitlines()
    hashtable1 = Hashtable(hash,100)
    for word in L:
        key,val = word, len(word)
        hashtable1.put(key,val)
        print(hashtable1.N)
    hashtable1.repartition()


import numpy as np

class Polynomial:

    def __init__(self,L):
        self.coeffs = L

    def __str__(self):
        l = len(self.coeffs)
        cond0 = self.coeffs[l - 1] != 0
        s=""
        if l !=0:
            if cond0:
                s = str(self.coeffs[l - 1]) + " "
        else:
            return "0"
        if l >=1:
            plus = ""
            if self.coeffs[l - 1] != 0:
                plus = " + "
            coeff = self.coeffs[l - 2]
            if coeff != 0 and coeff != 1:
                s = str(coeff)+"*X "+plus+s
            if coeff == 1:
                s = "X "+plus+s
        for i in range(2,l):
            coeff = self.coeffs[l - 1 - i]
            if coeff != 1 and coeff != 0:
                s = str(coeff)+"*X^"+str(i)+" + " + s
            if coeff == 1:
                s = "X^"+str(i)+" + " + s
        return s

    def add(self,L2):
        L1 = self.coeffs.copy()
        L = []
        a = 0
        if len(L1)>= len(L2):
            L = L1
        else:
            L = L2
            a = 1
        if a == 0:
            for i in range(len(L2)):
                L[len(L1)-1-i] = L[len(L1)-1-i] + L2[len(L2)-1-i]
        else:
            for i in range(len(L1)):
                L[len(L2)-1-i] = L[len(L2)-1-i] + L1[len(L1)-1-i]
        return Polynomial(L)


    def scalar(self,c):
        array = np.array(self.coeffs).copy()
        array = c*array
        return Polynomial(array)


class Z(Polynomial):

    def __init__(self,L,q,n):
        super().__init__(L)
        self.n = n
        self.q = q
        self.init_coeffs = self.coeffs.copy()
        L = []
        for coeff in self.coeffs:
            L.append(coeff%q)
        self.coeffs=L.copy()
        self.verif_deg()

    def scalar(self,c):
        L = [(c*coeff)%self.q for coeff in self.coeffs]
        return Polynomial(L)

    def verif_deg(self):
        if len(self.coeffs)>=self.n+1:
            return False

    def rescale(self,r):
        return Z(self.init_coeffs,r,self.n)

    def add(self,Zqn):
        assert self.q == Zqn.q and self.n == Zqn.n
        L = [(self.coeffs[i]+Zqn[i])for i in range(self.n)]
        return Polynomial(L)


if __name__ == "__main__":
    P = Polynomial([1,4,2])
    print(P.__str__())
    print(P.add([4,5]))
    print(P.scalar(2))
    z = Z([2,5,6],2,5)
    print(z)
    print(z.rescale(2))
    print(2%2,5%2,6%2)


class T:

    def __init__(self,label,*children):
        self.label = label
        self.children = children
        self.nb_children = len(children)

    def child(self,i):
        return T(self.children[i])

    def is_leaf(self):
        if self.children == ():
            return True
        return False

    def depth(self,children_ = 0,s=0):
        depth_ = 0
        if children_ == 0:
            children_ = self.children
        if len(children_)==0:
            return s
        for child in children_:
            val = self.depth(child.children,s+1)
            if val >= depth_:
                depth_ = val
        return depth_

    def __str__(self):
        string = ""
        if len(self.children)==0:
            return self.label
        for child in self.children:
            string += child.__str__()+','
        string= string[:-1]
        return str(self.label)+'('+string+')'

    def __eq__(self, other):
        if self.__str__()==other.__str__():
            return True
        else:
            return False

    def deriv(self,var):
        if len(self.children) != 0:
            if len(self.children[0].children)==0 and len(self.children[1].children)==0:
                if self.label == "*":
                    cond1 = not self.children[0].label == var
                    cond2 = not self.children[1].label == var
                    if cond1 and cond2:
                        self.children[0].label = '0'
                        self.children[1].label = '0'
                    if self.children[0].label == var:
                        if self.children[1].label == var:
                            self.children[0].label = '2'
                            self.children[1].label = var
                        else:
                            print(1)
                            self.children[0].label = '1'
                    if self.children[1].label == var:
                        if self.children[0].label == var:
                            self.children[0].label = '2'
                            self.children[1].label = var
                        else:
                            self.children[0].label = '1'
                if self.label == "+":
                    print(2)
                    if self.children[0].label == var:
                        self.children[0].label = '1'
                    else:
                        self.children[0].label = '0'
                    if self.children[1].label == var:
                        self.children[1].label = '1'
                    else:
                        self.children[1].label = '0'
            else:
                self.children[0].deriv(var)
                self.children[1].deriv(var)











if __name__=="__main__":

    a = '+'
    b = '*'
    poly = T(a,T('7'),T(a,T(b,T('X'),T('5')),T(b,T('X'),T(a,T('X'),T('3')))))
    poly.deriv('X')

    print(poly.__str__())
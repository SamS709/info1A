class Tree:
    def __init__(self, label, *children):
        self._label = label
        self._children = tuple(children)

    def label(self):
        return self._label

    def children(self):
        return self._children

    def nb_children(self):
        return len(self._children)

    def child(self, i):
        return self._children[i]

    def is_leaf(self):
        return len(self._children) == 0
    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max(child.depth() for child in self._children)
    def __str__(self):
        if self.is_leaf():
            return self._label
        return f"{self._label}({','.join(str(child) for child in self._children)})"

    def __eq__(self, other):
        if not isinstance(other, Tree):
            return False
        return self._label == other._label and self._children == other._children
    def deriv(self, var):
        if self.is_leaf():
            return Tree('1') if self._label == var else Tree('0')
        if self._label == '+':
            return Tree('+', *(child.deriv(var) for child in self._children))
        if self._label == '*':
            # Produit dérivé: u'v + uv'
            u, v = self._children
            return Tree('+',
                        Tree('*', u.deriv(var), v),
                        Tree('*', u, v.deriv(var)))
        return Tree('0')
    def substitute(self, t1, t2):
        if self == t1:
            return t2
        return Tree(self._label, *(child.substitute(t1, t2) for child in self._children))
    def simplify(self):
        if self.is_leaf():
            return self

        simplified_children = [child.simplify() for child in self._children]

        if self._label == '+':
            # simplifications arithmétiques
            if simplified_children == [Tree('0'), simplified_children[1]]:
                return simplified_children[1]
            if simplified_children == [simplified_children[0], Tree('0')]:
                return simplified_children[0]
            if all(child.is_leaf() and child._label.isdigit() for child in simplified_children):
                val = sum(int(child._label) for child in simplified_children)
                return Tree(str(val))

        if self._label == '*':
            if Tree('0') in simplified_children:
                return Tree('0')
            if Tree('1') in simplified_children:
                return next(child for child in simplified_children if child != Tree('1'))
            if all(child.is_leaf() and child._label.isdigit() for child in simplified_children):
                val = 1
                for child in simplified_children:
                    val *= int(child._label)
                return Tree(str(val))

        return Tree(self._label, *simplified_children)
    def eval(self, var, value):
        substituted = self.substitute(Tree(var), Tree(str(value)))
        simplified = substituted.simplify()
        return simplified
    def to_infix(self):
        if self.is_leaf():
            return self._label
        elif self.nb_children() == 2:
            return f"({self._children[0].to_infix()} {self._label} {self._children[1].to_infix()})"
        else:
            return f"{self._label}({', '.join(child.to_infix() for child in self._children)})"


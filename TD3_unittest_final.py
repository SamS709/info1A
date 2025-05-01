import unittest
from TD3_final import Tree  # Assure-toi que la classe Tree est dans un fichier nommé tree.py

class TestTree(unittest.TestCase):

    def test_basic_methods(self):
        t = Tree('a')
        self.assertEqual(t.label(), 'a')
        self.assertTrue(t.is_leaf())
        self.assertEqual(t.nb_children(), 0)

        t2 = Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(t2.label(), 'f')
        self.assertEqual(t2.nb_children(), 2)
        self.assertFalse(t2.is_leaf())
        self.assertEqual(t2.child(0), Tree('a'))

    def test_str_and_eq(self):
        t1 = Tree('f', Tree('a'), Tree('b'))
        t2 = Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(str(t1), 'f(a,b)')
        self.assertEqual(t1, t2)

    def test_depth(self):
        t = Tree('f', Tree('a'), Tree('g', Tree('b')))
        self.assertEqual(t.depth(), 2)

    def test_deriv(self):
        expr = Tree('+',Tree('+',
                    Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                    Tree('*', Tree('5'), Tree('X'))),Tree('7'))
        derived = expr.deriv('X')
        self.assertEqual(str(derived), '+(+(+(*(0,*(X,X)),*(3,+(*(1,X),*(X,1)))),+(*(0,X),*(5,1))),0)')  # structure attendue (non simplifiée)

    def test_substitution(self):
        expr = Tree('+', Tree('a'), Tree('X'))
        substituted = expr.substitute(Tree('X'), Tree('b'))
        self.assertEqual(str(substituted), '+(a,b)')

    def test_simplify(self):
        expr = Tree('+', Tree('X'), Tree('0'))
        self.assertEqual(expr.simplify(), Tree('X'))

        expr2 = Tree('*', Tree('0'), Tree('X'))
        self.assertEqual(expr2.simplify(), Tree('0'))

        expr3 = Tree('+', Tree('3'), Tree('4'))
        self.assertEqual(expr3.simplify(), Tree('7'))

    def test_eval(self):
        expr = Tree('+',Tree('+',
                    Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                    Tree('*', Tree('5'), Tree('X'))),Tree('7'))

        evaluated = expr.eval('X', 2)
        print(evaluated)
        self.assertEqual(evaluated, Tree('29'))  # 3*2² + 5*2 + 7 = 12 + 10 + 7 = 29

    def test_to_infix(self):
        expr = Tree('+', Tree('X'), Tree('3'))
        self.assertEqual(expr.to_infix(), '(X + 3)')


if __name__ == '__main__':
    unittest.main()

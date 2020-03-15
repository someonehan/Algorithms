from .LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left = None, right = None):
        """Create an expression tree.
        In a single parameter form, token should be a leaf value(eg '42') and the expression tree will have that value at an isolated node

        In a tree parameter version,token should be an operator, and left and right should be existing expressiontree instance that become
        the operands for the binary operator 
        """
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in '+-*/':
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        """return string representation of the expression"""
        pieces = []
        self._parenthesize(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize(self.left(p), result)
            result.append(str(p.element()))
            self._parenthesize(self.right(p), result)
            result.append(')')

    def evaluate(self):
        """return the numeric result of the expression"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """ Return the numeric result of subtree rooted p"""
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_value = self._evaluate_recur(self.left(p))
            right_value = self._evaluate_recur(self.right(p))
            return eval(str(left_value) + str(op) + str(right_value))

        
def build_expression_tree(tokens):
    """ Return an expression tree based upon by a tokenized expression"""    
    S = []
    for token in tokens:
        if token in '+-*/':
            S.append(token)
        elif token not in '()':
            S.append(ExpressionTree(token))
        elif token == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()
import unittest
from src.DataStructure.Tree import build_expression_tree

class Test_BuildExpressionTree(unittest.TestCase):
    def test_buildExpressionTree_plus(self):
        ret = build_expression_tree("(1+1)")
        print(ret)
        print(ret.is_empty())

if __name__ == "__main__":
    unittest.main()
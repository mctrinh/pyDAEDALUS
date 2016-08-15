from StringIO import StringIO
from unittest import TestCase

sample_ply_file = """ply
format ascii 1.0
element vertex 12
property float32 x
property float32 y
property float32 z
element face 20
property list uint8 int32 vertex_indices
end_header
0.000000 0.000000 1.176000
1.051000 0.000000 0.526000
0.324000 1.000000 0.525000
-0.851000 0.618000 0.526000
-0.851000 -0.618000 0.526000
0.325000 -1.000000 0.526000
0.851000 0.618000 -0.526000
0.851000 -0.618000 -0.526000
-0.325000 1.000000 -0.526000
-1.051000 0.000000 -0.526000
-0.325000 -1.000000 -0.526000
0.000000 0.000000 -1.176000
3 0 1 2
3 0 2 3
3 0 3 4
3 0 4 5
3 0 5 1
3 1 5 7
3 1 7 6
3 1 6 2
3 2 6 8
3 2 8 3
3 3 8 9
3 3 9 4
3 4 9 10
3 4 10 5
3 5 10 7
3 6 7 11
3 6 11 8
3 7 10 11
3 8 11 9
3 9 11 10
"""


class TestReadingPlyFile(TestCase):
    def test_correct_number_of_nodes_is_parsed(self):
        file = StringIO()
        file.write(sample_ply_file)
        self.fail()

class TestSplitEdge(TestCase):
    def test_ending_node_count(self):
        self.fail()


from statistics import median
from typing import Tuple, List
from collections import namedtuple

class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    def __str__(self) -> str:
        return f'({self.x},{self.y})'
    def __repr__(self) -> str:
        return self.__str__()

class Node:
    def __init__(self, point: Point):
        self.p = point
        self.med = 0.0
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.p)

class PriorityTree:
    def __init__(self, points: List[Point]) -> None:
        if not points:
            self.root = None
        else:
            points = list(sorted(points, key=lambda p: -p[1]))
            self.root = self._create(points)

    def _create(self, points: List[Point]) -> Node:
        if not points:
            return None
        first = points[0]
        n = Node(first)
        n.med = first[0]
        del points[0]
        if points:
            med = median(map(lambda it: it[0], points))
            n.med = med
            Pl = list(filter(lambda it: it[0] <= med, points))
            if Pl:
                n.left = self._create(Pl)
            Pr = list(filter(lambda it: it[0] > med, points))
            if Pr:
                n.right = self._create(Pr)
        return n

    def findSplitNode(self, x: Tuple[float, float]) -> Tuple[Node, list]:
        x_left, x_right = x
        n, path = self.root, []
        while n is not None and (x_left > n.med or x_right < n.med):
            p = n.p
            path.append(p)
            if x_right < n.med:
                n = n.left
            else:
                n = n.right
        return n, path

    def queryPrioritySubtree(self, n: Node, y: float) -> list:
        res = []
        if n is not None and n.p.y >= y:
            res.append(n.p)
            res = res + self.queryPrioritySubtree(n.left, y)
            res = res + self.queryPrioritySubtree(n.right, y)
        return res


def query(tree: PriorityTree, x: Tuple[float, float], y: float) -> List[Point]:
    ret_list_point = []
    qx1, qx2, qy1 = x[0], x[1], y
    splitting_node, node_points = tree.findSplitNode(x)

    for n in node_points:
        if n[0] >= qx1 and n[0] <= qx2 and n[1] >= qy1:
            ret_list_point.append(n)

    if splitting_node is None:
        return ret_list_point

    if splitting_node.left is None and splitting_node.right is None:
        ret_list_point += tree.queryPrioritySubtree(splitting_node, qy1)
    else:
        p_n = splitting_node.p
        if p_n.x >= qx1 and p_n.x <= qx2 and p_n.y >= qy1:
            ret_list_point.append(splitting_node.p)
        n = splitting_node.left

        while n is not None and n.p[1] >= qy1:
            if n.p[0] >= qx1 and n.p[0] <= qx2 and n.p[1] >= qy1:
                ret_list_point.append(n.p)
            if n.p[0] >= qx1 and n.p[0] <= qx2:
                ret_list_point.extend(tree.queryPrioritySubtree(n.right, qy1))
                n = n.left
            else:
                n = n.right

        n = splitting_node.right
        while n is not None and n.p[1] >= qy1:
            if n.p[0] >= qx1 and n.p[0] <= qx2:
                ret_list_point.append(n.p)
                ret_list_point.extend(tree.queryPrioritySubtree(n.left, qy1))
                n = n.right
            else:
                n = n.left

        return ret_list_point
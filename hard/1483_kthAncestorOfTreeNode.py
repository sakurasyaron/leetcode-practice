from typing import List

# TODO Revise

# class Node:
#     def __init__(self, data: int):
#         self.data = data
#         self.parent = None
#
#
# class TreeAncestor:
#
#     def __init__(self, n: int, parent: List[int]):
#         self.root, self.node_dict = self.populateTree(parent)
#         self.total_nodes = n
#
#     def populateTree(self, parent: List[int]) -> Tuple:
#         node_dict = {}
#         root = None
#         for i, elem in enumerate(parent):
#             new_node = Node(i)
#             node_dict[i] = new_node
#             if elem == -1:
#                 root = new_node
#             elif elem in node_dict:
#                 new_node.parent = node_dict[elem]
#         return root, node_dict
#
#     def getKthAncestor(self, node: int, k: int) -> int:
#         tree_node = self.node_dict[node]
#         while k:
#             ancestor = tree_node.parent
#             k -= 1
#             if k == 0 and ancestor:
#                 return ancestor.data
#             elif not ancestor:
#                 break
#             else:
#                 tree_node = ancestor
#         return -1


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.pars = [parent]
        for k in range(self.getLogRange(n)):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)

    def getLogRange(self, n: int):
        return len(bin(n)) - 2

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k:
            if node == -1:
                break
            if k & 1:  # checking if it is an odd number
                node = self.pars[i][node]
            i += 1
            k >>= 1
            print(i, k)
        return node


lst = [x for x in range(-1, 64, 1)]
obj = TreeAncestor(len(lst), lst)
print(obj.getKthAncestor(45, 41))
print(obj.getKthAncestor(56, 32))
print(obj.getKthAncestor(6, 5))

print("-----")

obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(obj.getKthAncestor(3, 1))
print(obj.getKthAncestor(5, 2))
print(obj.getKthAncestor(6, 3))
print(obj.getKthAncestor(5, 1))

print("-----")

obj = TreeAncestor(5, [-1, 0, 0, 0, 3])
print(obj.getKthAncestor(1, 5))
print(obj.getKthAncestor(3, 2))
print(obj.getKthAncestor(0, 1))
print(obj.getKthAncestor(3, 1))
print(obj.getKthAncestor(3, 5))

print("-----")
class BinaryTree:
    def __init__(self, key):
        self.val = key
        self.left_child = None
        self.right_child = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left_child:
            ret += self.left_child.__str__(level + 1, "L--- ")
        if self.right_child:
            ret += self.right_child.__str__(level + 1, "R--- ")
        return ret

    def as_dict(self):
        return {
            "val": self.val,
            "left_child": self.left_child.as_dict() if self.left_child else None,
            "right_child": self.right_child.as_dict() if self.right_child else None,
        }

    def delete(self, key):
        if self.val == key:
            if self.left_child is None and self.right_child is None:
                return None
            if self.left_child is None:
                return self.right_child
            if self.right_child is None:
                return self.left_child
            min_val = self.right_child.find_min()
            self.val = min_val
            self.right_child = self.right_child.delete(min_val)
        elif self.val > key:
            if self.left_child is not None:
                self.left_child = self.left_child.delete(key)
        else:
            if self.right_child is not None:
                self.right_child = self.right_child.delete(key)
        return self

    def find_max(self):
        if self.right_child is None:
            return self.val
        return self.right_child.find_max()

    def find_min(self):
        if self.left_child is None:
            return self.val
        return self.left_child.find_min()

    def get_sum(self):
        sum = self.val
        if self.left_child:
            sum += self.left_child.get_sum()
        if self.right_child:
            sum += self.right_child.get_sum()
        return sum

    def insert(self, new_node):
        if self.val > new_node:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                self.left_child.insert(new_node)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                self.right_child.insert(new_node)

    def search(self, key):
        if self.val == key:
            return True
        if self.val > key:
            if self.left_child is None:
                return False
            return self.left_child.search(key)
        else:
            if self.right_child is None:
                return False
            return self.right_child.search(key)

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        average = sum(lst) / len(lst)
        average_value = min(lst, key=lambda x: abs(x - average))
        root = cls(average_value)
        lst.remove(average_value)
        for val in lst:
            root.insert(val)
        return root


if __name__ == "__main__":
    import argparse
    import random

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", type=int, help="Number of elements in the tree", default=10)

    args = parser.parse_args()
    list_range = args.range
    lst = [random.randint(1, 10*list_range) for _ in range(list_range)]
    lst = list(set(lst))
    tree = BinaryTree.from_list(lst)
    print("Binary Tree:")
    print(tree)
    print(f"Sum of all elements: {tree.get_sum()}")
    print(f"Minimum value: {tree.find_min()}")
    print(f"Maximum value: {tree.find_max()}")

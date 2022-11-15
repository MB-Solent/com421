import intro3.implement_tree as module
import collections


def bfs(tree, target):
    open_list = collections.deque(maxlen=30)

    found = False

    open_list.append(tree.root)

    while found is False and len(open_list) > 0:

        current = open_list.popleft()
        if current.value == target:
            found = True
        else:
            if current.left is not None:
                open_list.append(current.left)
            if current.right is not None:
                open_list.append(current.right)

    if found is True:
        print("Target found in tree.")
    else:
        print("Target not found in tree.")


def run():
    tree = module.BinaryTree()
    tree.add(5, 2, 6, 7, 1, 3)
    tree.recursive_print()
    target = int(input("Input a number to search in the queue."))
    bfs(tree, target)


if __name__ == "__main__":
    run()

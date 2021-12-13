from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

segments = [[line.split("-")[0], line.split("-")[1]] for line in lines]


def find_connected_nodes(node_name):
    connected_nodes = []
    for seg in segments:
        if seg[0] == node_name:
            if seg[1] == "d":
                print("DEBUG!!! " + str(node_name))
            connected_nodes.append(TreeNode(seg[1], []))
        elif seg[1] == node_name:
            if seg[0] == "d":
                print("DEBUG!!! " + str(node_name))
            connected_nodes.append(TreeNode(seg[0], []))
    return connected_nodes


def find_node_by_name(name, root):
    if root.name != name and len(root.children) == 0:
        return None
    if root.name == name:
        return root
    for child in root.children:
        result = find_node_by_name(name, child)
        if result:
            return result
    return None


def build_node_dict():
    node_dict = defaultdict(list)
    for seg in segments:
        a, b = seg
        node_dict[a].append(b)
        node_dict[b].append(a)

    return node_dict

TOTAL_VALID_PATHS = 0
def count_valid_paths(nd, current_node, visited_small_caves):
    if current_node.islower():
        visited_small_caves.append(current_node)
    if current_node == "end":
        global TOTAL_VALID_PATHS
        TOTAL_VALID_PATHS += 1
        return
    else:
        for child in nd[current_node]:
            if child not in visited_small_caves:
                count_valid_paths(nd, child, visited_small_caves.copy())


nd = build_node_dict()
count_valid_paths(nd, "start", [])
print(TOTAL_VALID_PATHS)
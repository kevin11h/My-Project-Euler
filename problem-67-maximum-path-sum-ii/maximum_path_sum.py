from sys import argv
import itertools

def triangle_file_to_matrix(file_name):
    matrix = []

    with open(file_name, 'r') as f:
        for line in f:
            numbers = map(int, line.split())
            matrix.append(numbers)

    return matrix

class Node:
    def __init__(self, value, parents=[], children=[]):
        self.value = value
        self.parents = parents
        self.children = children

def matrix_to_graph(matrix):
    triangular_grid_graph = [[Node(num) for num in row] for row in matrix]

    for row_num in range(len(triangular_grid_graph)):
        next_row = row_num + 1

        if next_row < len(triangular_grid_graph):
            current_row_of_nums = triangular_grid_graph[row_num]
            next_row_of_nums = triangular_grid_graph[next_row]

            for i in range(len(current_row_of_nums)):
                parent_node = current_row_of_nums[i]
                left_child_node = next_row_of_nums[i]
                right_child_node = next_row_of_nums[i + 1]

                parent_node.children = [left_child_node, right_child_node]
                left_child_node.parents = left_child_node.parents + [parent_node]
                right_child_node.parents = right_child_node.parents + [parent_node]
                #left_child_node.parents.append(parent_node)
                #right_child_node.parents.append(parent_node)

    return frozenset(list(itertools.chain(*triangular_grid_graph)))

def max_path_sum(node):
    memo_tab = {}

    def max_path_sum_rec(node):
        if node is None:
            return 0
        else:
            if node not in memo_tab:
              path_length_to_parents = map(max_path_sum_rec, node.parents)
              local_sum = node.value + max(path_length_to_parents + [0])
              memo_tab[node] = local_sum

            return memo_tab[node]

    return max_path_sum_rec(node)

def max_path_sum_for_triangle_matrix(triangle_file):
    matrix = triangle_file_to_matrix(triangle_file)
    graph = matrix_to_graph(matrix)
    sinks = filter(lambda node : not node.children, graph)

    return max(map(max_path_sum, sinks))

print max_path_sum_for_triangle_matrix(argv[1])

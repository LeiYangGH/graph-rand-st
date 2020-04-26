import os
import re
from collections import defaultdict

reg_graph_content = re.compile(r'^(?:\d+\n){3}\n(?:(?:\d\s*)+\n)')


# reg_graph_content = re.compile(r'^(?:\d+\n){3}\n')

def read_graph(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if len(line) > 1]
        # print(lines)
        vertices_count = int(lines[0])
        s_vertex = lines[1]
        t_vertex = lines[2]
        # do some check for content format
        assert vertices_count == len(lines) - 3
        assert int(s_vertex) <= vertices_count
        assert int(t_vertex) <= vertices_count
        graph = defaultdict(list)

        for index_row, line in enumerate(lines[3:]):
            # print(index_row, line)
            self_vertex = str(index_row + 1)
            connects = [c.strip() for c in line.split()]
            assert len(connects) == vertices_count
            for index_column, is_connected in enumerate(connects):
                if is_connected == '1':
                    graph[self_vertex].append(str(index_column + 1))
                else:
                    assert is_connected == '0'
        # print(graph)
        return graph


if __name__ == "__main__":
    graph = read_graph(r'testgraphs/testgraph1.txt')
    print(graph)

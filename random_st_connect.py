import os
import random
from collections import defaultdict


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
        return (graph, vertices_count, s_vertex, t_vertex)


def randomised_st_connectivity(G, n, s, t):
    step_count = 0
    current_vertex = s
    while (current_vertex != t) and (step_count < 2 * pow(n, 3)):
        current_vertex = random.choice(G[current_vertex])
        step_count = step_count + 1
    if current_vertex == t:
        return (True, step_count)
    else:
        return (False, step_count)


def read_find_report(graph_file, report_file):
    (graph, vertices_count, s_vertex, t_vertex) = read_graph(graph_file)
    found, step_count = randomised_st_connectivity(graph, vertices_count, s_vertex, t_vertex)
    with open(report_file, "w") as fw:
        fw.write('input graph file: {} \n'.format(graph_file))
        fw.write('vertices_count: {} \n'.format(vertices_count))
        fw.write('s: {} \n'.format(s_vertex))
        fw.write('t: {} \n'.format(t_vertex))
        fw.write('Found: {}\n'.format(found))
        fw.write('step_count: {}\n'.format(step_count))
    print('Done processing {} and report in {}.'.format(graph_file, report_file))


if __name__ == "__main__":
    graphs_dir = 'testgraphs'
    reports_dir = 'reports'
    if not os.path.isdir(reports_dir):
        os.mkdir(reports_dir)
    for filename in os.listdir(graphs_dir):
        graph_fullname = os.path.join(graphs_dir, filename)
        report_fullname = os.path.join(reports_dir, filename)
        read_find_report(graph_fullname, report_fullname)

import parser
import graphviz as gv

class Grapher(object):
    def __init__(self):
        self.graph = gv.Graph(format='png')
        self.idx = 0

    def plot_graph(self, parent, tree):
        self.idx += 1
        if isinstance(tree, parser.AndNode):
            self.graph.node(parent)
            current_idx = self.idx
            self.graph.edge(parent, "AND" + str(current_idx))
            for sub in tree.children:
                self.plot_graph("AND" + str(current_idx), sub)
        elif isinstance(tree, parser.OrNode):
            self.graph.node(parent)
            current_idx = self.idx
            self.graph.edge(parent, "OR" + str(current_idx))
            for sub in tree.children:
                self.plot_graph("OR" + str(current_idx), sub)
        elif isinstance(tree, parser.Course):
            self.graph.node(parent)
            self.graph.edge(parent, tree.name)
        else:
            exit(1) # you done fucked up.



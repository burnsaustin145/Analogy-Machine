import networkx as nx

class ComplexObject(object):

    def __init__(self, graph=None):
        self.complex_universe = {}
        self.name_id = 0
        self.names = {}  # names to be used for Co construction, collects and checks for redundancy
        if graph is None:
            self.graph = nx.DiGraph()
        else:
            if isinstance(graph, dict):
                self.graph = nx.DiGraph()
                for node, edges in graph.items():
                    self.graph.add_node(node)
                    for target, weight in edges.items():
                        self.graph.add_edge(node, target, weight=weight)
            else:
                self.graph = graph

    def complex_universe_construction(self, *node, union=False):
        """takes k nodes and returns a l1cu.
        Used in object and quality construction"""

        one_meta_universe = {}

        for foo in node:
            if foo in self.graph:
                bar = set()
                # adjusted to use successors properly 
                for baz in self.graph.successors(foo):
                    bar.add(baz)
            if bar is not None:
                one_meta_universe[foo] = bar

        container = []

        for foo in one_meta_universe.values():
            container.append(foo)

        if union:
            inner_dict = {}
            sett = set.union(*container)
            for foo in sett:
                inner_dict[foo] = 1

            name = 'l1cuo-{}'.format(self.name_creation(*sett, 'l1cu'))

            self.complex_universe[name] = inner_dict
            self.graph.add_edges_from([(foo, bar) for foo in sett for bar in sett if foo != bar])
        else:
            inner_dict = {}
            sett = set.intersection(*container)
            for foo in sett:
                inner_dict[foo] = 1

            name = 'l1cuc-{}'.format(self.name_creation(*sett, level='l1cu'))

            self.complex_universe[name] = inner_dict
            self.graph.add_edges_from([(foo, bar) for foo in sett for bar in sett if foo != bar])

        return self.graph

    def complex_quality_construction(self, *node):
        """takes n nodes and returns a complex quality
        object, as well as saving one into the graph"""

        l1cu = self.complex_universe_construction(*node)

        name = 'l1cq-{}'.format(self.name_creation(*node, level='l1cq'))
        inner = {}
        l1cq = {}
        l1cq.setdefault(name)
        for foo in l1cu:
            inner[foo] = 1

        l1cq[name] = inner
        self.graph.add_edges_from([(foo, bar) for foo in inner for bar in inner if foo != bar])
        return l1cq

    def complex_object_construction(self, *node):
        """takes n nodes, and uses quality construction
        to generate a quality. Then finds all k w/ *q
        qualities, creating a l1co.
        returns a node with the standard labeling
        convention 'L1Co-xxx' and adds it back into the
        main graph"""

        l1co = {}
        l1cq = self.complex_quality_construction(*node)

        curr_o = set()
        for foo in l1cq:
            for bar in l1cq[foo]:
                curr_o.add(bar)

        inner = dict()
        for baz in self.graph:
            curr_q = set()

            for bar in self.graph.successors(baz):
                curr_q.add(bar)

            if set.intersection(curr_q, curr_o) == set():
                continue

            elif set.intersection(curr_q, curr_o) == curr_o:
                name_creation = self.name_creation(*curr_q, level='l1co')
                name = "l1co-{}".format(name_creation)

                inner[baz] = 1
        name = 'l1co-{}'.format(self.name_creation(*curr_q, level='l1co'))
        l1co[name] = inner
        self.graph.add_edges_from([(foo, bar) for foo in inner for bar in inner if foo != bar])

        return l1co

    def name_creation(self, *node, level):
        """takes n nodes and returns the first
        letter name code (checks for extant names
        in class attribute 'self.names' a dict."""

        name_creation = ''
        for foo in node:
            name_creation += str(foo)

        if name_creation in self.names:
            name_creation += 'x'
            self.names[name_creation] = level
        else:
            self.names[name_creation] = level

        if name_creation is not None:
            return name_creation
        else:
            self.name_id += 1
            return self.name_id



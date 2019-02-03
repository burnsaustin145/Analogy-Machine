import pprint


class GraphDict(object):

    def __init__(self, graph_dict=None):
        """initializes graph object;
    empty if passed no start graph
    """

        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict
            
    def __get__(self, instance, owner):
        return self.graph_dict

    def get_graph(self):
        """returns the graph, fully
        enumerated"""
        pprint.pprint(self.graph_dict)

    def add_node(self, *node):
        """adds a node to the main graph,
        added with an empty arc dict.
        First checks for exsisting node;
        if one is found, user can write another
        node of the same name called a
        'double'"""
        keys = list(self.graph_dict.keys())
        for foo in node:
            if foo in keys:
                print("****node in keys mate****")
                choice = input("Node exists already, still write?(y/n):")
                if choice == 'y':
                    bar = foo * 2
                    self.graph_dict[bar] = {}
                    return
                elif choice == 'n':
                    return
                else:
                    print("input error")
                    return
            else:
                self.graph_dict[foo] = {}

    def add_arc(self, node, *arc):
        """adds any number of arcs to one
        node at value '1'. checks for existing
        node/arcs first. Will add node/arc
        if not in (think on the merit of this)"""
        if node in self.graph_dict:
            for foo in arc:
                if foo in self.graph_dict:
                    self.graph_dict[node][foo] = 1
                else:
                    self.add_node(foo)
                    self.add_arc(node, foo)
        else:
            self.add_node(node)
            self.add_arc(node, *arc)

    def q_or_e(self, node):
        """takes node and defines it as an entity
        or a quality **need a better way than
        exhaustively searching qualities"""
        qualities = []
        for foo in self.graph_dict:
            for bar in self.graph_dict[foo]:
                qualities.append(bar)
        if node in qualities:
            return 'q'
        else:
            return 'e'

    def cup_or_ce(self, l1cu):
        """will decide whether a Cu is a CU or Ce
        using the q_or_e function. Then returns
        CU or Ce as labeled as such"""

        pass

    def set_of_parents(self, vertex):
        """Takes a vertex and returns a set of all parents"""
        set_parents = set()
        for foo in self.graph_dict:
            for bar in self.graph_dict[foo]:
                if bar == vertex:
                    set_parents.add(foo)
                else:
                    pass

        return set_parents


class ComplexObject(object):

    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict
        self.complex_universe = {}
        self.names = {}  # names to be used for Co construction, collects and checks for redundancy
        if graph_dict is None:
            self.graph_dict = {}
        
    def complex_universe_construction(self, *node, union=False):
        """takes k nodes and returns a l1cu.
        Used in object and quality construction"""
        #TODO check for extant names before naming (not sure if working, moved to name creation)
        one_meta_universe = {}

        for foo in node:
            if self.graph_dict[foo]:
                bar = set()
                for baz in self.graph_dict[foo]:
                    if self.graph_dict[foo][baz] == 1:
                        bar.add(baz)
                    else:
                        pass
                    
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
            self.graph_dict[name] = inner_dict
        else:
            inner_dict = {}
            sett = set.intersection(*container)
            for foo in sett:
                print('foo' + foo)
                inner_dict[foo] = 1

            name = 'l1cuc-{}'.format(self.name_creation(*sett, level='l1cu'))

            self.complex_universe[name] = inner_dict
            self.graph_dict[name] = inner_dict

        return self.graph_dict[name]

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
        self.graph_dict[name] = inner
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
        for baz in self.graph_dict:
            curr_q = set()

            for bar in self.graph_dict[baz]:
                curr_q.add(bar)

            if set.intersection(curr_q, curr_o) == set():
                continue

            elif set.intersection(curr_q, curr_o) == curr_o:
                name_creation = self.name_creation(*curr_q, level='l1co')
                name = "l1co-{}".format(name_creation)

                inner[baz] = 1

        l1co[name] = inner
        self.graph_dict[name] = inner

        return l1co

    def name_creation(self, *node, level):
        """takes n nodes and returns the first
        letter name code (checks for extant names
        in class attribute 'self.names' a dict."""

        name_creation = ''
        for foo in node:
            name_creation += foo[0]

        if name_creation in self.names:
            name_creation += 'x'
            self.names[name_creation] = level
        else:
            self.names[name_creation] = level

        return name_creation


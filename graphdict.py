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









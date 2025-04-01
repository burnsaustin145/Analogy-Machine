from graphdict import *
from complexobject import *

g = GraphDict()
co = ComplexObject(g.graph_dict)


class Control(object):

    def __init__(self):
        return

    @staticmethod
    def composition(*node):
        g.add_node(*node)
        """I think this might take nothing but """
        co.complex_object_construction(*node)
        """and here's where I'll start composing all of
        the other complex constructors and what not;
        still need to think on design a bit."""


c = Control()
c.composition('comp nodes')

print(g.graph_dict)
print(co.graph_dict)



















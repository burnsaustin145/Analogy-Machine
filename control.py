from graphdict import *
from complexobject import *


class Control(object):

    def __init__(self, graph_dict=None):

        if graph_dict is None:
            self.graph_dict = self.g.graph_dict
        else:
            self.graph_dict = {}

    def control(self):
        self.g(self.graph_dict)
        self.c(self.graph_dict)
        self.g.add_arc("Connor", "Burns")
        print(self.graph_dict)














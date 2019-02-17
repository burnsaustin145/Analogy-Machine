from graphdict import *
from complexobject import *
import pprint

if __name__ == "__main__":
    g = {"Connor": {"Burns": 1} # this just means if I'm not importing then use these run commands
         }

    ##I should pass the graph_dict instance attribute to my universe instance on the main class page itself, perhaps
    ##in a seperate (meta?) class used for combining objects
    graph = GraphDict(g)
    universe = ComplexObject(graph.graph_dict)

    ##*test code for graph & add & the q/e question

    graph.add_node("Austin", "Burns", "Person", "Miranda", "phone")
    graph.add_arc("Austin", "Burns", "Person", "testies")
    graph.add_arc("Connor", "organized", "anal", "entertaining", "Person")
    graph.add_arc("organized", "modifier", "quality", "word")
    graph.add_arc("Austin", "word")
    graph.add_arc("Miranda", "Burns", "Person", "word", "nice", "girl", "female")
    graph.add_arc("female", "word", "modifier", "sex")
    graph.add_arc("sex", "word", "reproduction", "type")
    graph.add_arc("phone", "item", "technology", "communication", "communicate", "handheld")
    graph.add_arc("handheld", "modifier", "size")
    graph.add_arc("size", "metric", "descriptor", "relative")
    graph.add_arc("miranda", "small")
    graph.add_arc("small", "size")
    graph.add_arc("Connor", "Skinny", "tall", "white", "college", "student", "word")
    graph.add_arc("Miranda", "student", "small", "short", "happy")
    print(pprint.pprint(universe.graph_dict))
    print("First L1Cu construction test (Miranda, Connor)")
    print(universe.complex_universe_construction('Miranda', 'Connor'))
    print('find all parents (person)')
    print(graph.set_of_parents('Person'))
    print('find all parents (Burns)')
    print(graph.set_of_parents('Burns'))
    print('find all parents of (reproduction)')
    print(graph.set_of_parents('reproduction'))
    print(graph.q_or_e('Miranda'))
    print("Result of complex construction on the kids: ")
    universe.complex_universe_construction('Miranda', 'Austin')
    print(pprint.pprint(graph.graph_dict))
    print(universe.complex_quality_construction('Miranda', 'Austin'))
    print("Complex object construction test: ")
    print(universe.complex_object_construction('Miranda', 'Austin'))
    print("graph. graph_dict test here folks:")
    print(pprint.pprint(graph.graph_dict))
    graph.graph_dict['foo'] = "this is added after graph.graph_dict, but before universe.graph dict is printed"
    print("universe.graph_dict test here folks:")
    print(pprint.pprint(universe.graph_dict))

    print(graph.get_graph())
    print(GraphDict.get_graph(graph))





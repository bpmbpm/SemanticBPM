from lxml import etree
from pprint import pp

namespaces = {"g": "http://graphml.graphdrawing.org/xmlns", "y": "http://www.yworks.com/xml/graphml"}

nodes_xpath = '//g:graph/g:node'
edges_xpath = '//g:graph/g:edge'

shape_type_mapping = {
    "ellipse": "rdfs:Literal",
    "rectangle": "owl:Class",
}

def get_node_parameters(node):
    return {
        "id": node.xpath("@id", namespaces = namespaces)[0],
        "label": node.xpath("g:data/y:ShapeNode/y:NodeLabel/text()", namespaces = namespaces)[0],
        "type": shape_type_mapping[node.xpath("g:data/y:ShapeNode/y:Shape/@type", namespaces = namespaces)[0]],
    }

def get_edge_parameters(edge):
    id = edge.xpath("@id", namespaces = namespaces)[0]
    source = edge.xpath("@source", namespaces = namespaces)[0]
    target = edge.xpath("@target", namespaces = namespaces)[0]
    label = edge.xpath(f"g:data/y:PolyLineEdge/y:EdgeLabel/text()", namespaces = namespaces)[0]
    return {
        "id": id,
        "type": "rdf:Property",
        "source": source,
        "target": target,
        "label": label,
    }

def build_triple(edge, processed_nodes):
    source_node = list(filter(lambda node: node["id"] == edge["source"], processed_nodes))[0]
    target_node = list(filter(lambda node: node["id"] == edge["target"], processed_nodes))[0]
    return [source_node["label"], edge["label"], target_node["label"]]

tree = etree.parse("diagrams/siem_example.graphml")

nodes = tree.xpath(nodes_xpath, namespaces = namespaces)
edges = tree.xpath(edges_xpath, namespaces = namespaces)

processed_nodes = [get_node_parameters(node) for node in nodes]
processed_edges = [get_edge_parameters(edge) for edge in edges]

triples = [build_triple(edge, processed_nodes) for edge in processed_edges]

pp(triples)

#!/usr/bin/env python3

from lxml import etree
from pprint import pp
from argparse import ArgumentParser

namespaces = {"g": "http://graphml.graphdrawing.org/xmlns", "y": "http://www.yworks.com/xml/graphml"}

nodes_xpath = '//g:graph/g:node'
edges_xpath = '//g:graph/g:edge'

# shape_type_mapping = {
#     "rectangle": "owl:Class",
#     "ellipse": "xsd:string",
#     "parallelogram": "xsd:integer",
#     "hexagon": "xsd:dateTime",
# }

node_configuration_mapping = {
    "com.yworks.flowchart.userMessage": "vad:Process",
    "com.yworks.flowchart.start1": "vad:Performer"
}

onto_predicates = ["a", "rdf:type", "vad:next", "vad:previous", "vad:comment", "vad:performs"]

def prefix_header(prefix_file):

    ttl_header = """@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix vad: <http://example.org/vad2#> .
"""

    if prefix_file:
        with open(prefix_file) as fp:
            custom_prefixes = fp.read()
            ttl_header += ""
            ttl_header += custom_prefixes

    return ttl_header

def ontology_header(namespace, version):
    return f"""
<{namespace[:-1]}>
    a vad:Diagram ;
    .
"""

def is_attribute(node):
    return node["type"] in ["xsd:string", "xsd:dateTime", "xsd:integer"]

def is_special_edge(edge):
    return edge["label"] in ["attribute"]

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

# def build_triple(edge, processed_nodes):
#     source_node = list(filter(lambda node: node["id"] == edge["source"], processed_nodes))[0]
#     target_node = list(filter(lambda node: node["id"] == edge["target"], processed_nodes))[0]
#     return [source_node["label"], edge["label"], target_node["label"]]

def standalone_str(s):
    return f"""
{s}
"""

def get_onto_edges(edges):
    return list(filter(lambda edge: edge["label"] in onto_predicates, edges))

def get_oprop_edges(edges):
    return list(filter(lambda edge: edge["label"] not in onto_predicates and not is_special_edge(edge), edges))

def get_node_by_id(nodes, id):
    for node in nodes:
        if node["id"] == id:
            return node

def build_definitions(nodes, edges):
    classes = list(set([node["label"] for node in nodes if not is_attribute(node)]))
    attributes = list(set([node["label"] for node in nodes if is_attribute(node)]))
    object_properties = list(map(lambda edge: edge["label"], get_oprop_edges(edges)))
    result = ""
    for c in classes:
        result += standalone_str(f"{c} a owl:Class .")
    for attribute in attributes:
        result += standalone_str(f"{attribute} a owl:DatatypeProperty .")
    for p in object_properties:
        result += standalone_str(f"{p} a owl:ObjectProperty .")
    return result

def build_onto_triples(nodes, edges):
    edges = get_onto_edges(edges)
    classes = list(set([node["label"] for node in nodes if not is_attribute(node)]))
    attributes = list(set([node["label"] for node in nodes if is_attribute(node)]))
    object_properties = list(set([edge["label"] for edge in edges if not is_special_edge(edge)]))
    result = ""
    for edge in edges:
        subject = get_node_by_id(nodes, edge["source"])["label"]
        predicate = edge["label"]
        object = get_node_by_id(nodes, edge["target"])["label"]
        result += standalone_str(f"{subject} {predicate} {object} .")
    return result

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", action="store", dest="input")
    parser.add_argument("-o", "--output", action="store", dest="output")
    parser.add_argument("-f", "--format", dest="format", default="turtle")
    parser.add_argument("-p", "--prefixes", action="store", dest="prefix_file", default=False)
    parser.add_argument("-n", "--namespace", action="store", dest="namespace", default="http://sec-kg.org/input-ontologies/example#")
    parser.add_argument("-v", "--version", action="store", dest="version", default="0.1")
    args = parser.parse_args()

    tree = etree.parse(args.input)

    nodes = tree.xpath(nodes_xpath, namespaces = namespaces)
    edges = tree.xpath(edges_xpath, namespaces = namespaces)

    processed_nodes = [get_node_parameters(node) for node in nodes]
    processed_edges = [get_edge_parameters(edge) for edge in edges]

    # triples = [build_triple(edge, processed_nodes) for edge in processed_edges]

    subject_ids = []
    result = prefix_header(args.prefix_file)
    result += ""
    result += ontology_header(args.namespace, args.version)
    result += ""
    result += build_definitions(processed_nodes, processed_edges)
    result += ""
    result += build_onto_triples(processed_nodes, processed_edges)
    result += ""
    for edge in processed_edges:
        subject_id = edge["source"]
        if not subject_id in subject_ids:
            result += build_shacl_rules(processed_nodes, processed_edges, subject_id)
        subject_ids.append(subject_id)

    # pp(result)
    open(args.output, 'w').write(result)

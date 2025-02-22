#!/usr/bin/env python3

from lxml import etree
from pprint import pp
from argparse import ArgumentParser
from odysseus.debug import __
from odysseus.coll import get

namespaces = {"g": "http://graphml.graphdrawing.org/xmlns", "y": "http://www.yworks.com/xml/graphml"}

nodes_xpath = '//g:graph/g:node'
edges_xpath = '//g:graph/g:edge'

rdf_mapping = {
    "comment": "rdfs:comment"
}

node_configuration_mapping = {
    "com.yworks.flowchart.userMessage": "vad:Process",
    "com.yworks.flowchart.start1": "vad:Performer",
    "com.yworks.flowchart.process": "vad:Comment",
    "com.yworks.flowchart.networkMessage": "vad:ParentProcess"
}

def prefix_header(namespace = "http://example.org/vad2/diagram#"):
    ttl_header = f"""@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix vad: <http://example.org/vad2#> .
@prefix : <{namespace}> .
"""
    return ttl_header

def standalone_str(s):
    return f"""
{s}
"""

def get_node_by_id(nodes, id):
    for node in nodes:
        if node["id"] == id:
            return node

def is_named_graph(node):
    return get(node, "type") in ["vad:ParentProcess"]

def is_individual(node):
    return get(node, "type") in ["vad:Process", "vad:Performer"]

def is_literal(node):
    return get(node, "type") in ["vad:Comment"]

def get_node_parameters(node):
    return {
        "id": node.xpath("@id", namespaces = namespaces)[0],
        "label": node.xpath("g:data/y:GenericNode/y:NodeLabel/text()", namespaces = namespaces)[0],
        # "type": shape_type_mapping[node.xpath("g:data/y:ShapeNode/y:Shape/@type", namespaces = namespaces)[0]],
        "type": node_configuration_mapping[node.xpath("g:data/y:GenericNode/@configuration", namespaces = namespaces)[0]],
    }

def get_edge_parameters(edge):
    id = edge.xpath("@id", namespaces = namespaces)[0]
    source = edge.xpath("@source", namespaces = namespaces)[0]
    target = edge.xpath("@target", namespaces = namespaces)[0]
    label = edge.xpath(f"g:data/y:PolyLineEdge/y:EdgeLabel/text()", namespaces = namespaces)[0]
    return {
        "id": id,
        "source": source,
        "target": target,
        "label": label,
    }

def build_definitions(nodes, edges):
    individuals = [node for node in nodes if is_individual(node)]
    result = ""
    for i in individuals:
        id = i["id"]
        type = i["type"]
        label = i["label"]
        result += standalone_str("")
        result += f":{id} a owl:NamedIndividual, {type} ;\n"
        result += f"\t\trdfs:label \"{label}\" ."
    return result

def build_triples(nodes, edges):
    result = ""
    for edge in edges:
        subject = get_node_by_id(nodes, edge["source"])["id"]
        predicate = get(rdf_mapping, edge["label"], "vad:" + edge["label"])
        object = get_node_by_id(nodes, edge["target"])
        if is_literal(object):
            object = "\"" + object["label"] + "\""
        else:
            object = ":" + object["id"]
        result += standalone_str(f":{subject} {predicate} {object} .")
    return result

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", action="store", dest="input")
    parser.add_argument("-o", "--output", action="store", dest="output")
    parser.add_argument("-n", "--namespace", action="store", dest="namespace", default="http://example.org/vad2/diagram#")
    args = parser.parse_args()

    tree = etree.parse(args.input)

    nodes = tree.xpath(nodes_xpath, namespaces = namespaces)
    edges = tree.xpath(edges_xpath, namespaces = namespaces)

    processed_nodes = [get_node_parameters(node) for node in nodes]
    processed_edges = [get_edge_parameters(edge) for edge in edges]

    # triples = [build_triple(edge, processed_nodes) for edge in processed_edges]

    result = ""
    result += build_definitions(processed_nodes, processed_edges)
    result += "\n"
    result += build_triples(processed_nodes, processed_edges)

    named_graph = [node for node in processed_nodes if is_named_graph(node)]
    if named_graph:
        named_graph = named_graph[0]
        named_graph_id = named_graph["id"]
        named_graph_type = named_graph["type"]
        result = f":{named_graph_id} {{{result}\n}}"
        result = f"\n\n:{named_graph_id} a owl:NamedIndividual, {named_graph_type} .\n\n" + result

    result = prefix_header(args.namespace) + result

    # pp(result)
    open(args.output, 'w').write(result)

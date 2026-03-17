import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    """
    Build a directed graph representing the LLM processing workflow.
    Mimics LangGraph-style orchestration for visualization and system documentation.
    """
    G = nx.DiGraph()
    G.add_edges_from([
        ("User Input", "Intent Detection"),
        ("Intent Detection", "Document Retrieval"),
        ("Document Retrieval", "LLM Response"),
        ("LLM Response", "Output")
    ])
    # save visualization for documentation / architecture review
    nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", arrows=True)
    plt.savefig("graph.png")
    return G
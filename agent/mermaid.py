from IPython.display import Image, display
from langchain_core.runnables.graph import MermaidDrawMethod
from graph import graph_builder

display(Image(graph_builder.get_graph(xray=2).draw_mermaid_png()))

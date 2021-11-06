import Model
import os
import shutil
import graphviz as gv
from PIL import Image


# Defining graph styles
default_style = {
    'graph': {
        'rankdir': 'LR'
    },
    'nodes': {
        'shape': 'circle',
    },
    'edges': {
        'arrowhead': 'open',
    }
}


# Applying graph styles
def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


# Constructing argumentative framework graph
def ConstructGraph():

    # Apply graphic styles to generate jpg type images
     graph = gv.Digraph(format='jpg')
     apply_styles(graph, default_style)

    # Generate graphical nodes based on arguments
     for i in Model.arguments:
         graph.node(i, i)

    # Generate edges based on attack relationships
     ed = []
     for i in Model.relations:
         ed.append((i[0], i[1]))
     graph.edges(ed)

    # Rendered image saved to path 'data/graph'
     graph.render('data/graph')


# Constructing argumentative label colour display graph
def ConstructColouredGraph(label):

    # Empty the files，initialise the folder for the label graph
    if not os.path.exists('./data/labelgraphs'):
        os.mkdir('./data/labelgraphs')
    else:
        shutil.rmtree('./data/labelgraphs')
        os.mkdir('./data/labelgraphs')

    # Iterate over the label sets if it is not empty
    lens = len(label)
    if lens != 0:
        for i in label:

            # Apply graphic styles to generate jpg type images
            labelgraph = gv.Digraph(format='jpg')
            apply_styles(labelgraph, default_style)

            # Changing data types to list
            eachlabel = list(i)

            # Generate graphical nodes based on arguments, display colours based on label sets
            for j in Model.arguments:
                if j in eachlabel[0]:
                    labelgraph.node(j, j, color="green")
                elif j in eachlabel[1]:
                    labelgraph.node(j, j, color="red")
                elif j in eachlabel[2]:
                    labelgraph.node(j, j, color="grey")

            # Generate edges based on attack relationships
            ed = []
            for m in Model.relations:
                ed.append((m[0], m[1]))
            labelgraph.edges(ed)

            # Rendered image saved to path 'data/labelgraph'
            labelgraph.render('data/labelgraph')

            # Copy image to folder
            shutil.copy2('./data/labelgraph.jpg', './data/labelgraphs/labelgraph {}.jpg'.format(lens))
            lens = lens-1

        # Open the original image, get the number of label sets,
        # create a new image based on the size of the original image and the number of label sets
        image = Image.open('./data/labelgraph.jpg')
        lens = len(label)
        to_image = Image.new('RGB', (image.size[0], lens * image.size[1]))

        # Stitch the label images in sequence onto the new image
        for x in range(lens):
            from_image = Image.open('./data/labelgraphs/labelgraph {}.jpg'.format(x+1))
            to_image.paste(from_image, (0, (x) * image.size[1]))
        to_image.save('./data/resultlabelgraph.jpg')

    # If it is empty, clear the label image
    else:
        shutil.copy2('./data/blank.png', './data/resultlabelgraph.jpg')
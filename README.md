# Computational Graph interview question

## About

## Examples

Here is an example of the graph `2x - 3y`:

![graph](diff_of_products.dot.png)

You can see how this would be written in different formats:
* [dot](dot/diff_of_products.dot)
* [json](d3/diff_of_products.json)
* csv [nodes](csv/diff-of-products.nodes.csv) and [edges](csv/diff-of-products.edges.csv)

There are some more examples in the `d3`, `dot`, and `csv` directories.

### Setup

To run the dot examples, you must first `brew install dot`

To run the python examples, you must first `pip install -r requirements.txt`

### Run

You can visualise the examples by running e.g.:

    ./dot-to-png.sh dot/coloured_graph.dot

    python plot-csv.py coloured-graph


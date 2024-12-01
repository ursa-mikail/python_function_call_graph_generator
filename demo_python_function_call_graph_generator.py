## outputs - `example.py`: Python script containing functions such as `factorial`, `fibonacci`, `calculate`, `display_results`, and `main` to demonstrate function calls.

example_code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calculate():
    fact_result = factorial(5)
    fib_result = fibonacci(5)
    return fact_result, fib_result

def display_results():
    fact, fib = calculate()
    print(f"Factorial(5): {fact}")
    print(f"Fibonacci(5): {fib}")

def main():
    display_results()

if __name__ == "__main__":
    main()
"""
with open('/content/example.py', 'w') as file:
    file.write(example_code)


## - `call_graph.dot`: DOT file representing the function call graph.
## - `call_graph.png`: Final PNG image of the call graph generated from `example.py`.

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

# Set the output file path
graphviz = GraphvizOutput()
graphviz.output_file = '/content/call_graph.png'

# Use pycallgraph to trace the function calls
with PyCallGraph(output=graphviz):
    import example
    example.main()

# Display the generated call graph image
from IPython.display import Image, display

display(Image(filename=graphviz.output_file))


## - `call_graph_calling_between_functions.png`: PNG image of the call graph showing the functions `main`, `display_results`, `calculate`, `factorial`, and `fibonacci`.
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
import sys

# Set the output file path for the higher-level call graph
graphviz = GraphvizOutput()
graphviz.output_file = '/content/call_graph_calling_between_functions.png'

# Create a custom trace function to filter the functions we want to include
def trace(frame, event, arg):
    # We are only interested in the functions in the call chain: main, display_results, calculate, factorial, fibonacci
    func_names = ['main', 'display_results', 'calculate', 'factorial', 'fibonacci']
    if frame.f_code.co_name in func_names:
        return trace
    return None

# Use pycallgraph2 to trace function calls and generate the call graph for the selected functions
sys.settrace(trace)  # Start tracing
with PyCallGraph(output=graphviz):
    import example
    example.main()
sys.settrace(None)  # Stop tracing

# Display the generated call graph image
from IPython.display import Image, display

display(Image(filename=graphviz.output_file))

## call_graph_calling_between_functions_in_example.py.png focusing on example.py calls
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
import sys

# Set the output file path for the generated call graph
graphviz = GraphvizOutput()
graphviz.output_file = '/content/call_graph_calling_between_functions_in_example.py.png'

# Create a custom trace function to filter the functions to be included in the graph
def trace(frame, event, arg):
    # We only want to trace functions in the call chain starting from main
    func_names = ['main', 'display_results', 'calculate', 'factorial', 'fibonacci']
    if frame.f_code.co_name in func_names:
        return trace
    return None

# Use pycallgraph2 to trace function calls and generate the call graph for the selected functions
sys.settrace(trace)  # Start tracing
with PyCallGraph(output=graphviz):
    import example  # Import the script, triggering the trace
    example.main()  # Run main(), starting the function calls
sys.settrace(None)  # Stop tracing

# Display the generated call graph image
from IPython.display import Image, display

display(Image(filename=graphviz.output_file))

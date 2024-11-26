# false positive case in bandit

import ast

def safe_eval(expr):
    """
    Safely evaluate a mathematical expression.
    Only allows basic arithmetic operations.
    """
    # Parse the expression
    tree = ast.parse(expr, mode='eval')

    # Define allowed node types
    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Num,
        ast.operator,
        ast.unaryop,
    )

    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Unsafe expression detected!")

    return eval(compile(tree, filename="", mode="eval"))

# Example usage
if __name__ == "__main__":
    user_input = "2 + 3 * (4 - 1)"
    result = safe_eval(user_input)
    print(f"Result: {result}")

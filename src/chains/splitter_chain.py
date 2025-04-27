

import ast
from typing import List

def split_functions(code: str) -> List[str]:
    """
    Split a Python source string into individual function and class snippets.

    Returns a list where each item is the source of one top-level function or class.
    """
    tree = ast.parse(code)
    lines = code.splitlines()
    snippets: List[str] = []

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            start, end = node.lineno - 1, node.end_lineno
            snippet = "\n".join(lines[start:end])
            snippets.append(snippet)

    return snippets

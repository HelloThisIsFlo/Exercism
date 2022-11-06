import re
from enum import Enum, auto, Flag


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return f"Node<prop={self.properties} | child={self.children}>"


class Parsing(Enum):
    START = auto()
    TREE = auto()
    NODE = auto()
    KEY = auto()
    VALUE = auto()


def valid_key_char(key_char):
    return key_char.isupper()


def validate_key_char(key_char):
    if not valid_key_char(key_char):
        raise ValueError(f"Key char is not valid: '{key_char}'")


def new_node():
    return SgfTree(properties=dict(), children=[])


def parse(input_string: str):
    if not input_string:
        raise ValueError("Empty String")
    print()
    print()
    print(input_string)
    print()

    root = new_node()
    node = root

    key = []
    val = []
    prev = ""
    parsing_value = False
    for curr in input_string:
        print()
        print("(prev, curr):", f"('{prev}', '{curr}')")

        if parsing_value:
            match (prev, curr):
                case ("\\", val_curr):
                    print("CONTINUE: Val - [Replace escape] ", val_curr)
                    val[-1] = val_curr

                case (_, "]"):
                    print("END: Value")
                    node.properties[key].append("".join(val))
                    parsing_value = False

                case (_, "\n" as val_curr):
                    print("CONTINUE: Val - \\n")
                    val.append(val_curr)

                case (_, whitespace) if re.match(r"\s", whitespace):
                    print("CONTINUE: Val - [replace whitespace]")
                    val.append(" ")

                case (_, val_curr):
                    print("CONTINUE: Val -", val_curr)
                    val.append(val_curr)

                case _:
                    raise ValueError("Unexpected char")
        else:
            match (prev, curr):
                case ("", "("):
                    print("START: Tree (first)")

                case ("]" | ")", "("):
                    print("START: Tree (subtree)")

                case ("(", ";"):
                    print("START: Node (first)")

                case ("]", ";"):
                    print("START: Node (extra)")
                    parent = node
                    node = new_node()
                    parent.children.append(node)

                case (prev, "[") if valid_key_char(prev):
                    print("END: Key")
                    node.properties["".join(key)] = []

                case ("[", val_curr):
                    print("& START: Value")
                    val = [val_curr]
                    parsing_value = True

                case ("]", "["):
                    print("START: Extra Value")

                case ("]" | ";" | ")", ")"):
                    print("END: Subtree")

                case ("]", key_curr):
                    print("START: Extra Key")
                    validate_key_char(key_curr)
                    key = key_curr

                case (";", key_curr):
                    print("START: Key -", key_curr)
                    validate_key_char(key_curr)
                    key = key_curr

                case (prev, key_curr) if valid_key_char(prev):
                    print("CONTINUE: Key -", key_curr)
                    validate_key_char(key_curr)
                    key += key_curr

                case _:
                    raise ValueError("Unexpected char")

        prev = curr

    return root

class StackUnderflowError(Exception):
    """Exception raised when stack does not have enough items."""
    pass


def evaluate(input_data):
    stack = []
    dictionary = {}

    def require(n):
        if len(stack) < n:
            raise StackUnderflowError("Insufficient number of items in stack")

    def is_number(token):
        return token.lstrip("-").isdigit()

    # Built-ins
    def add():
        require(2)
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)

    def sub():
        require(2)
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)

    def mul():
        require(2)
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)

    def div():
        require(2)
        b, a = stack.pop(), stack.pop()
        if b == 0:
            raise ZeroDivisionError("divide by zero")
        stack.append(a // b)

    def dup():
        require(1)
        stack.append(stack[-1])

    def drop():
        require(1)
        stack.pop()

    def swap():
        require(2)
        stack[-1], stack[-2] = stack[-2], stack[-1]

    def over():
        require(2)
        stack.append(stack[-2])

    builtins = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "dup": dup,
        "drop": drop,
        "swap": swap,
        "over": over,
    }

    def compile_token(token):
        if is_number(token):
            value = int(token)
            return lambda: stack.append(value)

        if token in dictionary:
            ops = dictionary[token]

            def run():
                for op in ops:
                    op()

            return run

        if token in builtins:
            return builtins[token]

        raise ValueError("undefined operation")

    # Flatten input
    tokens = []
    for line in input_data:
        tokens.extend(line.lower().split())

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == ":":
            i += 1
            if i >= len(tokens):
                raise ValueError("invalid definition")

            name = tokens[i]

            if is_number(name):
                raise ValueError("illegal operation")

            i += 1
            definition_tokens = []

            while i < len(tokens) and tokens[i] != ";":
                definition_tokens.append(tokens[i])
                i += 1

            if i == len(tokens):
                raise ValueError("invalid definition")

            compiled = []
            for t in definition_tokens:
                compiled.append(compile_token(t))

            dictionary[name] = compiled

        else:
            op = compile_token(token)
            op()

        i += 1

    return stack
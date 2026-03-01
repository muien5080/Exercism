def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    expression = question[8:-1].strip()
    if not expression:
        raise ValueError("syntax error")

    tokens = expression.split()

    try:
        result = int(tokens[0])
    except:
        raise ValueError("syntax error")

    i = 1

    while i < len(tokens):
        token = tokens[i]

        # Expecting an operation
        if token == "plus":
            operation = "plus"
            i += 1
        elif token == "minus":
            operation = "minus"
            i += 1
        elif token == "multiplied":
            if i + 1 < len(tokens) and tokens[i + 1] == "by":
                operation = "multiplied"
                i += 2
            else:
                raise ValueError("syntax error")
        elif token == "divided":
            if i + 1 < len(tokens) and tokens[i + 1] == "by":
                operation = "divided"
                i += 2
            else:
                raise ValueError("syntax error")
        elif token.lstrip("-").isdigit():
            # A number where an operation was expected
            raise ValueError("syntax error")
        else:
            raise ValueError("unknown operation")

        if i >= len(tokens):
            raise ValueError("syntax error")

        try:
            number = int(tokens[i])
        except:
            raise ValueError("syntax error")

        i += 1

        # Left-to-right evaluation
        if operation == "plus":
            result += number
        elif operation == "minus":
            result -= number
        elif operation == "multiplied":
            result *= number
        elif operation == "divided":
            result //= number

    return result
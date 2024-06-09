def is_balanced_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def contains_only_valid_characters(expression):
    valid_chars = set("0123456789+-*/() ")
    for char in expression:
        if char not in valid_chars:
            return char
    return None

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
    except SyntaxError:
        return "Error: Operand error or invalid syntax."
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Arithmetic Expression Evaluator")
    print("Enter 'q' to quit.")

    while True:
        expression = input("Enter an arithmetic expression: ").strip()
        if expression.lower() == 'q':
            break

        invalid_char = contains_only_valid_characters(expression)
        if invalid_char:
            if invalid_char == '^':
                print("Error: Unsupported character ^")
            elif invalid_char == '%':
                print("Error: Unsupported character %")
            else:
                print(f"Error: Unsupported character {invalid_char}")
            continue

        if not is_balanced_parentheses(expression):
            print("Error: Unbalanced parentheses.")
            continue

        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()

#會計系 H14126173 賈閔之
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    line_1 = []
    line_2 = []
    dash = []
    result = []

    for problem in problems:
        parts = problem.split()
        first, operator, second = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        width = max(len(first),len(second)) +2

        line_1.append(f"{first:>{width}}")
        line_2.append(f"{operator} {second:>{width - 2}}")
        dash.append('-' * width)
        
        # Calculate result and proper width
        if show_answers:
            computed_result = str(int(first) + int(second)) if operator == '+' else str(int(first) - int(second))
            result.append(f"{computed_result:>{width}}")

    # Use '\n'.join for cleaner formatting
    rows = [
        "    ".join(line_1),
        "    ".join(line_2),
        "    ".join(dash)
    ]

    if show_answers:
        rows.append("    ".join(result))

    arranged_problem = '\n'.join(rows)
    return arranged_problem

# Test
print(arithmetic_arranger(["1 + 2", "1 - 9380"], True))

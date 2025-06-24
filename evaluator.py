def calculate_output(equation):
    """
    Evaluates a string math equation.
    Returns result as a string or 'Error' if evaluation fails.
    """
    try:
        answer = str(eval(equation))
        return answer
    except Exception:
        return "Error"

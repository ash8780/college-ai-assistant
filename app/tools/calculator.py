def calculate(expression: str):
    allowed = set("0123456789+-*/%.() ")

    if not expression or any(ch not in allowed for ch in expression):
        return {"error": "Only basic mathematical expressions are allowed."}

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return {"expression": expression, "result": result}
    except (SyntaxError, ZeroDivisionError, TypeError) :
        return {"error": "Invalid mathematical expression."}


def attendance_percentage(attended: float, total: float):
    if total <= 0 or attended < 0 or attended > total:
        return {"error": "Enter valid attendance numbers."}

    percentage = (attended / total) * 100

    return {
        "attended_classes": attended,
        "total_classes": total,
        "percentage": round(percentage, 2),
    }

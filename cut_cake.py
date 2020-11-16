def cut_cake(parts):
    try:
        return 1 / int(parts)
    except (ZeroDivisionError, TypeError, ValueError):
        return "Are you crazy?!"

cake = cut_cake([1])
print(cake)

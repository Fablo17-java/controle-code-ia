# mycode.py — version initiale (contient des défauts à trouver)


def division(a, b):
    """Divise a par b et retourne le résultat."""
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être nul.")
    return a / b


def factorielle(n):
    """Calcule la factorielle de n (récursif)."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n doit être un entier positif ou nul.")
    if n == 0:
        return 1
    return n * factorielle(n - 1)

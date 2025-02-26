def add(a, b):
    """Ajoute deux nombres."""
    return a + b

def multiply(x, y):
    """Multiplie deux nombres."""
    return x * y

def divide(x, y):
    """Divise x par y en évitant la division par zéro."""
    if y != 0:
        return x / y
    return None  # Bonne pratique : retourner une valeur explicite en cas d'erreur

def greet(name):
    """Renvoie un message de salutation."""
    if not name:  # Vérifie si name est vide ou None
        return "Hello, World!"
    return f"Hello, {name}"

import math


# GÉOMETRIE

# cette partie regroupe de nombreux concepts de géometrie
# je vais donc transcrire en premier lieu la géometrie dans un contexte algorithmique.

# Définitions et concepts de base

# point en 2 dimensions

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, t):
        self.x += t.x
        self.y += t.y

    def __sub__(self, t):
        self.x -= t.x
        self.y -= t.y

    def __mul__(self, t):
        self.x *= t.x
        self.y *= t.y

    def __truediv__(self, t):
        self.x /= t.x
        self.y /= t.y

    def dot(self, t):
        return self.x * t.x + self.y * t.y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, t):
        self.x += t.x
        self.y += t.y
        self.z += t.z

    def __sub__(self, t):
        self.x -= t.x
        self.y -= t.y
        self.z -= t.z

    def __mul__(self, t):
        self.x *= t.x
        self.y *= t.y
        self.z *= t.z

    def __truediv__(self, t):
        self.x /= t.x
        self.y /= t.y
        self.z /= t.z

    def dot(self, t):
        return self.x * t.x + self.y * t.y + self.z * t.z

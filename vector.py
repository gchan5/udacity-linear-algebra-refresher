import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    """Return sum of this and v's coordinates"""
    def addition(self, v):
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    """Return difference of this and v's coordinates"""
    def subtract(self, v):
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])
    
    """Return product of this coordinate by multiplier"""
    def scalar_mult(self, multiplier):
        return Vector([i*multiplier for i in self.coordinates])

    """Return length of this vector"""
    def magnitude(self):
        total = 0

        for i in self.coordinates:
            total += i*i

        return math.sqrt(total)
    
    """Return normalization of this vector"""
    def direction(self):
        mag = self.magnitude()

        if mag == 0:
            return 0
        else:
            return self.scalar_mult(1/mag)

    """Return dot_product of this vector with v1"""
    def dot_product(self, v1):
        return sum([x*y for x,y in zip(self.coordinates, v1.coordinates)])


    """Return angle of this vector with v1"""
    def angle(self, v1, radian):
        v_n = self.direction()
        v1_n = v1.direction()
        dot = round(v_n.dot_product(v1_n), 3)

        if radian:
            return math.acos(dot)
        else:
            return math.acos(dot) * (180./math.pi)

    """Check if this vector is parallel with v1"""
    def parallel(self, v1):
        return (self.angle(v1, True) == 0 or self.angle(v1, True) == math.pi)

    """Check if this vector is orthogonal with v1"""
    def orthogonal(self, v1, tolerance=1e-10):
        return abs(self.dot_product(v1)) < tolerance

    """Return projection of v1 onto this vector"""
    def proj(self, v1):
        normalized = self.direction()
        proj_length = v1.dot_product(normalized)

        return normalized.scalar_mult(proj_length)
    
    """Return component of v1 orthogonal to this vector"""
    def proj_orth(self, v1):
        proj_v1 = self.proj(v1)
        return v1.subtract(proj_v1)

    """Return cross product of this vector and v1"""
    def cross_product(self, v1):
        product = []
        product.append((self.coordinates[1]*v1.coordinates[2]) - (v1.coordinates[1] * self.coordinates[2]))
        product.append(-1 * ((self.coordinates[0] * v1.coordinates[2]) - (v1.coordinates[0] * self.coordinates[2])))
        product.append((self.coordinates[0]*v1.coordinates[1]) - (v1.coordinates[0] * self.coordinates[1]))

        return Vector(product)

    """Return area of parallelogram created by cross product of this vector and v1"""
    def area_parallelogram(self, v1):
        return self.cross_product(v1).magnitude()

    """Return area of triangle created by cross product of this vector and v1"""
    def area_triangle(self, v1):
        return 0.5 * self.area_parallelogram(v1)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    



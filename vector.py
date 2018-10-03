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

    def addition(self, v):
        return [x+y for x, y in zip(self.coordinates, v.coordinates)]

    def subtract(self, v):
        return [x-y for x, y in zip(self.coordinates, v.coordinates)]
        
    def scalar_mult(self, multiplier):
        return [i*multiplier for i in self.coordinates]

    def magnitude(self):
        return 0
    
    def direction(self):
        return 0

if __name__ == "__main__":
    v = Vector([2, 2, 2])
    v2 = Vector([3, 3, 3])

    print(v.addition(v2))
    print(v.subtract(v2))
    print(v.scalar_mult(2))
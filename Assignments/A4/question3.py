class Circle:
    def __init__(self, center, radius):
        self.center = center  # center is a tuple (x, y)
        self.radius = radius

    def concentric(self, another_circle):
        '''
         Two circles are concentric if they share the same center.
        :param another_circle:
        :return: boolean
        '''
        return self.center == another_circle.center

    def intersects(self, another_circle):
        from math import sqrt
        '''
        Calculate the distance between the centers of the two circles.
        Circles intersect if the distance between centers is less than or equal to the sum of their radii
        and greater than or equal to the absolute difference of their radii.
        
        :param another_circle:
        :return: boolean
        '''

        distance_centers = sqrt((self.center[0] - another_circle.center[0]) ** 2 + (self.center[1] - another_circle.center[1]) ** 2)

        # Calculate the sum and the absolute difference of the radii
        sum_radii = self.radius + another_circle.radius
        diff_radii = abs(self.radius - another_circle.radius)

        return diff_radii <= distance_centers <= sum_radii

    def remap(self, percentage):
        '''
        Change the radius by the given percentage
        :param percentage:
        :return: update local vatiable
        '''

        self.radius *= (1 + percentage / 100)

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"


circle1 = Circle((0, 0), 5)
circle2 = Circle((0, 0), 10)
circle3 = Circle((10, 0), 7)

print(circle1.concentric(circle2))  # True
print(circle1.intersects(circle3))  # True
circle1.remap(20)  # Increase radius by 20%
print(circle1)  # Circle(center=(0, 0), radius=6.0)
circle1.remap(-50)  # Decrease radius by 50%
print(circle1)  # Circle(center=(0, 0), radius=3.0)

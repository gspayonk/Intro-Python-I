# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def _init_(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def _init_(self, name, lat, lon):
        super()._init_(lat, lon)
        self.name = name
    
    def _str_(self):
        return f'{self.name} is at ({self.lat}, {self.lon})'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def _init_(self, name, difficulty, size, lat, lon):
        super()._init_(name, lat, lon)
        self.size = size
        self.difficulty = difficulty

    def _str_(self):
        return f'{self.name} is at ({self.lat}, {self.lon}) and has difficulty {self.difficulty}.'
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint._str_())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache._str_())

earth_year_per_year_on = {
    'Earth': 1.0,
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132
}
def get_years_on(planet):
    return lambda self: round(self._years_on_earth /
                              earth_year_per_year_on[planet], 2)
class SpaceAge(object):
    on_earth = get_years_on('Earth')
    on_mercury = get_years_on('Mercury')
    on_venus = get_years_on('Venus')
    on_mars = get_years_on('Mars')
    on_jupiter = get_years_on('Jupiter')
    on_saturn = get_years_on('Saturn')
    on_uranus = get_years_on('Uranus')
    on_neptune = get_years_on('Neptune')
    def __init__(self, seconds):
        self.seconds = float(seconds)
        self._years_on_earth = self.seconds / 31557600
      
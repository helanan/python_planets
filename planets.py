print("------------Planets----------------")
planets = ['Mars', 'Venus', 'Mercury', 'Uranus']
planets.append('Jupiter')
planets.append('Saturn')
planets.insert(0, 'Earth')
planets.insert(1, 'Venus')
planets.append('Pluto')
for planet in planets:
    print(planet.title())

print("------------rocky planets----------------")
rocky_planets = planets[0:3]
for rocky_planet in rocky_planets:
    print(str(rocky_planet) + " is a Rocky Planet")

print("----------------------------")
print("Uh oh! Small Dwarf Discovered, planet must be removed!")
planets.remove('Pluto')

print("------------Updated planets----------------")
for planet in planets:
    print(planet.title())

print("------------spacecrafts to deploy----------------")
launched_spacecrafts = ['Apollo', 'Titan', 'Saturn V', 'Buran', 'Vostok', 'Gemini']
for launched_spacecraft in launched_spacecrafts:
    print(launched_spacecraft.title())

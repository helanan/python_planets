# python_planets

Using python to display planets in lists utilizing concepts like Tuples:

- Use append() to add Jupiter and Saturn at the end of the list.
- Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
- Use insert() to add Earth, and Venus in the correct order.
- Use append() again to add Pluto to the end of the list.
- Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
- Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

Iterating over planets

- Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
- Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.

import ninja, pets


ninja_bob = ninja.Ninja("Bob", "Ninja", 25, 100, pets.Pet("Charlie", "Iguana", "Bluuuuurrrrrpppp", ["lay down", "sleep", "poop"], 1000, 500))
ninja_bob.feed().walk().bathe()
print(f"{ninja_bob.pet.name}'s energy is {ninja_bob.pet.energy}")

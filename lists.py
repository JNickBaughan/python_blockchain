dogs = ['Oliver', 'Gibson']

dogs.append("Finn")

print(dogs)

# accessing is by value, not reference
print(dogs[0] + " the French Bulldog")

dogs[2] = "Finnegan"

print(dogs)

puppy = [dogs.pop()]

print(dogs)

print(puppy)


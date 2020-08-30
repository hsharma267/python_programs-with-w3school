# Python Iterator

print("-- Python Iterator --")

# Iterator vs Iterable

print("-- Iterator example --")

mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

print("-- Iterable example --")

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an Iterator

print("-- Looping through an Iterator --")
print("-- Iterator example --")

mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)
for x in myit:
    print(x)

print("-- Iterable example --")

mystr = "banana"
myit = iter(mystr)
for x in myit:
    print(x)

# Create an Iterator

print('-- Create an Iterator --')


class Mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


mynum = Mynumber()
myit = iter(mynum)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Stop Iteration

print("-- Stop Iteration --")


class MynumberClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


mynum = MynumberClass()
myit = iter(mynum)
for x in myit:
    print(x)

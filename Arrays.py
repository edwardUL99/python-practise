import random

class Arrays:
    def __init__(self, array = []):
        self.array = array

    def add(self, element):
        self.array.append(element)

    def length(self):
        return len(self.array)

    def shuffle(self):
        for x in range(0, self.length()):
            temp = self.array[x]
            pos = random.randint(0, self.length() - 1)
            self.array[x] = self.array[pos]
            self.array[pos] = temp

    def display(self):
        print(self.array)


    

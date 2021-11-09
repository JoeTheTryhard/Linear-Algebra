from sys import exit
from traceback import format_exc

class Vector():
    def __init__(self, liste):
        try:
            self.entries = liste.copy()
            self.lenght = len(self.entries)
            for value in self.entries:
                if type(value) in (int, float):
                    pass
                else:
                    raise TypeError
        except(TypeError):
            self.error("This Vector is not made exclusively out of interger or floats.")
       
    def __add__(self, other):
        if type(other) is Vector:
            try:
                if other.lenght == self.lenght:
                    liste = []
                    for i in range(1, self.lenght+1):
                        liste.append(self.index(i) + other.index(i))
                    return Vector(liste)
                else:
                    raise ValueError
            except(ValueError):
                self.error("Vectors have different lenghts")
    
    def __mul__(self, other):
        if type(other) in (int, float):
            liste = []
            for entry in self.entries:
                liste.append(entry*other)
            return Vector(liste)
    
    def __sub__(self, other):
        if type(other) is Vector:
            return self + other *-1

    def __truediv__(self, other):
        if type(other) in (float, int):
            return self * (1/other)
                
    def index(self, integer):
        try:
            return self.entries[integer-1]
        except(IndexError):
            self.error("This Index doesn't have a value in this Vector")


    def error(self, message):
        ''' Debbugging tool, should not be pampered with'''
        TraceBack = format_exc()
        position = TraceBack.find('\n', 35)
        TraceBack = TraceBack[0:position]
        print("\n"+ TraceBack + "\n" + "Vector Error: " + message + "\n")
        exit(1)

    def display(self):
        for entry in self.entries:
            print("|" + str(entry) + "|", end="\n")
    
    def dot(self, other):
        try:
            if self.lenght == other.lenght:
                tmp = []
                for i in range(1, self.lenght+1):
                    tmp.append(self.index(i) + other.index(i))
                return Vector(tmp)
            else:
                raise ValueError

        except(ValueError):
            self.error("Vectors have different lenghts ({} != {})".format(self.lenght, other.lenght))



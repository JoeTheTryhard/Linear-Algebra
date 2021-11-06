from sys import exit
from traceback import format_exc
from VectorClass import Vector

class Matrix(): # This class uses the vector class in order to do certain operations and so they are needed to import this class
    def __init__(self, list_o_lists):
        try:
            self.entries = list_o_lists.copy() #Stores the list of list in a other variable without having them be linked
            self.rows, self.columns = len(self.entries), len(self.entries[0]) #Assigns the number ofrows to be the lenght of the list and the number of rows to be the number of entries in the FIRST
            self.rowXcol = str(self.rows) + "x"+ str(self.columns)

            for liste in self.entries: #Check if the list of list contains identical number of entries
                if len(liste) == self.columns:
                    for entry in liste:
                        if type(entry) in (float, int):
                            pass #This is what we want to happend, This is a Matrix
                        else:
                            raise TypeError("Type of structure not compatible") #Entries aren't floats or integers
                            
                else:
                    raise ValueError("Entries in structure not compatible") #Rows with different lenghts
        
        except(TypeError):
            self.error("This Matrix is not made exclusively out of interger or floats.")

        except(ValueError):
            self.error("This Matrix has rows with different lenghts.")

    def __add__(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Does Matrix Addition following the conventional rules. If the matrix do not have the same dimension, it will Crash the program instead'''
        try:
            if type(other) is Matrix:
                if self.rowXcol == other.rowXcol:
                    new_rows = []
                    for i in range(1, self.rows+1): # Range excludes the last terms so by adding 1, i will be equal to the last term
                        new_column = []
                        for j in range(1, self.columns+1):
                            new_column.append(self.index([i, j]) + other.index([i, j]))
                        new_rows.append(new_column)
                    return Matrix(new_rows)
                else:
                    raise TypeError
        except:
            self.error("The Two Matrices do not have the same dimension ({} and {})".format(self.rowXcol, other.rowXcol))

    def __mul__(self, other): #Note that multiplication in python is not commutative, you might think that it is but really, classes are all made with each other in mind and my new matrix wasn't intended to be multiplied with ints
        if type(other) in (int, float):
            ''' (Matrix, Scalar) -> Matrix
            Does Matrix-Scalar Multiplication following the conventional rules.'''
            new_rows = []
            for i in range(1, self.rows+1): # Range excludes the last terms so by adding 1, i will be equal to the last term
                new_column = []
                for j in range(1, self.columns+1):
                    new_column.append(self.index([i, j]) * other)
                new_rows.append(new_column)
            return Matrix(new_rows)
        
        if type(other) is Vector:
            try:
                if self.rows == other.lenght: #Check if the number of rows in the matrix is equal to the lenght of the Vector, this is a prerequesite for matrix-vector multiplication
                    tmp = []
                    for nmb_of_zeros in range(1, self.rows+1):
                        tmp.append(0)
                    sumVect = Vector(tmp)
                    for i in range(1, self.rows+1):
                        sumVect += Vector(self.column(i)) * other.index(i)
                    return sumVect
                else: 
                    raise(ValueError)
            except(ValueError): 
                self.error("Matrix and vector have of different sizes (Matrix size: {} and Vector lenght: {}".format(self.rowXcol, other.lenght))

        if type(other) is Matrix:
            try:
                if self.columns == other.rows:
                    liste = []
                    for i in range(1, other.columns+1):
                        print(other.column(i))
                        partVect = self * Vector(other.column(i))
                        partVect.display()
                        liste.append(partVect.entries)
                    print(liste)
                    return Matrix(liste)
                else: raise ValueError
            except (ValueError): 
                self.error("Matrix of different row-column number (Matrix1 size: {} and Matrix 2 size: {}".format(self.rowXcol, other.rowXcol))
               
    def __sub__(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Does Matrix Substraction following the conventional rules. If the matrix do not have the same dimension, it will Crash the program instead'''
        return self + other*-1

    def __truediv__(self, other):
        if type(other) in (int, float):
            ''' (Matrix, Scalar) -> Matrix
            Does Matrix-Scalar Multiplication following the conventional rules.'''
            new_rows = []
            for i in range(1, self.rows+1): # Range excludes the last terms so by adding 1, i will be equal to the last term
                new_column = []
                for j in range(1, self.columns+1):
                    new_column.append(self.index([i, j]) * (1/other))
                new_rows.append(new_column)
            return Matrix(new_rows)

    def error(self, message):
        ''' Debbugging tool, should not be pampered with'''
        TraceBack = format_exc()
        position = TraceBack.find('\n', 35)
        TraceBack = TraceBack[0:position]
        print("\n"+ TraceBack + "\n" + "Matrix Error: " + message + "\n")
        exit(1)    

    def display(self):
        ''' Prints the Matrix like a usual Mathematical Matrix'''
        for column in self.entries:
            print("|", end=" ")
            for entry in column:
                print(entry, end=" ")
            print("|")

    def index(self, coordinates):
        '''(Liste or Tuple of Numbers) -> Numerical Value
        Returns the value at the associated position. If coordinates aren't Tuples or list or coordinates out of range, it will return None'''
        if type(coordinates) in (list, tuple):
            i, j = coordinates[0], coordinates[1]
            try:
                return self.entries[i-1][j-1]
            except(IndexError):
                self.error("Matrix Error: Row or column does not exist. (Goes from A_sub(1,1) to A_sub(m,n))")

        else:
            return None
    
    def row(self, integer):
        try:
            row = self.entries[integer-1]
            return row
        except(IndexError):
            self.error("This Matrix has no corresponding row #{}".format(integer))

    def column(self, integer):
        try:
            column = []
            for i in range(1, self.columns+1):
                column.append(self.entries[i-1][integer-1])
            return column
        except(IndexError):
            self.error("This Matrix has no corresponding column #{}".format(integer))




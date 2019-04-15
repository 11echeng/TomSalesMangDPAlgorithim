class Tom:

   def  __init__(self, total_units, days, maximum):
       self.total_units = total_units
       self.days = days
       self.maximum = maximum
       self.maximum.insert(0,0)

   def checkConditions(self):
       if self.total_units < self.days:
           self.null = 0
           print(self.null)
       if len(self.maximum) > self.days:
           self.null = 0
           return None

   def initiateMatrix(self):
        self.M = [[0] * (self.total_units + 1) for i in range(self.days + 1)]
        # Initialize the matrix to fill in 0’s for day = 0
        for i in range(1, self.days + 1):
             for j in range(1, self.total_units + 1):
               if i == 1:
                   for k in range(1,self.maximum[i]+1):
                       if k <= j:
                        self.M[i][k] = 1
               if i == j:
                    self.M[i][j] = 1
        return self.M

   def solution(self):
       for i in range(2, self.days + 1):
           for j in range(i + 1,self.total_units + 1):
               for k in range(1,self.maximum[i]+1):
                    if k < j :
                        self.M[i][j] += self.M[i - 1][j - k]
                        self.solution = self.M[self.days][self.total_units]
       return self.solution

   def printSolution(self):
        modular = 10**9 + 7
        print(self.solution % modular)

total_units = int(input())
days = int(input())
values = input()
maximum = [int(value) for value in values.split()]

g = Tom(total_units, days, maximum)
g.checkConditions()
g.initiateMatrix()
g.solution()
g.printSolution()



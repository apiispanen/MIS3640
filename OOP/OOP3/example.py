class City:
    
    def __init__(self, passing_name = "Unknown", pop = 0, gdp = 0):
        self.name = passing_name
        self.population = pop
        self.gdp_per_capita = gdp

    def __str__(self):
        return "{} has {} people, with gdp per capita of ${}.".format(self.name, self.population,self.gdp_per_capita)
    
    def __gt__(self, other):
        if self.gdp_per_capita > other.gdp_per_capita:
            return True
        elif self.gdp_per_capita == other.gdp_per_capita:
            if self.population > other.population:
                return True
        else:
            return False  
        
    def __add__(self, other):
        total_city = City("{} and {} together".format(self.name, other.name), self.population+other.population, self.gdp_per_capita+other.gdp_per_capita)
        return total_city

    def __eq__ (self, other):
        return self.population == other.population and self.gdp_per_capita == other.gdp_per_capita

city1 = City("New York", 8537000, 50000000)
print(city1)
print(city1.name)
print()

Boston = City("Boston", 300000, 50000000)

print (city1 > Boston)

print(city1+Boston)
print(city1==Boston)

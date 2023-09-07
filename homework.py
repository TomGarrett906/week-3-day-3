#1=============================================================================
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
print(list(filter(lambda p: p.strip() != "", places))) 




#2=============================================================================
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda l_name: l_name.split()[-1].lower())
print(author)

#  OR

# def authors(l_name):
#     return l_name.split()[-1].lower()

# last_names = [(authors(f_name), author) for f_name in author]
# last_names_sorted = [name[1] for name in last_names ]



#3=============================================================================
cities = [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)] 
temp_convert =  list(map(lambda c: (c[0], (9/5)*c[1] + 32), cities))

print(temp_convert)




#4=============================================================================
# Output for fib(5) =>  Iteration 0: 1 Iteration 1: 1 Iteration 2: 2 Iteration 3: 3 Iteration 4: 5 Iteration 5: 8
def fib_function(i, iteration = 0, a = 0, b = 1):
    if iteration == i:
        return f'Interation {iteration} {b}\n'
    return f'Interation {iteration}: {b}| ' + fib_function(i, iteration +1, b, a + b)

fib = fib_function(5)

print(fib)
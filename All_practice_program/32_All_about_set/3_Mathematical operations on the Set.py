
# 1.union(): We can use this function to return all elements present in both sets.
# Syntax : x.union(y) 0r x|y

x = {10,20,30,40}
y = {30,40,50,60}
z = {50,60,70}
print(x.union(y))       # {40, 10, 50, 20, 60, 30}
print(x|y)              # {40, 10, 50, 20, 60, 30}
print(x|z)              # {50, 20, 70, 40, 10, 60, 30}


# 2. intersection() : return common element present in both set.
# Syntax : x.intersection(y)   or  x&y

p = {10,20,30,40}
q = {30,40,50,60}
r = {50,60,70}

print(p.intersection(q))                # {40, 30}
print(p&q)                              # {40, 30}
print(p.intersection(r))                # set()


# 3. difference() : returns the element present in x but not in y.
# syntax : x.difference(y)   or x-y

a = {10,20,30,40}
b = {30,40,50,60,80,99}
c = {50,60,70}

print(a.difference(b))      # {10, 20}
print(a-b)                  # {10, 20}
print(b-a)                  # {80, 50, 99, 60}
print(c-b)                  # {70}


# 4. symmetric difference() : Returns elements present in either x or y but not in both.
# Syntax : x.symmetric_difference(y) or x^y

s = {10,20,30,40}
t = {30,40,50,60}

print(x.symmetric_difference(y))    # {10,60,50,20}
print(x^y)                          # {10, 50, 20, 60}
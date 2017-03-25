from HaPy import SchdgerEngine

a = [1.1, 2.2, 4.4, 8.8, 4.4, 2.2, 1.1]

r1, r2 = SchdgerEngine.solve(a, a, 1.0, 2)
p1 = SchdgerEngine.schrodinger(a, a, 1.0)
p2 = SchdgerEngine.schrodinger(p1[0], p1[1], 1.0)

print(r1)
print(p1)
print(r2)
print(p2)
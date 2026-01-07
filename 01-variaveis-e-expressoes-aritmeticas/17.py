inv1 = float(input())
inv2 = float(input())
inv3 = float(input())
premio = float(input())
total = inv1 + inv2 + inv3
r1 = (inv1/total) * premio
r2 = (inv2/total) * premio
r3 = (inv3/total) * premio
print(f"{r1:.2f}")
print(f"{r2:.2f}")
print(f"{r3:.2f}")
radius = 42
point_1 = (23, 34)
point_2 = (30, 30)
S = radius**2 * 3.1415926
S = round(S,4)
M = point_1 = (23**2 + 34**2)**0.5
print("S = ", S)
if M < radius:
    print("Точка M находится внутри кругa")
else:
    print("Точка М не находится внутри круга")
N = (30**2 + 30**2) ** 0.5
if N < radius:
    print("Точка N находится внутри кругa")
else:
    print("Точка N не находится внутри круга")
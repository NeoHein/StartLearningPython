C = {"#": 0, "1:Handset": 250, "2:Keypad": 20, "3:PC": 300, "4:Laptop": 400, "5:Radio": 10}
c = list(C)
n = int(input("Enter number"))
N = c[n]
print(N)
if N == C:
    print(C["N"])
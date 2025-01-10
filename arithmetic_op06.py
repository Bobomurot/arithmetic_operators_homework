# n  deb nomlangan o'zgaruvchi yarating va besh  xonali turli xil raqamni belgilang
n = 98468
# n sonining raqamlar yig'indisni toping va uni sum deb nomlangan o'zgaruvchiga belgilang.
x1 = n // 10000
x2 = (n % 10000) // 1000
x3 = (n % 1000) // 100
x4 = (n % 100) // 10
x5 = n % 10
sub = x1 + x2 + x3 + x4 + x5
# n sonining raqamlar ko'paymasini toping va uni k deb nomlangan o'zgaruvchiga belgilang.
k = x1 * x2 * x3 * x4 * x5
# total deb nomlangan o'zgaruvchi yarating va k ning qiymatini sum qiymatiga butunli bo'ling. 
total = k // sub
# total o'zgaruvchisining natijasini chiqaring.
print(total)
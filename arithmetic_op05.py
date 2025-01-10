# n  deb nomlangan o'zgaruvchi yarating va unga to'rt xonali raqamni belgilang
n = 9287
# n sonining teskarisini toping va uni total deb nomlangan o'zgaruvchiga belgilang.
x1 = n // 1000
x2 = (n % 1000) // 100
x3 = (n % 100) // 10
x4 = n % 10
# sub deb nomlanga o'zgaruvchi yarating va dastlabki n qiymatdan keyingi total qiymatni ayirmasini ta'minlang.
teskari_son = x4 * 1000 + x3 * 100 + x2 * 10 + x1

sub = teskari_son + n
# sub o'zgaruvchisini chiqaring
print(sub)
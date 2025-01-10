# n deb nomlangan o'zgaruvchi yarating va unga uch xonali raqamni belgilang.
n = 357
# n ning birinchi raqamini toping va x1 ga belgilang.
x1 = n // 100
# n ning ikkinchi raqamini toping va x2 ga belgilang.
x2 = n // 10 % 10
# n ning uchinchi raqamini toping va x3 ga belgilang.
x3 = n % 10
# total deb nomlangan o'zgaruvchi yarating va unga (x1 + x2 * x3) ushbu ifodani ta'minlan.
total = (x1 + x2 * x3)
# total qiymatini chop eting.
print(total)
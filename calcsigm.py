import math

def avgnums(nums, count):
    return nums/count

def sigma(aveg, lst, ite):
    ans = 0.0
    c = 0
    while(c < ite):
        ans += (lst[c] - aveg)*(lst[c] - aveg)
        c += 1
    ans = ans/ite
    return math.sqrt(ans)
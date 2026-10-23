class Solution:

  def divide(self, dividend: int, divisor: int) -> int:
    if dividend == divisor:
      return 1
    if dividend == -2 ** 31 and divisor == -1:
      return (2 ** 31) - 1

    if divisor == 1:
      return dividend

    is_negative = (dividend < 0) ^ (divisor < 0)

    n, d = abs(dividend), abs(divisor)
    ans = 0

    while n >= d:
      p = 0
      while n >= (d << p):
        p += 1
      p -= 1
      n -= (d << p)
      ans += 1 << p

    if is_negative:
      ans = -ans

    return min(max(ans, -2 ** 31), 2 ** 31 - 1)
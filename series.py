import math
import time
N = int(input('N: '))
start_time = time.time()
def p(N):
  s = set(range(2, N))
  for i in range(2, int(math.sqrt(N))):
    if i in s:
      s -= set(range(2*i, N, i))
  f = len(s)
  print(f'Found: {f}')
  print(f'Percent: {100/N*f}')
  return s
p(N)
print(f'Limit ----- {N} -----')
print(f'Exetime: {(time.time() - start_time)}')

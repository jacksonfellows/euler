#include <stdio.h>

int factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

int digit_factorial_sum(int n)
{
  int sum = 0;
  for (int r = n % 10; n > 0; n /= 10, r = n % 10) {
    sum += factorial[r];
  }
  return sum;
}

int chain_len(int n)
{
  for (int len = 0; ; len += 1, n = digit_factorial_sum(n)) {
    switch (n) {
    case 1:      return len + 1;
    case 2:      return len + 1;
    case 145:    return len + 1;
    case 169:    return len + 3;
    case 363601: return len + 3;
    case 1454:   return len + 3;
    case 871:    return len + 2;
    case 45361:  return len + 2;
    case 872:    return len + 2;
    case 45362:  return len + 2;
    case 40585:  return len + 1;
    }
  }
}

int main()
{
  int num_len_60_chains = 0;
  for (int n = 1; n < 1000000; ++n) {
    if (chain_len(n) == 60)
      ++num_len_60_chains;
  }
  printf("%d\n", num_len_60_chains);
  return 0;
}

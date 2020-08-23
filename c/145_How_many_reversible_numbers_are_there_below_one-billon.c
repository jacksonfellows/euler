#include <stdio.h>

int reverse(int n)
{
  int r, d;
  r = 0;
  while (n > 0) {
    d = n % 10;
    n /= 10;
    r = r*10 + d;
  }
  return r;
}

int all_odd(int n) {
  int d;
  while (n > 0) {
    d = n % 10;
    n /= 10;
    if (d % 2 == 0)
      return 0;
  }
  return 1;
}

int reversible(int n) {
  return n % 10 == 0 ? 0 : all_odd(n + reverse(n));
}

int main()
{
  int n = 0;
  for (int i = 0; i < 1000000000; ++i) {
    if (reversible(i))
      ++n;
  }
  printf("%d\n", n);
}

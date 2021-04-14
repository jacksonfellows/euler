#include <stdio.h>
#include <stdlib.h>

long reverse(long n) {
  long r, d;
  r = 0;
  while (n > 0) {
    d = n % 10;
    n /= 10;
    r = r * 10 + d;
  }
  return r;
}

long all_odd(long n) {
  long d;
  while (n > 0) {
    if (n % 2 == 0)
      return 0;
    n /= 10;
  }
  return 1;
}

int reversible(long n) { return n % 10 == 0 ? 0 : all_odd(n + reverse(n)); }

int main(int argc, char **argv) {
  long n = 0;
  long l = strtol(argv[1], NULL, 10);
  for (long i = 0; i < l; ++i) {
    if (reversible(i))
      ++n;
  }
  printf("%ld\n", n);
}

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long n_divs(long n) {
  long c = 0;
  long isqrt = (long)sqrt(n);
  long i;
  for (i = 1; i <= isqrt; i++) {
    if (n % i == 0)
      c += 2;
  }
  if (n % (i - 1) == 0 && n / (i - 1) == (i - 1))
    --c;
  return c;
}

int main(int argc, char **argv) {
  long l = strtol(argv[1], NULL, 10);
  long past, curr;
  past = 1;
  long n = 0;
  for (long i = 2; i < l; i++) {
    curr = n_divs(i);
    if (curr == past) {
      ++n;
    }
    past = curr;
  }
  printf("%ld\n", n);
  return 0;
}

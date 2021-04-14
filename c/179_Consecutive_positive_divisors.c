#include <math.h>
#include <stdio.h>

#define N 10000000

int divs[N + 1];

long n_divs(long n) {
  int c = 0;
  if (n % 2 == 0) {
    do {
      n /= 2;
      ++c;
    } while (n % 2 == 0);
    return (c + 1) * divs[n];
  }
  long isqrt = (long)sqrt(n);
  for (long i = 3; i <= isqrt; i += 2) {
    if (n % i == 0) {
      do {
        n /= i;
        ++c;
      } while (n % i == 0);
      return (c + 1) * divs[n];
    }
  }
  return 2;
}

int main(int argc, char **argv) {
  divs[1] = 1;
  divs[2] = 2;

  long count = 0;
  long d;
  for (long n = 3; n <= N; ++n) {
    d = n_divs(n);
    if (d == divs[n - 1])
      ++count;
    divs[n] = d;
  }

  printf("%ld\n", count);
}

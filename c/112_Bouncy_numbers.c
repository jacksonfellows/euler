#include <stdio.h>

int bouncy(int n) {
  int last_d, d, dir;
  last_d = n % 10;
  n /= 10;
  dir = 0;
  while (n > 0) {
    d = n % 10;
    n /= 10;
    if (d > last_d) {
      if (dir == -1)
        return 1;
      dir = 1;
    } else if (d < last_d) {
      if (dir == 1)
        return 1;
      dir = -1;
    }
    last_d = d;
  }
  return 0;
}

int main() {
  int n_bouncy = 0;
  for (int i = 0; ; ++i) {
    if (bouncy(i))
      ++n_bouncy;
    if ((double)n_bouncy/i == 0.99) {
      printf("%d\n", i);
      break;
    }
  }
}

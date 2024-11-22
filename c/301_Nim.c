#include <stdio.h>

int main() {
  int s = 0;
  for (int n = 1; n <= 1<<30; n++) {
    if ((n^(2*n)^(3*n)) == 0) s += 1;
  }
  printf("%d\n", s);
}

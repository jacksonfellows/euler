#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void simulate(int n) {
  double odds[] = {0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, 0.14285714285714285, 0.125, 0.1111111111111111, 0.1, 0.09090909090909091, 0.08333333333333333, 0.07692307692307693, 0.07142857142857142, 0.06666666666666667, 0.0625};
  int n_won = 0;
  for (int g = 0; g < n; g++) {
    int n_blue = 0;
    for (int i = 0; i < sizeof(odds)/sizeof(double); i++) {
      if ((rand() / (double)RAND_MAX) < odds[i]) {
        n_blue++;
      }
    }
    if (n_blue > 7) {
      n_won++;
    }
  }
  printf("won %d out of %d - %g\n", n_won, n, ((double)n_won)/((double)n));
}

int main(int argc, char **argv) {
  printf("seed: %ld\n", time(NULL));
  srand(time(NULL));
  simulate(atoi(argv[1]));
  return 0;
}

#include <cstdio>
#include <vector>

unsigned long gcd(unsigned long a, unsigned long b) {
  if (a == 0) {
    return b;
  }
  return gcd(b % a, a);
}

void find_triples(int N) {
  int max_L = 1500000;
  std::vector<char> T = std::vector<char>(max_L + 1, 0);

  for (unsigned long n = 1; n < N; n++) {
    for (unsigned long m = n + 1; m < N; m++) {
      for (unsigned long k = 1; k < N; k++) {
        unsigned long a = k*(m*m - n*n);
        unsigned long b = k*2*n*m;
        unsigned long c = k*(m*m + n*n);
        unsigned long L = a + b + c;
        if (L > max_L) {
          break;
        }
        if (gcd(m, n) == 1 && !(m % 2 == 1 && n % 2 == 1)) {
          if (L <= max_L) {
            T[L] = T[L] + 1;
          }
        }
      }
    }
  }
  
  std::printf("%d\n", T[12]);
  std::printf("%d\n", T[48]);
  std::printf("%d\n", T[120]);
  std::printf("%ld\n", std::count(T.begin(), T.end(), 1));
}

int main(int argc, char **argv) {
  find_triples(std::atoi(argv[1]));
}

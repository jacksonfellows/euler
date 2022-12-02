#include <algorithm>
#include <cstdio>
#include <vector>

std::vector<int> primes_under(int N) {
  std::vector<int> primes = std::vector<int>();
  std::vector<bool> sieve = std::vector<bool>(N, 1);
  for (int i = 2; i < N; i++) {
    if (sieve[i]) {
      primes.push_back(i);
      for (int j = i + i; j < N; j += i) {
        sieve[j] = 0;
      }
    }
  }
  return primes;
}

int prime_sums_rec(std::vector<int> primes, int N, int min) {
  int sums = std::binary_search(primes.begin(), primes.end(), N);
  for (int i = 0; primes[i] <= N - primes[i]; i++) {
    if (primes[i] < min) {
      continue;
    }
    sums += prime_sums_rec(primes, N - primes[i], primes[i]);
  }
  return sums;
}

int prime_sums(std::vector<int> primes, int N) {
  return prime_sums_rec(primes, N, 0);
}

int main(int argv, char **argc) {
  std::vector<int> primes = primes_under(100);
  for (int i = 2; i <= 100; i++) {
    int sums = prime_sums(primes, i);
    if (sums >= 5000) {
      std::printf("%d\n", i);
      break;
    }
  }
}

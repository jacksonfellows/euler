#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef uint64_t elem_t;

elem_t *alloc_bit_array(size_t n_bits) {
  return malloc(sizeof(elem_t) * (n_bits / (8 * sizeof(elem_t)) + 1));
}

void set_to_even_odd(elem_t *bit_array, size_t n_bits) {
  for (size_t i = 0; i < n_bits / (8 * sizeof(elem_t)) + 1; i++) {
    bit_array[i] = 0xAAAAAAAAAAAAAAAA;
  }
}

#define get_bit(arr, i) ((arr[i / (8 * sizeof(elem_t))] >> (i % (8 * sizeof(elem_t)))) & 1)

#define zero_bit(arr, i) (arr[(i) / (8 * sizeof(elem_t))] &= ~((elem_t)1 << ((i) % (8 * sizeof(elem_t)))))

struct list_t {
  long x;
  struct list_t *tail;
};

struct list_t *cons(long x, struct list_t *tail) {
  struct list_t *new = malloc(sizeof(struct list_t));
  new->x = x;
  new->tail = tail;
  return new;
}

struct list_t *sieve(long N) {
  elem_t *is_prime = alloc_bit_array(N);
  set_to_even_odd(is_prime, N);
  for (long i = 3; i <= (long)sqrt(N); i += 2) {
    for (; !get_bit(is_prime, i); i += 2);
    for (long j = i*i; j < N; j += 2*i) {
      zero_bit(is_prime, j);
    }
  }
  struct list_t *list = NULL;
  for (long i = 3; i < N; i++) {
    if (get_bit(is_prime, i)) {
      list = cons(i, list);
    }
  }
  return list;
}

void p111() {
  long N = 10000000000;
  /* First, get all primes under sqrt(N). */
  struct list_t *ps = sieve((long)sqrt(N));
  /* Work in chunks. */
  long chunk_len = 1000000;
  elem_t *chunk = alloc_bit_array(chunk_len);
  /* Digit counts! */
  long M[10] = {0};
  long S[10] = {0};
  int n_digits = 10;
  int digit_counts[10];
  for (long start = N / 10; start < N; start += chunk_len) {
    printf("start: %ld\n", start);
    set_to_even_odd(chunk, chunk_len);
    for (struct list_t *head = ps; head != NULL; head = head->tail) {
      long p = head->x;
      for (long i = start - start % p; i < start + chunk_len; i += p) {
        if (i >= start) {
          zero_bit(chunk, i - start);
        }
      }
    }
    for (long i = 0; i < chunk_len; i++) {
      if (get_bit(chunk, i)) {
        long p = start + i;
        /* get digits counts of p */
        for (int i = 0; i < 10; i++) {
          digit_counts[i] = 0;
        }
        long p_ = p;
        for (int i = 0; i < n_digits; i++) {
          digit_counts[p_ % 10]++;
          p_ /= 10;
        }
        for (int d = 0; d < 10; d++) {
          if (digit_counts[d] > M[d]) {
            M[d] = digit_counts[d];
            S[d] = p;
          } else if (digit_counts[d] == M[d]) {
            S[d] += p;
          }
        }
      }
    }
  }
  long S_tot = 0;
  for (int d = 0; d < 10; d++) {
    printf("%d %ld %ld\n", d, M[d], S[d]);
    S_tot += S[d];
  }
  printf("%ld\n", S_tot);
  /* Don't really feel like freeing memory. */
}

int main(int argc, char **argv) {
  p111();
  return 0;
}

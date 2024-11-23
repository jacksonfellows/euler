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
  int x;
  struct list_t *tail;
};

struct list_t *cons(int x, struct list_t *tail) {
  struct list_t *new = malloc(sizeof(struct list_t));
  new->x = x;
  new->tail = tail;
  return new;
}

struct list_t *sieve(int N) {
  elem_t *is_prime = alloc_bit_array(N);
  set_to_even_odd(is_prime, N);
  for (int i = 3; i <= (int)sqrt(N); i += 2) {
    for (; !get_bit(is_prime, i); i += 2);
    for (int j = i*i; j < N; j += 2*i) {
      zero_bit(is_prime, j);
    }
  }
  struct list_t *list = NULL;
  for (int i = 3; i < N; i++) {
    if (get_bit(is_prime, i)) {
      list = cons(i, list);
    }
  }
  /* Reverse list to go smallest to largest. */
  struct list_t *tmp, *head, *next_head;
  tmp = NULL;
  for (head = list; head->tail != NULL; head = next_head) {
    next_head = head->tail;
    head->tail = tmp;
    tmp = head;
  }
  head->tail = tmp;
  return head;
}

long isqrt(long n) {
  return floor(sqrt((double)n));
}

int is_prime_2(int *ps_arr, long n) {
  long n1 = n*n + 1;
  long n3 = n*n + 3;
  long n7 = n*n + 7;
  long n9 = n*n + 9;
  long n13 = n*n + 13;
  long n27 = n*n + 27;

  long n5 = n*n + 5;
  long n11 = n*n + 11;
  long n15 = n*n + 15;
  long n17 = n*n + 17;
  long n19 = n*n + 19;
  long n21 = n*n + 21;
  long n23 = n*n + 23;
  long n25 = n*n + 25;

  int div_counts[] = {0, 0, 0, 0, 0, 0, 0, 0};

  long lim = isqrt(n27);

  for (int i = 0; ps_arr[i] <= lim; i++) {
    if (n1 % ps_arr[i] == 0 || n3 % ps_arr[i] == 0 || n7 % ps_arr[i] == 0 || n9 % ps_arr[i] == 0 || n13 % ps_arr[i] == 0 || n27 % ps_arr[i] == 0) return 0;
    if (n5  % ps_arr[i] == 0) div_counts[0] = 1;
    if (n11 % ps_arr[i] == 0) div_counts[1] = 1;
    if (n15 % ps_arr[i] == 0) div_counts[2] = 1;
    if (n17 % ps_arr[i] == 0) div_counts[3] = 1;
    if (n19 % ps_arr[i] == 0) div_counts[4] = 1;
    if (n21 % ps_arr[i] == 0) div_counts[5] = 1;
    if (n23 % ps_arr[i] == 0) div_counts[6] = 1;
    if (n25 % ps_arr[i] == 0) div_counts[7] = 1;
  }
  return div_counts[0] == 1 && div_counts[1] == 1 && div_counts[2] == 1 && div_counts[3] == 1 && div_counts[4] == 1 && div_counts[5] == 1 && div_counts[6] == 1 && div_counts[7] == 1;
}

int main() {
  long N = 150000000;
  /* long N = 1000000; */
  struct list_t *ps = sieve(N);

  /* Copy "list" to array. */
  int len = 0;
  for (struct list_t *head = ps; head != NULL; head = head->tail) len++;

  int *ps_arr = malloc(len * sizeof(int));
  int i = 0;
  for (struct list_t *head = ps; head != NULL; head = head->tail) ps_arr[i++] = head->x;

  long s = 0;
  for (long n = 10; n < N; n += 10) {
    if (is_prime_2(ps_arr, n)) {
      printf("%ld\n", n);
      s += n;
    }
  }
  printf("sum: %ld\n", s);
}

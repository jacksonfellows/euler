#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <vector>
#include <utility>
#include <cassert>
#include <algorithm>
#include <unordered_set>

typedef uint16_t i_t; // max of 65535

const int MAX_TERMS = 4096;

void print_term(i_t *term, i_t k) {
  for (size_t i = 0; i < k; i++) {
    printf("%d ", term[i]);
  }
  printf("\n");
}

// TODO: will i_t overflow?
std::pair<i_t, i_t> prod_sum(i_t *term, i_t k) {
  i_t prod = 1;
  i_t sum = 0;
  for (size_t i = 0; i < k; i++) {
    prod *= term[i];
    sum += term[i];
  }
  return std::make_pair(prod, sum);
}

bool find_term(std::vector<i_t *> &gen, i_t *search_term, i_t k) {
  for (i_t *term : gen) {
    bool same = true;
    for (i_t i = k; i > 0; i--) {
      if (term[i - 1] != search_term[i - 1]) {
        same = false;
        break;
      }
    }
    if (same) {
      return true;
    }
  }
  return false;
}

i_t find_product_sum(i_t k) {
  // allocate terms
  i_t *terms = (i_t *)malloc(sizeof(i_t) * k * MAX_TERMS);
  // start with all 1'sn
  for (size_t i = 0; i < k; i++) {
    terms[i] = 1;
  }
  i_t *terms_end = &terms[k];
  std::vector<i_t *> gen;
  std::vector<i_t *> prev_gen;
  gen.push_back(terms);             // 1's
  while (1) {
    prev_gen = gen;
    gen.clear();
    // printf("gen (%lu)\n", prev_gen.size());
    // for (i_t *term : prev_gen) {
    // printf("%ad ", (term - terms) / k);
    // }
    // printf("\n");
    // printf("terms:\n");
    // for (i_t *term = terms; term < terms_end; term += k) {
    // print_term(term, k);
    // }
    for (i_t *term : prev_gen) {
      // try to increment rightmost item < last item
      for (ssize_t i = k - 2; i >= 0; i--) {
        if (term[i] < term[k - 1]) {
          // get a new term at terms_end
          memcpy(terms_end, term, sizeof(i_t) * k);
          terms_end[i]++;
          auto pair = prod_sum(terms_end, k);
          if (pair.first == pair.second) {
            free(terms);
            return pair.first;
          } else if (pair.first > pair.second || find_term(gen, terms_end, k)) {
            // undo - don't need to do anything
          } else {
            gen.push_back(terms_end);
            terms_end += k;     // move up end
          }
          break;
        }
      }
      // increment last item
      term[k - 1]++;
      auto pair = prod_sum(term, k);
      if (pair.first == pair.second) {
        free(terms);
        return pair.first;
      } else if (pair.first > pair.second) {
        // undo
        term[k - 1]--;
      } else {
        gen.push_back(term);
      }
    }
  }
  free(terms);
  assert(0);
}

int main(int argc, char **argv) {
  std::unordered_set<i_t> nums;
  i_t max_k = atoi(argv[1]);
  for (i_t k = 2; k <= max_k; k++) {
    i_t n = find_product_sum(k);
    printf("k = %d: %d\n", k, n);
    nums.insert(n);
  }
  unsigned int total = 0;
  for (auto n : nums) {
    total += n;
  }
  printf("total = %d\n", total);
}

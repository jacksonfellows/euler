#include <cstdio>
#include <climits>
#include <utility>
#include <queue>
#include <cassert>

const unsigned long test_mat[] = {
  131,673,234,103,18,
  201,96,342,965,150,
  630,803,746,422,111,
  537,699,497,121,956,
  805,732,524,37,331
};

const int deltas[4][2] = {
  {1, 0},
  {0, 1},
  {-1, 0},
  {0, -1}
};

void min_path_sum_rec(unsigned long *mat, unsigned long *min_sum, int N) {
  std::queue<std::pair<int,int> > Q;
  Q.push(std::make_pair(0, 0));
  while (!Q.empty()) {
    std::pair<int, int> p = Q.front();
    Q.pop();
    int i = std::get<0>(p);
    int j = std::get<1>(p);
    unsigned long sum = min_sum[i * N + j];
    assert(sum > 0);
    assert(sum != ULONG_MAX);
    for (int d = 0; d < 4; d++) {
      int i_ = i + deltas[d][0];
      int j_ = j + deltas[d][1];
      if (0 <= i_ && i_ < N && 0 <= j_ && j < N) {
        unsigned long new_sum = sum + mat[i_ * N + j_];
        if (new_sum < min_sum[i_ * N + j_]) {
          min_sum[i_ * N + j_] = new_sum;
          Q.push(std::make_pair(i_, j_));
        }
      }
    }
  }
}

unsigned long min_sum(unsigned long *mat, int N) {
  unsigned long *min_sum = new unsigned long[N];
  for (int i = 0; i < N * N; i++) {
    min_sum[i] = ULONG_MAX;
  }
  min_sum[0] = mat[0];
  min_path_sum_rec(mat, min_sum, N);
  return min_sum[N * N - 1];
}

void read_mat(const char *path, int N, unsigned long *mat) {
  FILE *file = std::fopen(path, "r");
  for (int i = 0; i < N * N; i++) {
    std::fscanf(file, "%lu, ", mat + i);
  }
}

int main(int argc, char **argv) {
  unsigned long mat[80 * 80];
  read_mat("../p081_matrix.txt", 80, mat);
  printf("%lu\n", min_sum(mat, 80));
}

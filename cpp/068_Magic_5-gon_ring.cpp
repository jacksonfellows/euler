#include <cstdio>
#include <algorithm>
#include <vector>

void print_arr(std::vector<char> arr) {
  std::printf("%d%d%d%d%d%d%d%d%d%d%d%d%d%d%d\n",
              arr[0], arr[1], arr[2],
              arr[3], arr[2], arr[4],
              arr[5], arr[4], arr[6],
              arr[7], arr[6], arr[8],
              arr[9], arr[8], arr[1]);
}

bool check_arr(std::vector<char> arr) {
  char totals[] = {
    arr[0] + arr[1] + arr[2],
    arr[3] + arr[2] + arr[4],
    arr[5] + arr[4] + arr[6],
    arr[7] + arr[6] + arr[8],
    arr[9] + arr[8] + arr[1]
  };
  for (int i = 1; i < sizeof(totals) / sizeof(char); i++) {
    if (totals[i] != totals[0]) {
      return false;
    }
  }
  return arr[0] < arr[3] && arr[0] < arr[5] && arr[0] < arr[7] && arr[0] < arr[9];
}

int main(int argc, char **argv) {
  std::vector<char> arr = std::vector<char>();
  arr.push_back(9);
  arr.push_back(8);
  arr.push_back(7);
  arr.push_back(6);
  arr.push_back(5);
  arr.push_back(4);
  arr.push_back(3);
  arr.push_back(2);
  arr.push_back(1);
  arr.push_back(10);
  while (!check_arr(arr)) {
    std::prev_permutation(arr.begin(), arr.end());
  }
  print_arr(arr);
}

#include <unordered_map>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int max = -1;
        int majority;
        unordered_map<int, int> map;
        
        for (auto& elem : nums) {
                if (map.find(elem) == map.end()) {
                map[elem] = 1;
            }

            else {
                map[elem]++;
            }
        }
        
        for (auto pair : map) {
            if (pair.second > max) {
                max = pair.second;
                majority = pair.first;
            }
        }
        
        return majority;
    }
};
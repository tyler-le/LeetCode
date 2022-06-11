#include <limits>
#include<algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_day = 0;
        int sell_day = 1;
        int max_profit = INT_MIN;
        int curr_profit;
        
        while(sell_day < prices.size()) {
            
            if (prices[buy_day] > prices[sell_day]) {
                buy_day = sell_day;
                sell_day++;
                curr_profit = prices[buy_day];
            }
            
            else {
                curr_profit = prices[sell_day] - prices[buy_day];
                max_profit = max(curr_profit, max_profit);
                sell_day++;
            }
        }
        
       return max_profit < 0 ? 0 : max_profit;
        
    }
};
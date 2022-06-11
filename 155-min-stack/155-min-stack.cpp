#include <stack>

class MinStack {
public:
    stack<pair<int,int>> st;
    int min;
    
    MinStack() {
        min = INT_MAX;
    }
    
    void push(int val) {
        if (val < min) min = val;
        st.push(make_pair(val, min));
    }
    
    void pop() {
        auto popped = st.top();
        st.pop();
        if (popped.second == min && !st.empty()) min = st.top().second;
        else if (st.empty()) min = INT_MAX;
    }
    
    int top() {
        return st.top().first;
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
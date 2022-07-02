import java.util.Stack;

class MyQueue {

    Stack<Integer> stack1;
    Stack<Integer> stack2;
    
    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        // move to stack2 to get first element
         Iterator itr = stack1.iterator();
        
        while (itr.hasNext()){
            Integer toPush = stack1.pop();
            stack2.push(toPush);
        }
        
        
        int front = stack2.pop();
    
        // now put back to stack1
        itr = stack2.iterator();
        
        while (itr.hasNext()){
            Integer toPush = stack2.pop();
            stack1.push(toPush);
        }
        
        return front;
            
    }
    
    public int peek() {
        // move to stack2 to get first element
        Iterator itr = stack1.iterator();
        
        while (itr.hasNext()){
            Integer toPush = stack1.pop();
            stack2.push(toPush);
        }
        
        
        int front = stack2.peek();
    
        // now put back to stack1
        
        itr = stack2.iterator();
        
        while (itr.hasNext()){
            Integer toPush = stack2.pop();
            stack1.push(toPush);
        }
        
        return front;
    }
    
    public boolean empty() {
        return stack1.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
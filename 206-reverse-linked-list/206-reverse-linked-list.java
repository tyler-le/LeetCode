/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
//     public ListNode reverseList(ListNode head) {
//         ListNode prev = null;
//         ListNode curr = head;
//         ListNode next;
        
//         while(curr != null) {
//             next = curr.next;
//             curr.next = prev;
//             prev = curr;
//             curr = next;
//         }
        
//         head = prev;
        
//         return head;
//     }
    
    public ListNode reverseList(ListNode head) {
        return helper(head, null);
    }
    
    public ListNode helper(ListNode head, ListNode newHead) {
        if (head == null) return newHead;
        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        return helper(next, head);
        
    }
}
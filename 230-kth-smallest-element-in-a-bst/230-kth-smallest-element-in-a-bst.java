/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<Integer> list = new ArrayList<>();
    
    // in order traversal, shove into list
    public void inorder_helper(TreeNode root) {
        if (root == null) return;
        
        inorder_helper(root.left);
        list.add(root.val);
        inorder_helper(root.right);
    }
    
    public int kthSmallest(TreeNode root, int k) {
        inorder_helper(root);
        return list.get(k-1);
    }
}
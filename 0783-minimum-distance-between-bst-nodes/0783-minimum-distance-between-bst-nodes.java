class Solution {
    int min=Integer.MAX_VALUE;
    Integer prev=null;
    public int minDiffInBST(TreeNode root) {
       if(root.left!=null) minDiffInBST(root.left);
       if(prev!=null) min=Math.min(min,root.val-prev);
       prev=root.val;
       if(root.right!=null)minDiffInBST(root.right);
      return min;  
    }
}
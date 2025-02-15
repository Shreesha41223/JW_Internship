
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root.left, root.right);
    }

    boolean isMirror(TreeNode p, TreeNode q) {
        if (p == null || q == null)
            return p == q;

        return (p.val == q.val) && isMirror(p.left, q.right) && isMirror(p.right, q.left);
    }
}
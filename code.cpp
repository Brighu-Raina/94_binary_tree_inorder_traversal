class Solution {
    void recurrence(TreeNode* root,vector<int>& ans)
    {
        if(root ==NULL)
            return;
        recurrence(root->left,ans);
        ans.push_back(root->val);
        recurrence(root->right,ans);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        recurrence(root,ans);
        return ans;
    }
};

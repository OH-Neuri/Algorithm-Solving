/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    let node = {};
    let hasParent = new Set();

    for (let desc of descriptions) {
        if (!node.hasOwnProperty(desc[0])) {
            node[desc[0]] = new TreeNode(desc[0]);
        }
        if (!node.hasOwnProperty(desc[1])) {
            node[desc[1]] = new TreeNode(desc[1]);
        }
        hasParent.add(desc[1]);
    }

    let root = null;
    for (let desc of descriptions) {
        if (desc[2] == 1) {
            node[desc[0]].left = node[desc[1]]; 
        } else {
            node[desc[0]].right = node[desc[1]]; 
        }
        if (!hasParent.has(desc[0])) {
            root = node[desc[0]];
        }
    }

    return root;
};

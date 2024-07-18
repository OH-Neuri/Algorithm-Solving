/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} distance
 * @return {number}
 */
var countPairs = function(root, distance) {
    const graph = new Map();
    const leafNodes = new Set();

    const traverseTree = (currNode, prevNode) => {
        if (!currNode) return;
        if (!currNode.left && !currNode.right) {
            leafNodes.add(currNode);
        }
        if (prevNode) {
            if (!graph.has(prevNode)) graph.set(prevNode, []);
            if (!graph.has(currNode)) graph.set(currNode, []);
            graph.get(prevNode).push(currNode);
            graph.get(currNode).push(prevNode);
        }
        traverseTree(currNode.left, currNode);
        traverseTree(currNode.right, currNode);
    };

    traverseTree(root, null);
    let ans = 0;
    for (const leaf of leafNodes) {
        const bfsQueue = [leaf];
        const seen = new Set([leaf]);
        for (let i = 0; i <= distance; i++) {
            const size = bfsQueue.length;
            for (let j = 0; j < size; j++) {
                const currNode = bfsQueue.shift();
                if (leafNodes.has(currNode) && currNode !== leaf) {
                    ans++;
                }
                if (graph.has(currNode)) {
                    for (const neighbor of graph.get(currNode)) {
                        if (!seen.has(neighbor)) {
                            bfsQueue.push(neighbor);
                            seen.add(neighbor);
                        }
                    }
                }
            }
        }
    }
    return Math.floor(ans / 2);
};
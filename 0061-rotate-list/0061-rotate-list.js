/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if(head === null || head.next == null)
       return head;

    let last = head;
    let totalNodes = 1;

    while (last.next !== null) {
        totalNodes++;
        last = last.next;
    }

    k %= totalNodes;
    if (k === 0) return head;

    let totalNodesMinusK = totalNodes - k;
    let curr = head;

    while (totalNodesMinusK > 1){
        curr = curr.next;
        totalNodesMinusK--;
    }

    const newHead = curr.next;
    curr.next = null;
    last.next = head;

    return newHead;
    
};
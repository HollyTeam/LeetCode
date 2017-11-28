/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let head = {},
    	carry = 0;
    const h = head

    while(l1 || l2){
    	head = head.next = new ListNode(0)
        head.val = ((l1?l1.val:0 || 0)+(l2?l2.val:0 || 0)+carry) % 10
        carry = Number.parseInt(((l1?l1.val:0 || 0)+(l2?l2.val:0 || 0)+carry) / 10)
        l1 = l1?l1.next:null
        l2 = l2?l2.next:null
    }

    if(carry)
        Object.assign(head.next = {},{val:carry,next:null})

    return h.next
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || k ==0){
            return head;
        }
        
        ListNode* temp = head;
        ListNode* prev = NULL;
        int count = 1;

        while(temp->next != NULL){
            count++;
            temp = temp->next;
        }

        temp->next = head;
        temp = head;
        k = k % count;
        count = count - k;

        if(count == 0){
            return head;
        }

        while(count > 0){
            prev = temp;
            temp = temp->next;
            count--;
        }

        prev->next = NULL;
        return temp;
        
    }
};
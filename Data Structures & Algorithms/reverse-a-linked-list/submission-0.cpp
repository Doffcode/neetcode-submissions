/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head||!head->next )return head;
        ListNode* temp=head;
        ListNode* temp2=NULL;
        while(temp->next){
            ListNode* t=temp->next;
            temp->next=temp2;
            temp2=temp;
            temp=t;
        }
        temp->next=temp2;
        return temp;
    }
};

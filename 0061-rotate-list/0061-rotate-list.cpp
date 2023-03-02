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
    int len(ListNode* p){
        int x = 0;
        while(p){
            x++;
            p = p->next;
        }
        return x;
    }
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL||head->next==NULL)return head;
        int l = len(head);
        k = k%l;
        if(k==0)return head;
        k = l-k;
        ListNode* p = head;
        while(--k){
            p = p->next;
        }
        ListNode* q = p->next;
        p->next = NULL;
        ListNode* ans = q;
        while(q->next != NULL){
            q = q->next;
        }
        q->next = head;
        return ans;
    }
};
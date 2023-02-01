// Using Binary Search Approach...
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int beg = 0;
        int end = nums.size()-1;
        while(beg <= end){
            int mid = (beg + end)/2;
            if(target > nums[mid]){
                beg = mid + 1;
            }else if(target < nums[mid]){
                end = mid - 1;
            }else{
                return mid;
            }
        }
        return beg;
    }
};
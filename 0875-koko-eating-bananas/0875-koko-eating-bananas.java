class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;

        for (int x : piles) {
            max = Math.max(max, x);
        }

        int left = 1;
        int right = max;

        while (left < right) {
            int mid = left + (right - left) / 2;

            int cnt = 0;

            for (int x : piles) {
                cnt += (x + mid - 1) / mid;
            }

            if (cnt > h) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
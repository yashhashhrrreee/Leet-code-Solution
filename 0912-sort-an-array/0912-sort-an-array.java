class Solution {
	private int finMax(int[] nums, int index, int size) {
		if (2 * index + 2 < size) {
			return Math.max(nums[index], Math.max(nums[2 * index + 1], nums[2 * index + 2]));
		}
		return Math.max(nums[index], nums[2 * index + 1]);
	}

	private void swap(int[] nums, int i, int j) {
		int tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;
	}

	private void maxHeapify(int[] nums, int index, int size) {
		while (2 * index + 1 < size) {
			int min = finMax(nums, index, size);
			if (min == nums[index]) {
				return;
			} else if (min == nums[2 * index + 1]) {
				swap(nums, index, 2 * index + 1);
				index = 2 * index + 1;
			} else {
				swap(nums, index, 2 * index + 2);
				index = 2 * index + 2;
			}
		}
	}

	public int[] sortArray(int[] nums) {
		int size = nums.length;
		for (int i = size / 2 - 1; i >= 0; i--) {
			maxHeapify(nums, i, size);
		}
		for (int i = size - 1; i > 0; i--) {
			swap(nums, 0, i);
			maxHeapify(nums, 0, i);
		}
		return nums;
	}
}
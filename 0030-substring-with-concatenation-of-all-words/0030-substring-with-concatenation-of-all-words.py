class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        num_words = len(words)
        word_length = len(words[0])
        substring_length = num_words * word_length
        target_cnt = Counter(words)

        def sliding_window(left):
            nonlocal n, word_length, substring_length, target_cnt, res
            curr_cnt = defaultdict(int)
            word_used = 0
            excess = False
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break
                _sub = s[right : right + word_length]
                if _sub not in target_cnt:
                    curr_cnt = defaultdict(int)
                    word_used = 0
                    excess = False
                    left = right + word_length
                else:
                    while right - left == substring_length or excess:
                        left_sub = s[left:left+word_length]
                        curr_cnt[left_sub] -= 1
                        left += word_length
                        if curr_cnt[left_sub] == target_cnt[left_sub]:
                            excess = False
                        else:
                            word_used -= 1

                    curr_cnt[_sub] += 1
                    if curr_cnt[_sub] <= target_cnt[_sub]:
                        word_used += 1
                    else:
                        excess = True
                    if word_used == num_words and not excess:
                        res.append(left)

        res = []
        for i in range(word_length):
            sliding_window(i)
        return res
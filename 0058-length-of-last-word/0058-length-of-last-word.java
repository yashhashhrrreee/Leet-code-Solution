class Solution {
    public int lengthOfLastWord(String s) {
           String trim = s.trim();
        char[] chars = trim.toCharArray();
        int count = 0;
        for (int i = chars.length - 1; i >= 0; i--) {
            count++;
            if(chars[i]==' '){
                return count-1;
            }
        }
        return count;
    }
}
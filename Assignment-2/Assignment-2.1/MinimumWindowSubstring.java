class MinimumWindowSubstring {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) {
            return new String();
        }

        int[] letterCount = new int[127];
        int left = 0;
        int right = 0;
        int startIndex = 0;
        int count = t.length();
        int minLength = Integer.MAX_VALUE;

        for (char c : t.toCharArray()) {
            letterCount[c]++;
        }

        char[] sCharArr = s.toCharArray();

        while (right < s.length()) {
            if (letterCount[sCharArr[right++]]-- > 0) {
                count--;
            }

            while (count == 0) {
                if (right - left < minLength) {
                    startIndex = left;
                    minLength = right - left;
                }

                if (letterCount[sCharArr[left++]]++ == 0) {
                    count++;
                }
            }
        }

        return minLength == Integer.MAX_VALUE ? new String() : new String(sCharArr, startIndex, minLength);
    }
}
class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] letter = new int[26];

        for (char c : s.toCharArray()) {
            letter[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            if (letter[c - 'a'] == 0) {
                return false;
            }
            letter[c - 'a']--;
        }
        return true;
    }
}
import java.util.*;

public class KthPermutation {
    public String getPermutation(int n, int k) {
        // Precompute factorial values up to (n-1)!
        int[] factorial = new int[n];
        factorial[0] = 1;
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }

        // List to hold the numbers 1 to n
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        // Convert k to 0-based index
        k--;

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int currentFact = factorial[n - 1 - i]; // (remaining elements - 1)!
            int index = k / currentFact;
            result.append(numbers.get(index));
            numbers.remove(index);
            k %= currentFact;
        }

        return result.toString();
    }
}
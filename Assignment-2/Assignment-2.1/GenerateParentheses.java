import java.util.*;

class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<String>();
        backTracking(new StringBuilder(), 0, n, result);
        return result;
    }

    void backTracking(StringBuilder sb, int count, int n, List<String> result) {
        if (count == 0 && n == 0) {
            result.add(sb.toString());
            return;
        }

        if (n > 0) {
            sb.append("(");
            backTracking(sb, count + 1, n - 1, result);
            sb.setLength(sb.length() - 1);
        }

        if (count > 0) {
            sb.append(")");
            backTracking(sb, count - 1, n, result);
            sb.setLength(sb.length() - 1);
        }
    }
}
package leetcode;

import java.util.*;

class L0020ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (c == '[') {
                stack.push(']');
            } else if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else {
                if (stack.empty()) {
                    return false;
                }
                if (c != stack.pop()) {
                    return false;
                }
            }
        }
        return stack.empty();
    }
}
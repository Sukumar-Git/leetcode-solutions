class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop top element if stack is non-empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening bracket onto the stack
                stack.append(char)

        # If stack is empty, all brackets were validly matched
        return not stack
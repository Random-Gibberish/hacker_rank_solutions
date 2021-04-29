
from collections import deque


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def push_character(self, item):     # push onto new list
        self.stack.append(item)         # letters are backwards

    def enqueue_character(self, item):  # enqueue on new list
        self.queue.append(item)

    def pop_character(self):            # pops last char
        return self.stack.pop()

    def dequeue_character(self):        # dequeues first char
        return self.queue.popleft()


# Not my code
if __name__ == '__main__':
    s = input()

    # Create the Solution class object
    obj = Solution()
    len_s = len(s)

    # push/enqueue all the characters of string s to stack
    for i in range(len_s):
        obj.push_character(s[i])
        obj.enqueue_character(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(len_s // 2):
        if obj.pop_character() != obj.dequeue_character():
            isPalindrome = False
            break

    # finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")

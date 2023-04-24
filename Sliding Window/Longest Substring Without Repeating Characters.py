def lengthOfLongestSubstring(s: str) -> int:
    substring = []
    longest = 0
    current = 0
    for c in s:
        if c not in substring:
            substring.append(c)
            current = current + 1
            longest = max(current, longest)
        else:
            substring = substring[substring.index(c) + 1:]
            substring.append(c)
            current = len(substring)
            longest = max(current, longest)
    return longest
print(lengthOfLongestSubstring("aab"))
s="abcde"
words=["a", "bb", "acd", "ace"]

def subset():
    count = 0
    for word in words:
        if len(word) < 2 and word in s:
                count += 1
        for i in range(len(s)):
            for j in range(len(word)):
                if word[j] != s[i]:# bb
                     break
                else:
                    continue
            count += 1
    print(count)
subset()
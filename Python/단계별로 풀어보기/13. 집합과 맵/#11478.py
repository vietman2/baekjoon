S = input()

def get_substring(s):
    return set(s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1))

print(len(get_substring(S)))
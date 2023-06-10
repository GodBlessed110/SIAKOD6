import random
import time


def compute_prefix_function(pattern):
    """
    Вычисляет префикс-функцию для заданной строки
    """
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi


"Алгоритм Кнута–Морриса–Пратта"
"AABAABAA"


def kmp_search(text, pattern):
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    res = []
    for i, c in enumerate(text):
        while q > 0 and pattern[q] != c:
            q = pi[q-1]
        if pattern[q] == c:
            q += 1
        if q == m:
            res.append(i-m+1)
            q = pi[q-1]
    return res


def primitive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    res = []
    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            res.append(i)
    return res


"""text = "dasABABCABDe"
pattern = "ABABCABD"

indices = kmp_search(text, pattern)

if len(indices) > 0:
    print("Pattern found at positions:")
    for index in indices:
        print(index)
else:
    print("Pattern not found.")"""


# Генерируем случайную строку и подстроку
text = "".join([random.choice("ABCD") for _ in range(100000)])
pattern = "".join([random.choice("ABCD") for _ in range(5)])

# Тестируем алгоритм КМП
start_time = time.time()
kmp_indices = kmp_search(text, pattern)
kmp_time = time.time() - start_time

# Тестируем примитивный алгоритм
start_time = time.time()
primitive_indices = primitive_search(text, pattern)
primitive_time = time.time() - start_time

print("Алгоритм КМП нашел", len(kmp_indices), "случаев за", kmp_time, "секунд")
print("Примитивный алгоритм нашел", len(primitive_indices), "случаев за", primitive_time, "секунд")
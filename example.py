from fuzzy_compare import compare_english_words


print(compare_english_words("hello", "hello"))  # Out: 1.0
print(compare_english_words("hello", "helllo"))  # Out: 0.9090...
print(compare_english_words("hello", "hell"))  # Out: 0.88...
print(compare_english_words("hello", "hallo"))  # Out: 0.8
print(compare_english_words("hello", "world"))  # Out: 0.4
print(compare_english_words("hello", ""))  # Out: 0.0

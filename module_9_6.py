def all_variants(text):
  length = len(text)
  for l in range(1, length + 1):
    for start in range(length - l + 1):
      end = start + l
      yield text[start:end]

a = all_variants("abc")
for i in a:
  print(i)
 # 2. Написатьпрограмму,котораяпроверяет,начинаетсялистрокас данного символа, используя lambda функцию.
word = "ello"

b = list(filter(lambda word: "h" == word[0], word))
print(b)

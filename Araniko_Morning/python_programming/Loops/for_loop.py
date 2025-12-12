# for i in range(5):
#     print(i)

# name = "Anish Dahal"
# for character in name:
#     print(character)

# to calculate the multiple of 7
# for i in range(7, 100, 7):
#     print(i)

# write a program to calculate the number of vowels letters in the text "python programming is fun if you learn properly"
text = "python programming is fun if you learn it properly"
vowels = "aeiou"
vowels_count = 0

for character in text:
    if character in vowels:
        vowels_count += 1
print(vowels_count)

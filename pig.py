# get sentence from user

original = input("Escreva uma frase qualquer: ").strip().lower()

#split sentence into words with string method .slip()

words = original.split()

# loop through words and convert to pig latin

new_words = []
for word in words:
    
#if starts with vowel, just add yay
    if word[0] in "aeiou":
        newword = word + "yay"
        new_words.append(newword)
#Otherwise, move the first consonant cluser to end and add ay
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        newword = rest + cons + "ay"
        new_words.append(newword)
        
print(new_words)

#stick words back together with stg method join and " ",
# which adds space to the list's strings

output = " ".join(new_words)

#output the final string

print(output)

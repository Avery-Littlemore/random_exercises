# You are given a sentence represented by a string str. Your objective is to reverse all the characters in 
# each word of the sentence while ensuring that the case of each character remains unchanged. The spaces 
# between words should be preserved as they are, and the overall order of the words in the sentence must not be altered.

# You should solve the problem without using the Array#reverse method.

def reverse_words(sentence):
    words = sentence.split(' ')

    for i in range(len(words)):
        
        word = list(words[i])
        start = 0
        end = len(word) - 1
        while start < end:
            [word[start], word[end]] = [word[end], word[start]]
            start += 1
            end -= 1

        words[i] = ''.join(word)

    return ' '.join(words)

print(reverse_words("Hello World") == "olleH dlroW")
print(reverse_words("JavaScript is fun") == "tpircSavaJ si nuf")
print(reverse_words("Coding in the sun") == "gnidoC ni eht nus")
print(reverse_words("Launch School") == "hcnuaL loohcS")
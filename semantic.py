import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")


#code comparing each word to another
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat and monkey are the most similar, followed by monkey and banana because monkeys eat bananas and then cat and banana



tokens = nlp('cat apple monkey banana ')

# for loop to compare each of the words in the list to each other and print the quantative similarity
for token1 in tokens:

    for token2 in tokens:

        print(token1.text, token2.text, token1.similarity(token2))

# it shows 100% similarity when compared to itself
# apple and banana are similar because both are fruits
# cat and monkey are similar because both are animals
# mokey and banana show some similarity as it recognises that monkeys eat bananas
#cats have little similarity with either of the other fruits

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

#comparing each sentence in list with sentence abovce using for loop
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# the highest similarity is when the sentence is there is my car as it is referring the the car as an object
# similarly with the lost my car in my car, it is referring to it as an object and so there is similarity
# the sentences with 'dog' show some similiarity as it recognises that dog is also an animal like cat
# the boat sentence is the least similar because it does not talk about an animal but it still recognises that boat is a vehicle like car

sentence_to_compare = "I bought a new kitten and his name is Ed"

sentences = ["where did my cat go",
"What is Fred doing tomorrow?",
"I made a new friend called Ed",
"My kitten likes to play with a ball",
"Ed is playing with some yarn."]

model_sentence = nlp(sentence_to_compare)

#comparing each sentence in list with sentence abovce using for loop
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Most similar is about a new friend called Ed as it refers to a new person or animal called Ed
# Least similar is where the cat went. it recognises some similarty between a cat and kitten
# the sentence about Fred has slightly higher similarity, most likely because of the spelling of ed and fred
# the kitten playing with the ball has higher similarity because it mentions the kitten
# Ed playing with yarn has higher similarity because of the name and possibly because of the link between kittens and yarn.
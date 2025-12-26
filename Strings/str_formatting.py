sentence = "My name is {}. I like to play {}."
name1 = "Alpha"
name2 = "Srilu"

game1 = "Football"
game2 = "Volleyball"
 
sentence_updated1 = sentence.format(name1, game1)
sentence_updated2 = sentence.format(name2, game2)

print(sentence_updated1)

num = int(input("Enter our name\n"))
print(num)

print(f"My name is {name2}. I like to play {game2}") # f string
import random

secretWord = ["accept", "damage","coffee", "danger", "record", "liquid", "market", "detail", "circle", "defeat","bishop","bordertliquid","rescue","retail","screen","salary","writer","yellow","update"]
word = random.choice(secretWord)

mysteryList = list(word)

rightLetters = []
wrongLetters = []
guessWord = []

misses = 0

print("Welcome to Hangman!")
incorrectLetters = input("How many times do you want to miss before you lose? ")

for letter in mysteryList:
		rightLetters.append("_")
print(rightLetters)

while True:
	guess = input("Guess a letter: ")
	if guess in word:
		index = mysteryList.index(str(guess))
		rightLetters.pop(int(index))
		rightLetters.insert(int(index), guess)
		print(rightLetters)
		print("Misses: " + str(guessWord))
		print("You can miss " + str(int(incorrectLetters) - int(misses))+ " more times")
	if guess not in word:
		misses = misses + 1
		guessWord.append(guess)
		print(rightLetters)
		print("Misses: " + str(guessWord))
		print("You can miss " + str(int(incorrectLetters) - int(misses))+ " more times")
	if misses == int(incorrectLetters):
		print("Game over! You lossed")
		print("The word was " + word)
		break
	if rightLetters[0] == mysteryList[0] and rightLetters[1] == mysteryList[1] and rightLetters[2] == mysteryList[2] and rightLetters[3] == mysteryList[3] and rightLetters[4] == mysteryList[4] and rightLetters[5] == mysteryList[5]:
		print("You won! ")
		break


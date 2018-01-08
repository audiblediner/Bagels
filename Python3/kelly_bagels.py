import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    print(secretNum)
    return secretNum

def getClues(guess, secretNum):
    fermi = pico = 0
    output = []
    for index in range(len(guess)):
        digit = guess[index]
        if digit==secretNum[index]:
            fermi += 1
        elif digit in secretNum:
            pico += 1
    for f in range(fermi):
        output.append("Fermi")
    for p in range(pico):
        output.append("Pico")
    if output==[]:
        output.append("Bagels")
    return(" ".join(output))
    
def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in ' 0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('--------------------------------------------------------------')
print('\t\tWELCOME TO THE GAME OF BAGELS!')
print('--------------------------------------------------------------')
print('You will try to guess a %s-digit number.'%(NUM_DIGITS))
print('I will give you clues based on your response.')
print('--------------------------------------------------------------')
print('When I say...\tit means that...')
print('--------------------------------------------------------------')
print('Bagels\t\tNone are right.')
print('Pico\t\tOne digit is correct but in the wrong position.')
print('Fermi\t\tOne digit is correct and in the right position.')
print('--------------------------------------------------------------')

def main():
    play = "yes"
    while play == "yes":
        print("I am thinking of a 3-digit number. Try to guess what it is")
        print('I will give you clues based on your response.')
        print('--------------------------------------------------------------')
        print('When I say...\tit means that...')
        print('--------------------------------------------------------------')
        print('Bagels\t\tNone are right.')
        print('Pico\t\tOne digit is correct but in the wrong position.')
        print('Fermi\t\tOne digit is correct and in the right position.')
        print('--------------------------------------------------------------')        

        secretNum = getSecretNum()
        
        print("I have thought up a number. You have 10 guesses to get it")

        for i in range(1,11):
            guess = input("Guess #" + str(i) + ":\n")
            if isOnlyDigits(guess):
                clue = getClues(guess,secretNum)
                print(clue)
                
                # if user guesses correct number, the for loop breaks
                if clue == "Fermi Fermi Fermi":
                    print("You win! Congrats!")
                play = input('Would you like to play again? (yes or no)')
                if play == 'no':
                    break

                

main()

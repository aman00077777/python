def func(userInput):
    vowels =  "aeiouAEIOU"
    countVowels = 0
    countConsonants = 0
    for char in userInput:
        if char.isalpha():
            if char in vowels:
                countVowels += 1
            else:
                countConsonants += 1
    print("Number of vowels:", countVowels)
    print("Number of consonants:", countConsonants)
userInput = input("Enter a string: ")
func(userInput) 
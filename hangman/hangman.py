import random
import string
from resource_words import words_resource

def corr_word(words_resource):
    word=random.choice(words_resource)
    while '-' in word or ' ' in word:
        word=random.choice(words_resource)

        return word
    
def hm():
    word=corr_word(words_resource)
    word_letters = set(word)
    alpha=set(string.ascii_uppercase)
    use_letter = set() 
    lives = 4

    while len(word_letters)>0 and lives>0:
        print('you have',lives,'lives lest and you have used these letters:', ' '.join(use_letter))
        word_list=[letter if letter in use_letter else '_' for letter in word]
        print('Current Word: ', ' '.join(word_list))
        user_letter=input('guess a letter').upper()
        if user_letter in alpha-use_letter:
            use_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)       
            
            else:
                lives=lives-1
                print('letter is not in word')
        elif user_letter in use_letter:
            print('you have already used that character')

        else:
            print('invalid character')
    

    if lives==0:
        print('you died, the word was',word)
    else:
        print('you guessed the word',word)
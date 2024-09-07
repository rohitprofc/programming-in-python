def remove_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    withnovowels = [ele for ele in string if ele.lower() not in vowels]
    result = ''.join(withnovowels)
    print(result)


string = input('Enter a string: ')
remove_vowel(string)

'''
Output:-
Enter a string: I am a vowel
 m  vwl
'''

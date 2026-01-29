# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 2 "Nested Dictionary from Strings"
# need to create a function which takes in a list of strings and outputs a dictionary with,
# each key being a string from the list and returning a dictionary value for each with the key being length and the value being the length and parity as a key and even or odd as the value
# Need to define the function  and make a dictonary inside it
def word_information_provider(list_of_words):
    final_word_info_dictionary = {}
    # need to now make a for loop which goes through each word in the list
    for words in list_of_words:
        #need to make a variable which stores the length of the word, this will make both sections a lot easier to approach
        length_of_words = len(words)
        # now need to get whether it is even or odd using the length of the word
        if length_of_words % 2 == 0:
            # need a function which tells me whether it is even or odd
            parity = "even"
        else:
            parity = "odd"
        # now have all the info I need just need to wrap it up into a final dictionary which I will return
        final_word_info_dictionary[words] = {

            "length": length_of_words,
            "parity": parity

        }
    return final_word_info_dictionary
# test run to make sure it works
words = ["freak", "apple", "ban", "fire"]
print(word_information_provider(words))
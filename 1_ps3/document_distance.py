# 6.100A Spring 2023
# Problem Set 3
# Name: <Kenneth Oranga>
# Collaborators: <Office Hours>

"""
Description:
    Computes the similarity between two texts using two different metrics:
    (1) shared words, and (2) term frequency-inverse document
    frequency (TF-IDF).
"""

import string
import math
import re

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    for i in input_text:
     if not str.isalpha(i):
        input_text = input_text.replace(i,' ')
    str_list = list(input_text.split()) #splits words at space and then lists each word
    return str_list


### Problem 1: Get Frequency ###
def get_frequencies(word_list):
    """
    Args:
        word_list: list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a word in l and the corresponding int
        is the frequency of the word in l
    """
    freq_dict = {}
    check_lst = []
    for wrd in word_list:
        if wrd in check_lst:
            freq_dict[wrd]+= 1 #increases the value of word if duplicate
        else:
            freq_dict[wrd] = 1
            check_lst.append(wrd)#adds word to checker lst
        
    return freq_dict 


### Problem 2: Get Words Sorted by Frequency
def get_words_sorted_by_frequency(frequencies_dict):
    """
    Args:
        frequencies_dict: dictionary that maps a word to its frequency
    Returns:
        list of words sorted by increasing frequency with ties broken
        by alphabetical order
    """
    srt_wrd_lst = []
    n = 1
    lmt = max(frequencies_dict.values())
    while n<lmt+1:
        checker = [] #creates new list everytime we go through the loop
        for i in frequencies_dict:
            if frequencies_dict[i]== n :
                checker.append(i) #adds all elements with the same freq in one list for alphabetical sorting
        d = sorted(checker)
        for x in d:
            srt_wrd_lst.append(x) #adds all sorted elements into one final list
        n += 1
    return srt_wrd_lst



### Problem 3: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          frequencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    if len(dict1)>=len(dict2):
        a,b = dict1,dict2
    else:
        a,b = dict2, dict1
    for wrd in b:
        #iterates over the samllest dict and adds similar word freqs and non-similar words to larger dict : a
        if wrd in a:
            keya = a[wrd]
            keyb = b[wrd]
            a[wrd]= keya+keyb
        else:
            a[wrd]=b[wrd]
    most_frq = max(a.values()) #gets the maximum freq
    frq_wrd_lst = [x for x in a if a[x]==most_frq]#iterates over larger dict to get the keys that have the max req and adds them to a list
    return frq_wrd_lst





### Problem 4: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of words of text1
        dict2: frequency dictionary of words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    freq_diff_dict = {}#new dict that shows freq differences
    freq_total_dict = {}#values are freq totals 
    if len(dict1)>len(dict2):
        a,b = dict1,dict2
    else:
        a,b = dict2, dict1
    for wrd in b:#iterates over smaller dict to add to new dicts
        if wrd in a:
            freq_diff_dict[wrd] = abs(a[wrd]-b[wrd])
            freq_total_dict[wrd] = abs(a[wrd]+b[wrd])
        else:
            freq_diff_dict[wrd]=b[wrd]
            freq_total_dict[wrd]=b[wrd]
    for wrd in a:#iterates over larger dict to add to new dicts
        if wrd not in freq_diff_dict:
            freq_diff_dict[wrd]=a[wrd]
            freq_total_dict[wrd]=a[wrd]
    x = sum(freq_diff_dict.values())#sums diff values
    y = sum(freq_total_dict.values())#sums total values
    similarity = 1-x/y
    ans = round(similarity,2)#rounds the similarity to 2 dp
    return ans

### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    input_txt = load_file(text_file)#loads file which has name text_file
    wrd_lst = prep_data(input_txt)#creates list of words in text
    freq_list = get_frequencies(wrd_lst)# gets freqs of wrds in list
    for i in freq_list:
        freq_list[i] = freq_list[i]/len(wrd_lst)
        #gets TF on each word key and changes word dict to have TF as the values of respective keys
    return freq_list


def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    docs_n = len(text_files)#no of documents
    super_list ={}

    for file_name in text_files:
        input_txt = load_file(file_name)#loads file with name: file_name
        wrd_list = set(prep_data(input_txt))#list of words in filename without duplictes
        for wrd in wrd_list:
            if wrd in super_list:
                super_list[wrd]+=1 #maps word to number of documents it appears in
            else:
                super_list[wrd]= 1
        
    for w_key in super_list:
        super_list[w_key]= math.log10(docs_n/super_list[w_key])
        #calculates IDF and maps it to respective wrd

    return super_list



def get_tfidf(text_file, text_files):
    """
    Args:
        text_file: name of file in the form of a string (used to calculate TF)
        text_files: list of names of files, where each file name is a string
        (used to calculate IDF)
    Returns:
       a sorted list of tuples (in increasing TF-IDF score), where each tuple is
       of the form (word, TF-IDF). In case of words with the same TF-IDF, the
       words should be sorted in increasing alphabetical order.

    * TF-IDF(i) = TF(i) * IDF(i)
    """
    tfidf_dict ={}
    ans_lst = []
    tf = get_tf(text_file)#gets tf
    idf = get_idf(text_files)#gets idf
    for wrd in tf:
            tfidf = tf[wrd]*idf[wrd]#gets tfidf 
            tfidf_dict[wrd]=tfidf

    sorted_vals= sorted(tfidf_dict.values())
    for val in sorted_vals:
        # sorts dict by sorting keys alphabetically with ascending vals 
        for key in sorted(tfidf_dict.keys()):
            if tfidf_dict[key] == val and (key,val) not in ans_lst:
                ans_lst.append((key,tfidf_dict[key]))#adds sorted tuple to empty list to be returned.
    return (ans_lst)


if __name__ == "__main__":
    pass
    # ##Uncomment the following lines to test your implementation
    # ## Tests Problem 1: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = prep_data(hello_world), prep_data(hello_friend)
    # print(world) ## should print ['hello', 'world', 'hello', 'there']
    print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 2: Get Frequencies
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq) ## should print {'hello': 2, 'world': 1, 'there': 1}
    print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}

    ## Tests Problem 3: Get Words Sorted by Frequency
    world_words_sorted_by_freq = get_words_sorted_by_frequency(world_word_freq)
    friend_words_sorted_by_freq = get_words_sorted_by_frequency(friend_word_freq)
    print(world_words_sorted_by_freq) ## should print ['there', 'world', 'hello']
    print(friend_words_sorted_by_freq) ## should print ['friends', 'hello']

    # ## Tests Problem 4: Most Frequent Word(s)
    freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    most_frequent = get_most_frequent_words(freq1, freq2)
    print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Similarity
    word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity) ## should print 0.33

    # ## Tests Problem 6: Find TF-IDF
    text_file = 'tests/student_tests/hello_world.txt'
    text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tf_idf = get_tfidf(text_file, text_files)
    print(tf) ## should print {'hello': 0.5, 'world': 0.25, 'there': 0.25}
    print(idf) ## should print {'there': 0.3010299956639812, 'world': 0.3010299956639812, 'hello': 0.0, 'friends': 0.3010299956639812}
    print(tf_idf) ## should print [('hello', 0.0), ('there', 0.0752574989159953), ('world', 0.0752574989159953)]


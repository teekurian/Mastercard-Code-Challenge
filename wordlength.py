
class Sentence:
    """
    Class to check Word length and find longest word in a given string.
    """
    sentence=''
    def __init__(self,sentence):
        self.sentence=sentence

    def find_longest_word(self):
        if self.sentence is None:
            raise TypeError
        if (not isinstance(self.sentence, str)) :
            raise TypeError
        if self.sentence.strip() =='':
            return 0,''
        words_list=self.sentence.lower().split()
       #Below lines are added to create a unique list of words.
        tmp_set=set(words_list)
        unique_words_list=list(tmp_set)

       #Performing alphabetical sort prior to length sort to ensure order of words in the results.
        unique_words_list_sorted= sorted(unique_words_list, key=str.lower)

        #Performing reverse sort based on length
        words_list_sorted_desc=sorted(unique_words_list_sorted,key=len,reverse=True)

        #First element in the reverse sorted list is the word with maximum length
        max_word_len = len(words_list_sorted_desc[0])
        words_list = words_list_sorted_desc[0]

        #Checking if more than one word has length equal to max length.If yes that word is also added to the result string
        for i in words_list_sorted_desc[1:]:
            if len(i) == max_word_len:
                words_list = words_list + ',' + i
            else:
                break
        return max_word_len,words_list


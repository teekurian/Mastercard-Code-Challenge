import unittest
import wordlength as wl

class TestWordlength(unittest.TestCase):

    def setUp(self):
        pass


#Test case 1: Word_list comparison and Word size comparison with double quoted string. Generic Positive case
    def test_find_longest_word1(self):
        my_sentence = "The cow jumped over the moon"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list,'jumped')
        self.assertEqual(word_size, 6)
        print("Finished Testcase 1")

# Test case 2:String containing multiple words with equal length
# Assumption:Testcase expects in a String containing words with equal length,all such words will be displayed.
    def test_find_longest_word2(self):
        my_sentence = "world hello dear world"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'hello,world')
        self.assertEqual(word_size, 5)
        print("Finished Testcase 2")

# Test case 3:String containing same word in different case
# Assumption: Testcase expects in a String containing same words with different case, only lower case word to be displayed.
    def test_find_longest_word3(self):
        my_sentence = "world hello dear World"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'hello,world')
        self.assertEqual(word_size, 5)
        print("Finished Testcase 3")

# Test case 4:Passing empty string
# Assumption: Testcase expects the method to return word_size=0 and word_list=''
    def test_find_longest_word4(self):
        my_sentence = ""
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, '')
        self.assertEqual(word_size, 0)
        print("Finished Testcase 4")

# Test case 5: No string passed
# Assumption: Testcase expects a typeerror when an empty string is passed.
    def test_find_longest_word5(self):
        with self.assertRaises(TypeError):
            sentence_instance = wl.Sentence()
            word_size, word_list = sentence_instance.find_longest_word()
        print("Finished Testcase 5")

# Test case 6: Passing NULL(None) as input
# Assumption: Testcase expects a typeerror when an NULL string is passed.
    def test_find_longest_word6(self):
        my_sentence = None
        with self.assertRaises(TypeError):
            sentence_instance = wl.Sentence(my_sentence)
            word_size, word_list = sentence_instance.find_longest_word()
        print("Finished Testcase 6")

# Test case 7: String containing special characters
# Assumption: Testcase expects no error from special characters in input string and will behave as
# calculate the consider word with special charecters as longest word in this case.
    def test_find_longest_word7(self):
        my_sentence = "world hello dear@^ World"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'dear@^')
        self.assertEqual(word_size, 6)
        print("Finished Testcase 7")

# Test case 8: Passing numbers as input
# Assumption: Testcase expects a typeerror.
    def test_find_longest_word8(self):
        my_sentence = 123
        with self.assertRaises(TypeError):
            sentence_instance = wl.Sentence(my_sentence)
            word_size, word_list = sentence_instance.find_longest_word()
        print("Finished Testcase 8")

# Test case 9: Passing List as input
# Assumption: Testcase expects a typeerror.
    def test_find_longest_word9(self):
        my_sentence = ['a','b']
        with self.assertRaises(TypeError):
            sentence_instance = wl.Sentence(my_sentence)
            word_size, word_list = sentence_instance.find_longest_word()
        print("Finished Testcase 9")

# Test case 10: Passing  dictionary as input
# Assumption: Testcase expects a typeerror.
    def test_find_longest_word10(self):
        my_sentence = {'practical': 1, 'volume': 1, 'physics': 1}
        with self.assertRaises(TypeError):
            sentence_instance = wl.Sentence(my_sentence)
            word_size, word_list = sentence_instance.find_longest_word()
        print("Finished Testcase 10")

#  Test case 11: Passing string with multiple lines
# Assumption: Testcase expects no error from new line character and  will pick up longest word from second line.
    def test_find_longest_word11(self):
        my_sentence = 'first line \n second line'
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'second')
        self.assertEqual(word_size, 6)
        print("Finished Testcase 11")

# Test case 12: Word_list comparison and Word size comparison for single quoted string.Generic Positive case
# Assumption:Testcase expects string with double and single quoted strings to produce same output.
    def test_find_longest_word12(self):
        my_sentence = 'The cow jumped over the moon'
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'jumped')
        self.assertEqual(word_size, 6)
        print("Finished Testcase 12")

# Test case 13:String containing repeating words with same case
# Assumption:Testcase expects in a String containing repeating words ,only 1 occurrence of the words to be displayed.
    def test_find_longest_word13(self):
        my_sentence = "world hello dear world"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'hello,world')
        self.assertEqual(word_size, 5)
        print("Finished Testcase 13")

# Test case 14:String containing URL
# Assumption: Testcase expects entire URL to be considered as word.
    def test_find_longest_word14(self):
        my_sentence = "https://wiki.python.org"
        sentence_instance = wl.Sentence(my_sentence)
        word_size, word_list = sentence_instance.find_longest_word()
        self.assertEqual(word_list, 'https://wiki.python.org')
        self.assertEqual(word_size, 23)
        print("Finished Testcase 14")

        def tearDown(self):
            pass


if __name__ == '__main__':
    unittest.main()
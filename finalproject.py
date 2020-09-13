# 
# FinalProject.py - Final Project
#
# A Statistical Tool to compare models of text
#
# CS111
#
# Name: Ben Badnani
#
# Email: Ben Badnani
#
# Partner Name: Brad Shulman
#
# Partner Email: brad217@bu.edu
#
import math

def clean_text(txt):
        """ takes a string of text txt
            as a parameter and returns
            a list containing the words
            in txt after punctuation is
            removed
        """
        s = ''
        txt = txt.lower().strip('\n')
        for x in txt:
            if x.isalpha() == True or x.isdigit() == True or x == ' ':
                s += x
        return s.split()

def stem(s):
    """ takes a string s
        and returns the
        stem of the string
    """
    if len(s) > 4:
        if s[-4:] == 'ship':
            s = s[:-4]
        if s[-4:] == 'ment' or s[-4:] == 'ness':
            s = s[:-4]
    if len(s) > 3:
        if s[-2:] == 'es':
            s = s[:-2]
        if s[-1:] == 'e' or s[-1:] == 's':
            s = s[:-1]
        if s[-3:] == 'ity' or s[-3:] == 'ier':
            s = s[:-3] + 'i'
        if s[-3:] == 'ing' or s[-3:] == 'est':
            s = s[:-3]
        if s[-2:] == 'er' or s[-2:] == 'th' or \
           s[-2:] == 'ly' or s[-2:] == 'ed':
            s = s[:-2]
        if s[-1:] == 'y':
            s = s[:-1] + 'i'
    return s

def compare_dictionaries(d1, d2):
    """ takes two feature
        dictionaries d1 and
        d2 and returns their
        log similarity score
    """
    score = 0
    total = 0
    for x in d1:
        total += d1[x]

    for x in d2:
        if x in d1:
            score += math.log(d1[x] / total) * d2[x]
        else:
            score += math.log(0.5 / total)
    return score

class TextModel:
    """ a class that analyzes the
        features of text for
        comparability to other texts
    """
    def __init__(self, model_name):
        """ constructs a new TextModel
            object by accepting a string
            as a parameter to analyze the
            attributes name, words, and
            word_lengths
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}

    def __repr__(self):
        """ returns a string that includes
            the name of the model and the
            sizes of the dictionaries for
            each feature of the text
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) \
             + '\n'
        s += '  number of punctuation marks: ' + \
             str(len(self.punctuation)) + '\n'
        return s
 
    def add_string(self, s):
        """ adds a string of text s to the
            model by augmenting the feature
            dictionaries defined in the
            constructor
        """
        b = s.split()
        count = 0
        for w in b:
            if w[-1] == '.' or w[-1] == '?' or w[-1] == '!':
                count += 1
                if count in self.sentence_lengths:
                    self.sentence_lengths[count] += 1
                else:
                    self.sentence_lengths[count] = 1
                count = 0
            else:
                count += 1

        for l in s:
            if l == ',' or l == '!' or l == '?' or l == '-' or l == '&' or \
               l == '/' or l == "'" or l == '(' or l == '*' or l == ':' or \
               l == ';' or l == '.':
                if l in self.punctuation:
                    self.punctuation[l] += 1
                else:
                    self.punctuation[l] = 1
                    
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            if stem(w) in self.stems:
                self.stems[stem(w)] += 1
            else:
                self.stems[stem(w)] = 1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
    def save_model(self):
        """ saves the TextModel object self
            by writing its various feature
            dictionaries to files.
        """
        filename = self.name + '_words.txt'
        a = open(filename, 'w')
        a.write(str(self.words))
        a.close()

        filename1 = self.name + '_word_lengths.txt'
        b = open(filename1, 'w')
        b.write(str(self.word_lengths))
        b.close()

        filename2 = self.name + '_stems.txt'
        c = open(filename2, 'w')
        c.write(str(self.stems))
        c.close()

        filename3 = self.name + '_sentence_lengths.txt'
        d = open(filename3, 'w')
        d.write(str(self.sentence_lengths))
        d.close()

        filename4 = self.name + '_punctuation.txt'
        e = open(filename4, 'w')
        e.write(str(self.punctuation))
        e.close()
                
    def read_model(self):
        """ reads the stored dictionaries for the called
            TextModel object from their files and assigns
            them to the attributes of the called TextModel.
        """
        filename = self.name + '_words.txt'
        a = open(filename, 'r')
        d_str = a.read()
        a.close()
        self.words = dict(eval(d_str))

        filename1 = self.name + '_word_lengths.txt'
        b = open(filename1, 'r')
        d_str = b.read()
        b.close()
        self.word_lengths = dict(eval(d_str))

        filename2 = self.name + '_stems.txt'
        c = open(filename2, 'r')
        d_str = c.read()
        c.close()
        self.stems = dict(eval(d_str))

        filename3 = self.name + '_sentence_lengths.txt'
        d = open(filename3, 'r')
        d_str = d.read()
        d.close()
        self.sentence_lengths = dict(eval(d_str))

        filename4 = self.name + '_punctuation.txt'
        e = open(filename4, 'r')
        d_str = e.read()
        e.close()
        self.punctuation = dict(eval(d_str))
                
    def add_file(self, filename):
        """ adds all of the text in
            the file identified by
            filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()

        self.add_string(text)

    def similarity_scores(self, other):
        """ computes and returns
            a list of log similarity
            scores measuring the
            similarity of self and
            other
        """
        word_score = compare_dictionaries(other.words, self.words)
        word_length_score = compare_dictionaries(other.word_lengths, \
                                                 self.word_lengths)
        stem_score = compare_dictionaries(other.stems, self.stems)
        sentence_length_score = compare_dictionaries(other.sentence_lengths, \
                                                     self.sentence_lengths)
        punctuation_score = compare_dictionaries(other.punctuation, \
                                                 self.punctuation)
        return [word_score] + [word_length_score] + [stem_score] + \
               [sentence_length_score] + [punctuation_score]

    def classify(self, source1, source2):
        """ compares the called
            TextModel object to
            two other "source"
            TextModel objects and
            determines the more
            likely source
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name + ':', scores1)
        print('scores for', source2.name + ':', scores2)
        
        count = 0
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]:
                count += 1
        if count >= 3:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)    
        
def sample_file_write(filename):
    """ A function that demonstrates
        how to write a Python dictionary
        to an easily-readable file.
    """

    d = {'test': 1, 'foo': 42}  # Create a sample dictionary.
    f = open(filename, 'w')     # Open file for writing.
    f.write(str(d))             # Writes the dictionary to the file.       
    f.close()                   # Close the file.
     
def sample_file_read(filename):
    """ A function that demonstrates how to read a
        Python dictionary from a file.
    """ 
    f = open(filename, 'r')
    d_str = f.read()
    f.close()

    d = dict(eval(d_str))

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('Shakespeare')
    source1.add_file('Shakespeare.txt')

    source2 = TextModel('Whitman')
    source2.add_file('Whitman.txt')

    new1 = TextModel('Twain')
    new1.add_file('Twain.txt')
    new1.classify(source1, source2)

    new2 = TextModel('CNN')
    new2.add_file('CNN.txt')
    new2.classify(source1, source2)

    new3 = TextModel('ScienceDaily')
    new3.add_file('ScienceDaily.txt')
    new3.classify(source1, source2)

    new4 = TextModel('ESPN')
    new4.add_file('ESPN.txt')
    new4.classify(source1, source2)
    
        
          
            
        
        
    

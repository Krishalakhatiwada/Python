import nltk
from nltk import tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')


print("1 #################################### Tokenizer ##################################################################")
text = "This is an example sentence. i love programming. it's how i work."
tokens = tokenize.NLTKWordTokenizer().tokenize(text)
print(tokens)

print("2 ####################################  Stemming ###################################################################")
stemmer = PorterStemmer()
words = ["running", "ran", "runs"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)

string_for_stemming = """ The crew of the USS Discovery discovered many discoveries.
 Discovering is what explorers do."""
words = tokenize.NLTKWordTokenizer().tokenize(string_for_stemming)
print(words)

stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)

print("3###################################### Lemmatization ############################################################")

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = tokenize.NLTKWordTokenizer().tokenize(string_for_lemmatizing)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(words)
print(lemmatized_words)
# print(WordNetLemmatizer.lemmatize(string_for_lemmatizing))


import nltk 
nltk.download('all')
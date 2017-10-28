from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

def clean(line):
    tokens = word_tokenize(line)
    tokens = [w.lower() for w in tokens]
    
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    
    words = [word for word in stripped if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in tokens]

    return ' '.join(words)

import numpy as np
import clean

def load_data(ham_file, spam_file):
    ham = list(open(ham_file, "r", encoding="utf8").readlines())
    ham = [h.strip() for h in ham]

    spam = list(open(spam_file, "r", encoding="utf8").readlines())
    spam = [s.strip() for s in spam]

    
    x_text = ham + spam
    x_text = [clean.clean(sentence) for sentence in x_text]

    ham_labels = [[0, 1] for h in ham]
    spam_labels = [[1, 0] for s in spam]

    y = np.concatenate([ham_labels, spam_labels])

    return [x_text, y]

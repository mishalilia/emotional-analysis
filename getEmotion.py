import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
#pip install scikit-learn==0.23.2

def getEmotion(word_list):
    csv_file = "./em.csv"
    with open(csv_file) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        texts = []
        texts_labels = []
        for line in reader:
            # print(line["emotion"],"",line["word"]),
            texts.append(line["word"])
            texts_labels.append(line["emotion"])

    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer('ngramrange=(1,2)')),
        ('clf', RandomForestClassifier())
    ])
    text_clf.fit(texts, texts_labels)
    stop_words = set(stopwords.words('english') + stopwords.words('russian'))
    word_tokens = word_tokenize(word_list)
    filtered_words = [w for w in word_tokens if not w in stop_words]
    filtered_words = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_words.append(w)
    # print(word_list)
    filtered_words = [' '.join(filtered_words)]
    print(filtered_words)
    res = text_clf.predict(filtered_words)
    return (res)

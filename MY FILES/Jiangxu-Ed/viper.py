import requests 
from viper import ViperPlagiarismChecker
from sklearn.feature_extraction import TfidVectorizer

viper = ViperPlagiarismChecker()

docs = [akashdasinn89.py, akbirooks007.py]

vectorizer = TfidVectorizer()
tfidf_vectors = vectorizer.fit_transform(docs)

results = viper.check_document(akashdasinn89.py, features=tfidf_vectors[0])

plagiarism_data = results.get('plagiarism_content')
plagiarism_score = results.get('plagiarism_score')



# url = 'https://www.viper.org/scan'
# files = {'file': open('akashdasinn89.py', 'rb')}

# response = requests.post(url, files=files)

# print(response.json())

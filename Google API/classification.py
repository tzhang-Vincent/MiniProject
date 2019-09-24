import argparse
import io
import json
import os
import re
from google.cloud import language
import numpy
import six

def classify(text):
    # Classify the input text with corresponding label
    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)

    label = language_client.classify_text(document)
    categories = label.categories

    result = {}

    for category in categories:
        result[category.name] = category.confidence

    print("Test Text is: ",text)
    for category in categories:
        print(u'=' * 10)
        print(u'{:<16}: {}'.format('category', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

def split_txt(inFile,des_name):
    with io.open(inFile,'r',encoding='gb18030') as f:
        text=f.read()
    a=re.split('\n',text)
    print(a)
    n=0
    for i in a:
        n+=1
        with open('{}/{}{}.txt'.format(des_name,des_name,n),'w', encoding='UTF-8') as f:
            f.write(i)



def FileForm(path, index_file):
    # Classify each text file in a path folder. Then dump the results into index_file.
    result = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        with io.open(file_path, 'r') as f:
            text = f.read()
            categories = classify(text)

            result[filename] = categories

    with io.open(index_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))
    return result


def query_category(index_file, category_string, n_top=5):
    #find the most 5 txt texts that are similar to the label

    with io.open(index_file, 'r') as f:
        index = json.load(f)

    # Make the category_string into a dictionary so that it is
    # of the same format as what we get by calling classify.
    query_categories = {category_string: 1.0}

    similarities = []
    for filename, categories in six.iteritems(index):
        similarities.append(
            (filename, similarity(query_categories, categories)))

    similarities = sorted(similarities, key=lambda p: p[1], reverse=True)

    print('=' * 20)
    print('Query: {}\n'.format(category_string))
    print('\nMost similar {} indexed texts:'.format(n_top))
    for filename, sim in similarities[:n_top]:
        print('\tFilename: {}'.format(filename))
        print('\tSimilarity: {}'.format(sim))
        print('\n')

    return similarities

def split_labels(categories):
    _categories = {}
    for name, confidence in six.iteritems(categories):
        labels = [label for label in name.split('/') if label]
        for label in labels:
            _categories[label] = confidence

    return _categories


def similarity(categories1, categories2):
    """Cosine similarity of the categories treated as sparse vectors."""
    categories1 = split_labels(categories1)
    categories2 = split_labels(categories2)

    norm1 = numpy.linalg.norm(list(categories1.values()))
    norm2 = numpy.linalg.norm(list(categories2.values()))

    # Return the smallest possible similarity if either categories is empty.
    if norm1 == 0 or norm2 == 0:
        return 0.0

    # Compute the cosine similarity.
    dot = 0.0
    for label, confidence in six.iteritems(categories1):
        dot += confidence * categories2.get(label, 0.0)

    return dot / (norm1 * norm2)

if __name__ == '__main__':
    # classify("Yesterday, I took a train trip from Boston to the New York City. It is really a good experience for my vacation and I enjoy it. During my trip, I took some photos inside the train and recorded lots of amazing scenes")
    # classify("Los Angeles is good place and the people there are friendly. The Disneyand is interesting. The Universal Studios is also fantastic.")
    # classify("We climbed mountain there and participated in the skiing activities. I don't like to stay in such a cold place for a long time although the scenes there are very impressive. When I took photos at the viewing platform on a high mountain, I felt too cold to firmly grasp my camera. It is a good place to travel but not a good place to live in.")
    # FileForm("C:/Users/Vincent/Desktop/601/TestText","index")
    # query_category("index","/Travel/Tourists Destinations")
    split_txt("first_test.txt","abcd")


import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six

def classify(text, verbose=True):
    """Classify the input text into categories. """
    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

def index(path, index_file):
    """Classify each text file in a directory and write
    the results to the index_file.
    """

    result = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if not os.path.isfile(file_path):
            continue

        try:
            with io.open(file_path, 'r') as f:
                text = f.read()
                categories = classify(text, verbose=False)

                result[filename] = categories
        except Exception:
            print('Failed to process {}'.format(file_path))

    with io.open(index_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

    print('Texts indexed in file: {}'.format(index_file))
    return result

def query(index_file, text, n_top=3):
    """Find the indexed files that are the most similar to
    the query text.
    """

    with io.open(index_file, 'r') as f:
        index = json.load(f)

    # Get the categories of the query text.
    query_categories = classify(text, verbose=False)

    similarities = []
    for filename, categories in six.iteritems(index):
        similarities.append(
            (filename, similarity(query_categories, categories)))

    similarities = sorted(similarities, key=lambda p: p[1], reverse=True)

    print('=' * 20)
    print('Query: {}\n'.format(text))
    for category, confidence in six.iteritems(query_categories):
        print('\tCategory: {}, confidence: {}'.format(category, confidence))
    print('\nMost similar {} indexed texts:'.format(n_top))
    for filename, sim in similarities[:n_top]:
        print('\tFilename: {}'.format(filename))
        print('\tSimilarity: {}'.format(sim))
        print('\n')

    return similarities

def query_category(index_file, category_string, n_top=3):
    """Find the indexed files that are the most similar to
    the query label.

    The list of all available labels:
    https://cloud.google.com/natural-language/docs/categories
    """

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
    """The category labels are of the form "/a/b/c" up to three levels,
    for example "/Computers & Electronics/Software", and these labels
    are used as keys in the categories dictionary, whose values are
    confidence scores.

    The split_labels function splits the keys into individual levels
    while duplicating the confidence score, which allows a natural
    boost in how we calculate similarity when more levels are in common.

    Example:
    If we have

    x = {"/a/b/c": 0.5}
    y = {"/a/b": 0.5}
    z = {"/a": 0.5}

    Then x and y are considered more similar than y and z.
    """
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
    classify("Yesterday, I took a train trip from Boston to the New York City. It is really a good experience for my vacation and I enjoy it. During my trip, I took some photos inside the train and recorded lots of amazing scenes")
    # classify("Los Angeles is good place and the people there are friendly. The Disneyand is interesting. The Universal Studios is also fantastic.")
    # classify("We climbed mountain there and participated in the skiing activities. I don't like to stay in such a cold place for a long time although the scenes there are very impressive. When I took photos at the viewing platform on a high mountain, I felt too cold to firmly grasp my camera. It is a good place to travel but not a good place to live in.")
    index("C:/Users/Vincent/Desktop/601/TestText","index")
    query_category("index","/Travel/Tourists Destinations")


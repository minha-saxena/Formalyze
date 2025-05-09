import os
import nltk
import utils
import reddit_dataset_generator
import brown_dataset_generator
import pickle
import random
import operator
import functools
import numpy as np
from keras.preprocessing.text import Tokenizer



def get_word_embeddings_weight_matrix(tokenizer):
    glove_embeddings = utils.load_glove_embeddings(r'C:\Users\minha\Desktop\project work\FormalityClassifier-master\data\glove.6B\glove.6B.100d.txt')

    
    unique_words_count = len(tokenizer.word_counts) + 1
    embedding_matrix = np.zeros((unique_words_count, 100))

    for word, i in tokenizer.word_index.items():
        embedding_vector = glove_embeddings.get(word)
        if embedding_vector is not None:
            
            embedding_matrix[i] = embedding_vector

    return embedding_matrix


def get_sentence_matrices(mapped_informal_sentences, mapped_formal_sentences, max_sentence_length=30):
    total_sentence_count = len(mapped_informal_sentences) + len(mapped_formal_sentences)
    sentence_matrix = np.zeros((total_sentence_count, max_sentence_length))
    label_matrix = np.zeros((total_sentence_count, 2))

    informal_sent_counter = 0
    formal_sent_counter = 0

    for sent_index in range(0, total_sentence_count):
        full_sentence = None
        if (random.random() < 0.5 and informal_sent_counter < len(mapped_informal_sentences)) or formal_sent_counter >= len(mapped_formal_sentences):
            full_sentence = mapped_informal_sentences[informal_sent_counter]
            informal_sent_counter += 1

            label_matrix[sent_index][0] = 1
        elif formal_sent_counter < len(mapped_formal_sentences):
            full_sentence = mapped_formal_sentences[formal_sent_counter]
            formal_sent_counter += 1

            label_matrix[sent_index][1] = 1
        else:
            print('Oh no!')
            exit(-1)

        full_sentence_np = np.array(full_sentence)

        
        pad_amount = (0, max_sentence_length - len(full_sentence_np))
        full_sentence_np = np.pad(full_sentence_np, pad_amount, 'constant')

        sentence_matrix[sent_index] = full_sentence_np

    return sentence_matrix, label_matrix


def get_sentence_matrix(tokenizer, lst_sentences, max_sentence_length=30):
    mapped_sentences = tokenizer.texts_to_sequences(lst_sentences)

    total_sentence_count = len(mapped_sentences)
    sentence_matrix = np.zeros((total_sentence_count, max_sentence_length))

    for sent_index in range(0, total_sentence_count):
        full_sentence = mapped_sentences[sent_index]
        full_sentence_np = np.array(full_sentence)

        
        pad_amount = (0, max_sentence_length - len(full_sentence_np))
        full_sentence_np = np.pad(full_sentence_np, pad_amount, 'constant')

        sentence_matrix[sent_index] = full_sentence_np

    return sentence_matrix


def get_numerical_training_data(lst_informal_sentences, lst_formal_sentences):
    all_sentences = lst_informal_sentences + lst_formal_sentences
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(all_sentences)

    mapped_informal_sentences = tokenizer.texts_to_sequences(lst_informal_sentences)
    mapped_formal_sentences = tokenizer.texts_to_sequences(lst_formal_sentences)

    X, Y = get_sentence_matrices(mapped_informal_sentences, mapped_formal_sentences)
    word_embeddings = get_word_embeddings_weight_matrix(tokenizer)

    return X, Y, word_embeddings


def get_numerical_test_data(lst_informal_sentences, lst_formal_sentences, lst_sentences_raw, pickle_path=None, skip_word_tokenization=False):
    if pickle_path is None:
        all_sentences = lst_informal_sentences + lst_formal_sentences
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(all_sentences)

        with open('tokenizer.p', 'wb') as f_tokenizer:
            pickle.dump(tokenizer, f_tokenizer)
    else:
        with open(os.path.join(pickle_path, 'tokenizer.p'), 'rb') as f_tokenizer:
            tokenizer = pickle.load(f_tokenizer)

    if not skip_word_tokenization:
        lst_sentences_tokenized = map(nltk.word_tokenize, lst_sentences_raw)
    else:
        lst_sentences_tokenized = lst_sentences_raw
    lst_sentences_cleaned = list(clean_sentences(lst_informal_sentences, lst_formal_sentences, lst_sentences_tokenized, pickle_path))

    X = get_sentence_matrix(tokenizer, lst_sentences_cleaned)
    return X


def get_training_sentences(sentence_limit=10000):
    reddit_data_gen = reddit_dataset_generator.sentence_generator_from_file(r'C:\Users\minha\Desktop\project work\FormalityClassifier-master\data\reddit_comments.txt', sentence_limit=sentence_limit)
    brown_data_gen = brown_dataset_generator.sentence_generator(sentence_limit=sentence_limit)

    
    reddit_sentences = list(reddit_data_gen)
    brown_sentences = list(brown_data_gen)


    words = functools.reduce(operator.add, reddit_sentences + brown_sentences)
    dist = nltk.FreqDist(words)

    # remove uncommon words
    reddit_sentences_cleaned = utils.remove_uncommon_words(dist, reddit_sentences)
    brown_sentences_cleaned = utils.remove_uncommon_words(dist, brown_sentences)

    return reddit_sentences_cleaned, brown_sentences_cleaned


def clean_sentences(lst_informal_sentences, lst_formal_sentences, sentences_to_clean, pickle_path=None):
    if pickle_path is None:
        words = functools.reduce(operator.add, lst_informal_sentences + lst_formal_sentences)
        dist = nltk.FreqDist(words)
        with open('freq_dist.p', 'wb') as f_dist:
            pickle.dump(dist, f_dist)
    else:
        with open(os.path.join(pickle_path, 'freq_dist.p'), 'rb') as f_dist:
            dist = pickle.load(f_dist)

    return utils.remove_uncommon_words(dist, sentences_to_clean)


if __name__ == '__main__':
    reddit_sent_gen, brown_sent_gen = get_training_sentences(sentence_limit=10000)

    lst_reddit_sentences = list(reddit_sent_gen)
    lst_brown_sentences = list(brown_sent_gen)

    utils.print_sentences(lst_reddit_sentences, 100)
    utils.print_sentences(lst_brown_sentences, 100)

    test_sentences = [
        'Each hash block is composed of at most 172 content blocks, and stores the sha1 hash for each block.',
        'That guy over there is kinda sketchy.',
        'Who was it that shot the Sheriff?',
        'You wouldn\'t believe how many people showed up, it was wonderful.'
    ]
    X_test = get_numerical_test_data(lst_reddit_sentences, lst_brown_sentences, test_sentences)

    print('X_test Shape: ' + str(X_test.shape))
    print('X_test Min: ' + str(X_test.min()))
    print('X_test Mean: ' + str(X_test.mean()))
    print('X_test Max: ' + str(X_test.max()))
    print()

    X, Y, word_embeddings = get_numerical_training_data(lst_reddit_sentences, lst_brown_sentences)

    print('X Shape: ' + str(X.shape))
    print('X Min: ' + str(X.min()))
    print('X Mean: ' + str(X.mean()))
    print('X Max: ' + str(X.max()))
    print()

    print('Y Shape: ' + str(Y.shape))
    print('Y Min: ' + str(Y.min()))
    print('Y Mean: ' + str(Y.mean()))
    print('Y Max: ' + str(Y.max()))
    print()

    print('Word Embedding Shape: ' + str(word_embeddings.shape))
    print('Word Embedding Min: ' + str(word_embeddings.min()))
    print('Word Embedding Mean: ' + str(word_embeddings.mean()))
    print('Word Embedding Max: ' + str(word_embeddings.max()))

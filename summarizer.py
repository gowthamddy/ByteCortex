import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Used to rank sentences according sentence scores
from heapq import nlargest

def estimated_reading_time(text):
    mins = int(len(text)/200)
    seconds = int((float(len(text)/200) - mins)*60)
    return "( Estimated reading time: {} mins, {} seconds )".format(str(mins),str(seconds))

def summarizer(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text.lower() not in word_frequencies.keys():
                    # Adding new word to word_frequency
                    word_frequencies[word.text.lower()] = 1
                else:
                    # Incrementing frequency in word already exists
                    word_frequencies[word.text.lower()] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] /= max_frequency
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    sentences_percent = 0.2
    sentences_selected = int(len(sentence_tokens)*sentences_percent)

    summary_sentences = nlargest(sentences_selected, sentence_scores, key = sentence_scores.get)
    summary_sentences = [word.text for word in summary_sentences]
    summary = " ".join(summary_sentences)
    return summary
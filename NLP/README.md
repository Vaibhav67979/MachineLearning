# Natural Language Processing
## Roadmap 
|No. | Topic | Techniques | Purpose | 
|----|-----|----|----|
|1. | Text preprocessing 1 | tokenization, lemmatization | cleaning the text |
|2. | Text preprocessing 2 | BOW(Bag of words), TFIDF, unigrams | converting input text to vectors |
|3. | Text preprocessing 3 | Word2vec, avgword2vec | convert input text to vectors |
|4. | RNN, LSTM RNN, GRU RNN | Neural networks - DL |
|5. | Text preprocessing 4 | Word embedding |convert input text to vectors |
|6. | Transformners |
|7. | BERT |

## Introduction 

Field of study focused on making sense of language
- Topic identification
- Text classification

NLP Applications include:
- Chatbots
- Translation
- Sentiment analysis

## Regular Expressions(RE/Regex) :

- Strings with a special syntax.
- Allow us to match patterns.
- Applicatiions of regular expressions:
  1. find all web links in a document.
  2. parse email addresses.
  3. Remove/replace unwanted characters.

### Import and Usage

```python
import re
re.match('abc', 'abcdef')
```
```
<re.Match object; span=(0, 3), match='abc'>
```
---
```python
re.match('abc', 'abcde')
```
```
<re.Match object; span=(0, 3), match='abc'>
```
---
```python
re.search('cd', 'abcde')
```
```
<re.Match object; span=(2, 4), match='cd'>
```
---

### Common regex patterns

|patterns | matches | example |
|---------|---------|---------|
|\w+ | word | 'Magic' |
| \d+ | digit | 9 |
| \s | space | ' ' |
| .* | wildcard | 'fkdja' |
| + or * | greedy match | 'aaaaa' |
| \S | not space | 'no_spaces' |
| [a-z] | lowercase group | 'adbdv' |


## Tokenization

Tokenization is the process of transforming a string or document into smaller chunks, which we call tokens.

Examples:
1. Breaking out words in a sentence.
2. Separating punctuation.
3. Separtaing all hashtags in a tweet.

### Terminologies 
1. Corpus - paragraph
2. Documents - sentences
3. Vocabulary - Unique words present
4. Words - all the words

### NLTK

`nltk` - natural language toolkit.

```python
from nltk.tokenize import word_tokenize
word_tokenize("Hi there")
```

### Why tokenization?

- Easier to map part of speech.
- Matching common words.
- Removing/replacing unwanted tokens.

### Other nltk tokenizers

- `sent_tokenize` : tokenize a document into sentences.
- `regexp_tokenize` : tokenize a string or document based on a regular expression pattern.
- `TweetTokenizer` : special class for tweet tokenization, allowing you to separate hashtags, mentions, and lots of exclamatiom points.

### [NLTK examples](https://github.com/Vaibhav67979/MachineLearning/blob/0cf3a5fd81728f33b2659071b1d7831f5e92a058/NLP/Code(examples)/TokenizationEx.ipynb)

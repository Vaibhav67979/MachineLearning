# Natural Language Processing
> Everything I learnt in the Datacamp course of "Introduction to Natural Language Processing in Python"
>
> URL - [Introduction to Natural Language Processing in Python](https://app.datacamp.com/learn/courses/introduction-to-natural-language-processing-in-python)


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


### Practice 1
```python
# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.split(digits, my_string))
```

## Tokenization

Tokenization is the process of transforming a string or document into smaller chunks, which we call tokens.

Examples:
1. Breaking out words in a sentence.
2. Separating punctuation.
3. Separtaing all hashtags in a tweet.


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

- `sent_tokenize` : tokenize a document inot sentences.
- `regexp_tokenize` : tokenize a string or document based on a regular expression pattern.
- `TweetTokenizer` : special class for tweet tokenization, allowing you to separate hashtags, mentions, and lots of exclamatiom points.

### Practice 2

```python
# Import necessary modules
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)
```

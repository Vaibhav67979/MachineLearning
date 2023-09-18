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

## Regukar Expressions(RE/Regex) :

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


### Exercise
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



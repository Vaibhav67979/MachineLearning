# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[A-Za-z\s]+:"
print(re.match(pattern2, sentences[3]))

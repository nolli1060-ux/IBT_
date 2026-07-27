def word_frequency(text):
    text = text.lower()
    punctuation = ".,!?"
    for char in punctuation:
        text = text.replace(char, "")
    
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
            
    return counts
print(word_frequency("Hello world, hello!"))
 text = "  Hello Python World!  "
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Trimmed:", text.strip())
print("Replace 'Python' with 'Programming':", text.replace("Python", "Programming"))
print("Count of 'o':", text.count("o"))
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with 'World!':", text.strip().endswith("World!"))
words = text.strip().split()
print("Words:", words)
print("Joined with '-':", "-".join(words))

O/P:
Length: 23
Uppercase:   HELLO PYTHON WORLD!  
Lowercase:   hello python world!  
Trimmed: Hello Python World!
Replace 'Python' with 'Programming':   Hello Programming World!  
Count of 'o': 3
Starts with 'Hello': True
Ends with 'World!': True
Words: ['Hello', 'Python', 'World!']
Joined with '-': Hello-Python-World!

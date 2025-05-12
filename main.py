import random

def advanced_encode(name, add_symbols=False, random_case=False, reversible=False):
    # Extended leet substitutions (multiple options per letter)
    leet_dict = {
        'a': ['4', '@', '∆', '^'],
        'b': ['8', '|3', 'ß'],
        'c': ['(', '<', '©'],
        'd': ['|)', 'Ð', 'đ'],
        'e': ['3', '€', '∃'],
        'f': ['ƒ', '|='],
        'g': ['9', '&', 'C-'],
        'h': ['#', '|-|', '}{'],
        'i': ['1', '!', '|'],
        'j': ['_|', '¿'],
        'k': ['|<', 'X'],
        'l': ['1', '|_', 'Ł'],
        'o': ['0', '°', '()'],
        's': ['5', '$', '§'],
        't': ['7', '+', '†'],
        'z': ['2', '~/_', '≥'],
    }
    
    encoded = []
    for char in name.lower():
        if char in leet_dict:
            # Randomly pick a substitution
            replacement = random.choice(leet_dict[char])
            encoded.append(replacement)
        else:
            encoded.append(char)
    
    # Randomize case (e.g., "G4T" → "g4t" or "G4T")
    if random_case:
        encoded = [c.upper() if random.choice([True, False]) else c.lower() for c in encoded]
    
    # Add symbols between letters (e.g., "G4T" → "G_4_T!")
    if add_symbols:
        symbols = ['_', '-', '!', '.', '*']
        encoded = [c + random.choice(symbols) if i < len(encoded)-1 else c for i, c in enumerate(encoded)]
    
    # Optional: Add a reversible hint (e.g., base64)
    if reversible:
        import base64
        original_bytes = name.encode('utf-8')
        encoded_hint = base64.b64encode(original_bytes).decode('utf-8')
        encoded.append(f" (reversible: {encoded_hint})")
    
    return ''.join(encoded)

# User input
name = input("Enter a name to encode: ")
encoded = advanced_encode(name, add_symbols=True, random_case=True, reversible=False)
print(f"Encoded: {encoded}")

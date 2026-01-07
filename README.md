# Random Letter Generator (Until "w")

## Description
This Python script continuously generates and prints random alphabetic characters (both uppercase and lowercase) until the letter **`w`** is randomly selected.  
All characters are printed on the same line in real time.

## How It Works
- Uses the `string` module to get all ASCII letters.
- Uses the `random` module to randomly select letters.
- Keeps printing letters until `"w"` appears.
- Output is flushed immediately so letters appear one by one without delay.

## Code
```python
import string
import random

letters = string.ascii_letters
c = ""

while c != "w":
    c = random.choice(letters)
    print(c, end="", flush=True)

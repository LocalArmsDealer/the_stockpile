# List of denied characters. This will be used later for the algebra calculator when I integrate it and when I learn how to check for list characters in inputs.
# If you know how to check for list characters in inputs, feel free to fix the code, it would be greatly appreciated.
denied = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
equat = input("""Use '+' for addition, '-' for subtraction, '/' for division, '*' for multiplication, and '%' for finding remainders.
Input equation here:""")

# Calculator code
if "a" or "A" or "b" or "B" or "c" or "C" or "d" or "D" or "e" or "E" or "f" or "F" or "g" or "G" or "h" or "H" or "i" or "I" or "j" or "J" or "k" or "K" or "l" or "L" or "m" or "M" or "n" or "N" or "o" or "O" or "p" or "P" or "q" or "Q" or "r" or "R" or "s" or "S" or "t" or "T" or "u" or "U" or "v" or "V" or "w" or "W" or "x" or "X" or "y" or "Y" or "z" or "Z" not in equat:
    print(eval(equat))
else:
    print("Error.")

def crunch_recursive(charset, current_string, min_length, max_length):
    if len(current_string) >= min_length:
        print(current_string)
        
    if len(current_string) == max_length:
        return

    for char in charset:
        crunch_recursive(charset, current_string + char, min_length, max_length)

import sys
charset = sys.argv[3] if len(sys.argv) > 3 else 'abcdeghijklmnopqrstuvwxyz'
min_length, max_length = map(int, sys.argv[1:3])
crunch_recursive(charset, "", min_length, max_length)
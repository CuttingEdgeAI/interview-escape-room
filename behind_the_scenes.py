def do_the_thing(s):
    clear_text = rot13(s)
    if "http" in clear_text: 
        print("Go here in your browser! {}".format(clear_text))
    else:
        print("Here is something [ {} ] but it doesn't look useful yet.".format(clear_text))
    exit()

def rot13(s):
    lower_chars = ''.join(chr(c) for c in range (97,123)) #ASCII a-z
    upper_chars = ''.join(chr(c) for c in range (65,91)) #ASCII A-Z
    lower_encode = lower_chars[13:] + lower_chars[:13] #shift 13 bytes ?
    upper_encode = upper_chars[13:] + upper_chars[:13] #shift 13 bytes ?
    output = "" #outputstring
    for c in s:
        if c in lower_chars:
                output = output + lower_encode[lower_chars.find(c)]
        elif c in upper_chars:
            output = output + upper_encode[upper_chars.find(c)]
        else:
            output = output + c
    return output

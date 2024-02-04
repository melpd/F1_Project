cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

#encrypted_file = open("encrypted_message_one.txt", 'r')

#encrypted_message = encrypted_file.readline()

#encrypted_file.close()

# Write code below
encrypted_message = 'atnng}vnn5}aglt}ygc}vzt}avkeis}v}sggj}qtotqutz[}e}vnqg}aglt}uaeq}vqqesiotiu}eq}igu}ugg}hvj}-*}hy}uat}dvy}daent}e}avkt}ygcz}vuutiuegi}e}uagcsau}e}dgcnj}sekt}ygc}v}mcgut}xzgo}ugo}sgndvy}hcu}uaeq}mcgut}eq}ei}uat}qtrgij}aejjti}otqqvst%'
decrypted_message = ''
for key, val in cipher.items():
    for l in encrypted_message:
        if val == l:
            decrypted_message += key
print(decrypted_message)
def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob.strip():
        return 'Fine. Be that way!'
    elif hey_bob.isupper() and hey_bob[len(hey_bob)-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob[len(hey_bob)-1] == '?':
        return 'Sure.'
    elif not hey_bob.strip():
        return 'Fine. Be that way!'
    return 'Whatever.'


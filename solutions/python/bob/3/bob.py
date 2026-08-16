"""
    This module contains the function for reponses.
"""

def response(hey_bob):
    """
        Parameters:
            hey_bob(string): Its the question or sentences for bob.
        Returns:
            Reponse(string): It's the response by bob at the questions or sentences.
    """
    hey_bob = hey_bob.strip()
    if not hey_bob.strip():
        return 'Fine. Be that way!'
    if hey_bob.isupper() and hey_bob[len(hey_bob)-1] == '?':
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    if hey_bob[len(hey_bob)-1] == '?':
        return 'Sure.'
    if not hey_bob.strip():
        return 'Fine. Be that way!'
    return 'Whatever.'
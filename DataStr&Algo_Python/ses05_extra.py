def caesar_cipher_encrypt(str_to_encrypt, n):
    """
    Encrypt string using Caesar cipher by n positions
    
    This function builds one of the most widely known encryption 
    techniques, _Caesar's cipher_. This works as follows: 
    you should be given a string str_to_encrypt and an encoding 
    integer n, which then be used to replace each initial letter 
    to the encrypted one by simply shifting the letter by n positions.
    
    Parameters:
        str_to_encrypt: string
        n: shift parameter
        
    Returns:
        n-encrypted string
    
    Examples:
    >>> caesar_cipher_encrypt('a', 1)
    'b'
    >>> caesar_cipher_encrypt('abc', 1)
    'bcd'
    >>> caesar_cipher_encrypt('abc', 4)
    'efg'
    >>> caesar_cipher_encrypt('thisistherealdeal', 6)
    'znoyoyznkxkgrjkgr'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    new_char = ""
    encrypted = ""
    for char in alphabet:
        alphabet_list.append(char) 
    for char in alphabet:
        alphabet_list.append(char)    
    
    n = n % 26
    for char in str_to_encrypt:
        digit = alphabet_list.index(char)
        new_char = alphabet_list[digit+ n]
        encrypted = encrypted+new_char

    return encrypted
        
    

def caesar_cipher_decrypt(str_to_decrypt, n):
    """
    Decrypt Caesar cipher by n positions
    
        
    Parameters:
        str_to_decrypt: string
        n: shift parameter
        
    Returns:
        n-decrypted string
    
    Examples:
    >>> caesar_cipher_decrypt('b', 1)
    'a'
    >>> caesar_cipher_decrypt('bcd', 1)
    'abc'
    >>> caesar_cipher_decrypt('efg', 4)
    'abc'
    >>> caesar_cipher_decrypt('znoyoyznkxkgrjkgr', 6)
    'thisistherealdeal'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    new_char = ""
    decrypted = ""

    for char in alphabet:
        alphabet_list.append(char) 
    for char in alphabet:
        alphabet_list.append(char)  

    
    n = n % 26
    for char in str_to_decrypt:
        digit = alphabet_list.index(char)
        new_char = alphabet_list[digit- n]
        decrypted = decrypted+new_char

    return decrypted

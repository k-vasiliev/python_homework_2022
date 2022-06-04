def get_token():
    with open('token.txt', 'r') as token_file:
        return str(token_file.readlines()[0])
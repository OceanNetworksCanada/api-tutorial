from IPython.core.display import display, HTML
from getpass import getpass

html_template = """

<iframe src="https://data.oceannetworks.ca/Profile" width="600" height="400"></iframe>

"""

def get_ONC_token():
    try:
        with open('token.txt','rt') as token_file:
            token = token_file.readline()
            
    except FileNotFoundError:
        display(HTML(html_template))
        token = getpass('Token:')
        print('Writing token')
        with open('token.txt','wt') as token_file:
            token_file.write(token)
            print('Written token')
    
    
    return token
    


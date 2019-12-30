#! python

# mcb.pyw - Saves and loads peices of text to the clipboard.
HELP = ('mcb <keyword> - Loads keyword to clipboard\n'
        'mcb add <keyword> - Saves clipboard to keyword\n'
        'mcb rm <keyword> - Removes the keyword from the list\n'
        'mcb <keyword> disp - Displays contents of keyword\n'
        'mcb list - Prints keywords to the terminal'
        )

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
mcbKeys = list(mcbShelf.keys())
try:
    arg1 = str(sys.argv[1])
except:
    for keys in mcbShelf.keys():
            print(keys)

# add or remove clipboard content.
if len(sys.argv) == 3:
    arg2 = str(sys.argv[2])
    if arg1.lower() == 'add':
        mcbShelf[arg2] = pyperclip.paste()
        print(f'\'{arg2}\' has been added to mcb')
    elif arg1.lower() == 'rm':
        try:
            del mcbShelf[arg2]
            print(f'\'{arg2}\' has been removed from mcb')
        except:
            sys.exit(f'\'{arg2}\' not found in mcb.  Type \'mcb help\' for a list of commands.')
    elif arg2.lower() =='disp':
        try:
            print(mcbShelf[arg1])
        except:
            sys.exit(f'\'{arg1}\' not found in mcb.  Type \'mcb lsit\' for a list of keywords.')
    else:
        sys.exit(f'\'{arg1} {arg2}\' not a recognized command in mcb.  Type \'mcb help\' for a list of commands.')

elif len(sys.argv) == 2:
    # List keywords and load content.
    if arg1.lower() == 'list':
        for keys in mcbShelf.keys():
            print(keys)
    elif arg1.lower() == 'help':
        sys.exit(HELP)
    elif arg1 in mcbShelf:
        pyperclip.copy(mcbShelf[arg1])
        print(f'\'{arg1}\' sucessfully copied')
    else:
        print(f'Keyword \'{arg1}\' not found.  Type \'mcb list\' for a list of keywords.')

mcbShelf.close()
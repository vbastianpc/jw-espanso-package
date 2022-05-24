import os
import sys
import re
import json
from pathlib import Path


with_unidecode = False
try:
    from unidecode import unidecode as ud
    with_unidecode = True
except ModuleNotFoundError:
    from subprocess import run
    run([sys.executable, '-m', 'pip', 'install', 'Unidecode'])
    try:
        from unidecode import unidecode as ud # type: ignore
        with_unidecode = True
    except ModuleNotFoundError:
        pass


BOOKNAMES_PATH = Path(__file__).parent / 'bibles'


def get_booknames(langcode):
    with open(BOOKNAMES_PATH / f'{langcode}.txt') as f:
        return [bookname.rstrip('\n') for bookname in f.readlines()]

def search_bookname(langcode, input_bookname):
    booknames = get_booknames(langcode)
    for booknum, bookname in enumerate(booknames, start=1):
        alias = bookname.lower().replace(' ', '')
        if alias.startswith(input_bookname) or (ud(alias).startswith(ud(input_bookname)) if with_unidecode else False):
            return booknum, bookname
    else:
        raise TypeError(f'{input_bookname!r} not found in {langcode!r} bible')


if __name__ == '__main__':
    bibles = json.load(open(BOOKNAMES_PATH / 'bibles.json'))
    jw_lang_prefer = sys.argv[1] if len(sys.argv) > 1 else 'VT'
    pub = sys.argv[2] if len(sys.argv) > 2 else 'nwtsty'
    pub = pub if pub in bibles[jw_lang_prefer]['pub'] else bibles[jw_lang_prefer]['pub'][0]
    user_input_bookname = os.getenv('ESPANSO_BOOKNAME', 'Sáng').lower().replace(' ', '')
    chapter = int(os.getenv('ESPANSO_CHAPTER', '1'))
    verses = os.getenv('ESPANSO_VERSES', '1-3')

    langcodes = [bibles[jw_lang_prefer]['langcode']] + [file.stem for file in BOOKNAMES_PATH.glob('*.txt')]
    print(jw_lang_prefer, pub, user_input_bookname, chapter, verses, BOOKNAMES_PATH, sep='\n')
    for langcode in langcodes:
        try:
            booknum, bookname = search_bookname(langcode, user_input_bookname)
        except TypeError:
            pass
        else:
            break
    else:
        print(f'{user_input_bookname} {chapter}:{verses}??') # not found
        sys.exit()


    split_verses = re.split(r'[ ,-]+', verses)
    first_verse, last_verse = int(split_verses[0]), int(split_verses[-1])
    code_citation = f'{booknum:0=2}{chapter:0=3}{first_verse:0=3}' + (f'-{booknum:0=2}{chapter:0=3}{last_verse:0=3}' if first_verse != last_verse else '')

    url = f'https://www.jw.org/finder?wtlocale={jw_lang_prefer}&prefer=lang&bible={code_citation}&pub={pub}'

    print(f'[{bookname} {chapter}:{verses}]({url})')


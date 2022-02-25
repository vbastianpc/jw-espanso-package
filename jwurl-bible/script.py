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


jw_lang_prefer = sys.argv[1] if len(sys.argv) > 1 else 'S'
book = os.getenv('ESPANSO_BOOKNAME', 'Sáng').lower().replace(' ', '')
chapter = int(os.getenv('ESPANSO_CHAPTER', '1'))
verses = os.getenv('ESPANSO_VERSES', '1')
split_verses = re.split(r'[ ,-]+', verses)

booknames_path = Path(__file__).parent / 'booknames'


def search_bookname(file):
    data = json.load(open(file))
    for booknum, bookname in enumerate(data['booknames'], start=1):
        alias = bookname.lower().replace(' ', '')
        if alias.startswith(book) or (ud(alias).startswith(ud(book)) if with_unidecode else False):
            return data.get('isSignLanguage'), file.stem, booknum, bookname


for file in [booknames_path / f'{jw_lang_prefer}.json'] + list(booknames_path.glob('*.json')):
    info = search_bookname(file)
    if info is not None:
        break
else:
    print(f'{book} {chapter}:{verses}??') # book not found
    sys.exit()


is_sign_language, lang_code, booknum, bookname = info
first_verse, last_verse = int(split_verses[0]), int(split_verses[-1])
url = f'https://www.jw.org/finder?wtlocale={lang_code}&bible={booknum:0=2}{chapter:0=3}{first_verse:0=3}'
if first_verse != last_verse:
    url += f'-{booknum:0=2}{chapter:0=3}{last_verse:0=3}'
if is_sign_language:
    url += '&pub=nwt'

print(f'[{bookname} {chapter}:{verses}]({url})')

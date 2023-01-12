# -*- coding:utf-8 -*-

from typing import Dict
from bs4 import BeautifulSoup
import requests

from daumdict.exceptions import UnavailableLanguage, TranslationNotFound


LANG_TO_DAUMDICT_LANG: Dict[str, str] = {
    "ko": "kor",
    "en": "eng",
}


def translate(lang: str, word: str) -> str:
    if lang not in LANG_TO_DAUMDICT_LANG:
        raise UnavailableLanguage
    daumdict_lang: str = LANG_TO_DAUMDICT_LANG[lang] # lang ?
    query_url: str = f'https://alldic.daum.net/search.do?q={word}'
    resp = requests.get(query_url)
    soup = BeautifulSoup(resp.text, features="html.parser")
    translation_list = soup.select(f'div[data-tiara-layer="word {daumdict_lang}"] .cleanword_type .list_search li')
    if len(translation_list) == 0:
        raise TranslationNotFound
    translation_list = [translation.get_text() for translation in translation_list]

    return f"{word}: {' '.join(translation_list)}"


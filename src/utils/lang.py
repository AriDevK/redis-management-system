import enum
from os import path, getcwd
from babel.support import Translations


class LangCode(enum.Enum):
    EN = 'en_US'
    ES = 'es_MX'
    NO = 'nn_NO'


class Language:
    def __init__(self, lang: str):
        __LOCALE_PATH = path.join(getcwd(), 'locale')
        self._lang = lang
        self._translations = Translations.load(__LOCALE_PATH, [self._lang])
        self._ = self._translations.gettext

    @property
    def lang(self) -> str:
        return self._lang

    @lang.setter
    def lang(self, value):
        self._lang = value

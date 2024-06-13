import pytest
from text_processing import clean_text, tokenize, count_words

def test_clean_text_le_corbeau():
    text = ("Mais le Corbeau, perché solitairement sur ce buste placide, parla "
            "ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne "
            "proférâi donc rien de plus: il n'agita donc pas de plume--jusqu'à ce "
            "que je fis à peine davantage que marmotter «D'autres amis déjà ont "
            "pris leur vol--demain il me laissera comme mes Espérances déjà ont "
            "pris leur vol.» Alors l'oiseau dit: «Jamais plus.»")
    expected = ("mais le corbeau perché solitairement sur ce buste placide parla "
                "ce seul mot comme si son âme en ce seul mot il la répandait je ne "
                "proférâi donc rien de plus il n'agita donc pas de plume jusqu'à ce "
                "que je fis à peine davantage que marmotter d'autres amis déjà ont "
                "pris leur vol demain il me laissera comme mes espérances déjà ont "
                "pris leur vol alors l'oiseau dit jamais plus")
    assert clean_text(text) == expected, "Clean_text failed on Le Corbeau"

def test_tokenize_le_corbeau():
    text = ("Mais le Corbeau, perché solitairement sur ce buste placide, parla "
            "ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne "
            "proférâi donc rien de plus: il n'agita donc pas de plume--jusqu'à ce "
            "que je fis à peine davantage que marmotter «D'autres amis déjà ont "
            "pris leur vol--demain il me laissera comme mes Espérances déjà ont "
            "pris leur vol.» Alors l'oiseau dit: «Jamais plus.»")
    expected = ["mais", "le", "corbeau", "perché", "solitairement", "sur", "ce", "buste", "placide", "parla",
                "ce", "seul", "mot", "comme", "si", "son", "âme", "en", "ce", "seul", "mot", "il", "la", "répandait", 
                "je", "ne", "proférâi", "donc", "rien", "de", "plus", "il", "n'agita", "donc", "pas", "de", "plume", 
                "jusqu'à", "ce", "que", "je", "fis", "à", "peine", "davantage", "que", "marmotter", "d'autres", 
                "amis", "déjà", "ont", "pris", "leur", "vol", "demain", "il", "me", "laissera", "comme", "mes", 
                "espérances", "déjà", "ont", "pris", "leur", "vol", "alors", "l'oiseau", "dit", "jamais", "plus"]
    assert tokenize(text) == expected, "Tokenizer failed on Le Corbeau"

def test_count_words_le_corbeau():
    text = ("Mais le Corbeau, perché solitairement sur ce buste placide, parla "
            "ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne "
            "proférâi donc rien de plus: il n'agita donc pas de plume--jusqu'à ce "
            "que je fis à peine davantage que marmotter «D'autres amis déjà ont "
            "pris leur vol--demain il me laissera comme mes Espérances déjà ont "
            "pris leur vol.» Alors l'oiseau dit: «Jamais plus.»")
    expected = {
        "mais": 1, "le": 2, "corbeau": 1, "perché": 1, "solitairement": 1, "sur": 1, "ce": 2, "buste": 1, 
        "placide": 1, "parla": 1, "seul": 2, "mot": 2, "comme": 2, "si": 1, "son": 1, "âme": 1, "en": 1, 
        "il": 2, "la": 1, "répandait": 1, "je": 2, "ne": 1, "proférâi": 1, "donc": 2, "rien": 1, "de": 2, 
        "plus": 1, "n'agita": 1, "pas": 1, "plume": 1, "jusqu'à": 1, "que": 1, "fis": 1, "à": 1, "peine": 1, 
        "davantage": 1, "marmotter": 1, "d'autres": 1, "amis": 1, "déjà": 2, "ont": 2, "pris": 2, "leur": 2, 
        "vol": 2, "demain": 1, "me": 1, "laissera": 1, "comme": 1, "mes": 1, "espérances": 1, "alors": 1, 
        "l'oiseau": 1, "dit": 1, "jamais": 1, "plus": 1
    }
    assert count_words(text) == expected, "Count_words failed on Le Corbeau"


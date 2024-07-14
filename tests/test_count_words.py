from text_processor import count_words

def test_count_words_le_corbeau():
    text = 'Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait.'
    expected = {
        'mais': 1, 'le': 1, 'corbeau': 1, 'perche': 1, 'solitairement': 1, 'sur': 1, 'ce': 3, 'buste': 1,
        'placide': 1, 'parla': 1, 'seul': 2, 'mot': 2, 'comme': 1, 'si': 1, 'son': 1, 'ame': 1,
        'en': 1, 'il': 1, 'la': 1, 'repandait': 1
    }
    result = count_words(text)
    assert result == expected, f"Failed to count words: {result}"

def test_count_words():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected = {
        'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1,
        'spoke': 1, 'only': 1, 'that': 2, 'one': 2, 'word': 2, 'as': 1, 'if': 1, 'his': 1, 'soul': 1,
        'in': 1, 'he': 1, 'did': 1, 'outpour': 1
    }
    result = count_words(text)
    assert result == expected, f"Failed to count words: {result}"




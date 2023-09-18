from translate import Translator
to_lang = 'zh'

try:
    with open ('./translator.txt', mode='r+') as translated:
        print(translated.read())
except FileNotFoundError as e:
    print("wrong file path")
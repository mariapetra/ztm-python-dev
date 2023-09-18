from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('./translator.txt', mode='r') as translated:
        text = translated.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print("wrong file path")




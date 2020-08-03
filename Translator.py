from translate import Translator

try:
    with open('transtest.txt', mode='r') as mfile:
        translang = Translator(to_lang="es")
        transtext = translang.translate(mfile.read())
    with open('transtest-spanish.txt', mode='w') as dfile:
        dfile.write(transtext)

except FileNotFoundError as e:
    print("No file exists")

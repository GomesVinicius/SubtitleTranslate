from googletrans import Translator
import time

translator = Translator(service_urls=['translate.googleapis.com'])

arch_dest = open('pt-br - example.txt', 'w', encoding='UTF-8')

with open('en - example.txt', 'r') as reader:
    text_array = reader.readlines(-1)

inicio = time.time()
for x in text_array:

    translation = translator.translate(
        text=x,
        dest='pt',
    )

    # print(translation.text)
    arch_dest.write(translation.text + '\n')

fim = time.time()
print(fim - inicio)

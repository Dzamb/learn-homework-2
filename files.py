"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
import re

def main():
    with open('referat.txt', 'r', encoding='utf-8') as ref_text:
        ref_content = ref_text.read()
        rep_content = ref_content.replace('.', '!')
        print(rep_content)
        word_len = len(re.findall(r'\w+', ref_content))
    with open('referat2.txt', 'w', encoding='utf-8') as text:
        text.write(rep_content)
    print(f'Количество слов в тексте: {word_len}')
    

if __name__ == "__main__":
    main()

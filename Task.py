import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def work(words):
    for word in words:
        w = morph.parse(word)[0]
        # for x in w.lexeme:
        #     print(x.word)
        print(w, w.tag, type(w), type(w.tag), sep='\n')


def main():
    # words = input().split()
    words = 'в большой дом'.split()
    work(words)


if __name__ == '__main__':
    main()  # Start
    # в большой дом

from daumdict.get_translation import translate


def main():
    import sys
    _, lang, word = sys.argv
    print(translate(lang, word))


if __name__ == '__main__':
    main()
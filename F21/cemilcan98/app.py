def toLowerCase(word):

    if(word[1] in ["en", "en-US", "en-IE", "en-Latn", "en-AU", "en-GB", "en-IE", "en-ZA"]):

        upperCaseWord = word[0].lower()
        return upperCaseWord

    # Checking for the special letters in Turkish and Azeri
    # The Azerbaijani Latin alphabet is based on the Turkish Latin alphabet.

    if(word[1] == "tr" or word[1] == "az"):

        upperCaseWord = word[0]

        upperCaseWord = upperCaseWord.replace(

            '\u011E', '\u011F')  # char is Ğ and ğ

        upperCaseWord = upperCaseWord.replace(

            '\u00C7', '\u00E7')  # char is Ç and ç

        upperCaseWord = upperCaseWord.replace(

            '\u00D6', '\u00F6')  # char is Ö and ö

        upperCaseWord = upperCaseWord.replace(

            '\u00D3', '\u00FC')  # char is Ó and ü

        upperCaseWord = upperCaseWord.replace(

            '\u015E', '\u015F')  # char is Ş and ş

        upperCaseWord = upperCaseWord.replace(

            '\u0049', '\u0131')  # char is I and ı

        upperCaseWord = upperCaseWord.lower()

        return upperCaseWord

    # Checking for the special cases in Irish

    if(word[1] == "ga" or word[1] == "ga-IE"):

        upperCaseWord = word[0]

        if(len(word[0]) > 1):
            first = word[0][0]
            second = word[0][1]
        else:
            first = word[0][0]
            second = ""

        first_letters = ['n', 't']
        second_letters = ['A', 'E', 'I', 'O', 'U', '\u00C1',
                          '\u00C9', '\u00CD', '\u00D3', '\u00D3']

        if (first in first_letters):

            if(second in second_letters):

                upperCaseWord = upperCaseWord.lower()
                upperCaseWord = upperCaseWord[:1] + "-" + upperCaseWord[1:]

                if(second == '\u00C1'):  # char is Á and á
                    upperCaseWord[2] = '\u00E1'

                if(second == '\u00C9'):  # char is É and é
                    upperCaseWord[2] = '\u00E9'

                if(second == '\u00CD'):  # char is Í and í
                    upperCaseWord[2] = '\u00ED'

                if(second == '\u00DA'):  # char is Ú and ú
                    upperCaseWord[2] = '\u00FA'

                if(second == '\u00D3'):  # char is Ó and ó
                    upperCaseWord = upperCaseWord[:2] + \
                        '\u00F3' + upperCaseWord[3:]

        else:

            upperCaseWord = upperCaseWord.lower()
        return upperCaseWord

    # Greek Cases

    if(word[1] == "el"):

        upperCaseWord = word[0]

        if(upperCaseWord[-1] == '\u03A3'):

            upperCaseWord = upperCaseWord[:-1] + '\u03C2'

        upperCaseWord = upperCaseWord.lower()
        return upperCaseWord

    if(word[1] in ["zh", "ja"]):

        upperCaseWord = word[0]
        return upperCaseWord

    if(word[1] in ["th"]):

        upperCaseWord = word[0]
        return upperCaseWord

    if(word[1] in ["zh-Hans"]):

        upperCaseWord = word[0]
        return upperCaseWord


def read_file(file_name):

    f = open(file_name, encoding="utf8")

    lines_text = []

    pieces_text = []

    for line in f:
        line = line.rstrip('\n')
        lines_text.append(line)
        pieces = line.split('\t')
        pieces_text.append(pieces)

    return pieces_text

# closing the file after reading


def close_file(file_name):
    f = open(file_name, encoding="utf8")
    f.close()


textFile = read_file('tests.tsv')

for iteration in textFile:
    if (iteration[2] != toLowerCase(iteration)):
        print("Failed test: ", iteration)


close_file('tests.tsv')

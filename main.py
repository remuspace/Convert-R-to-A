def get():
    cons_input = input()
    return cons_input


def get_list(input):
    input_list = input.replace(',', '')
    input_list = input_list.replace('.', '')
    input_list = input_list.split()
    return input_list


def get_big_words(words):
    big_words = []
    for i in range(len(words)):
        if words[i].isupper():
            big_words.append(words[i])
    return big_words


def check(big_words):
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    for word in big_words:
        for letter in word:
            if letter not in roman: return False

    return True


def convert(big_word):
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arab = [1, 5, 10, 50, 100, 500, 1000]
    letters = list(big_word)
    sum = 0
    cnt = 0
    while cnt < len(letters):
        look_next = True
        if cnt + 1 < len(letters):
            if letters[cnt] not in ['I', 'X', 'C']:
                index = roman.index(letters[cnt])
                cntoj = arab[index]
                sum += cntoj
            else:
                for x in range((len(roman) - 1) // 2):
                    if letters[cnt] == roman[2 * x] and look_next:  # IV
                        for y in range(len(roman)):
                            if y > 2 * x and letters[cnt + 1] == roman[y]:
                                cntoj = arab[y] - arab[2 * x]
                                sum += cntoj
                                cnt += 1
                                look_next = False
                                break
                        if not look_next: break

                        if look_next:  # II
                            sum += arab[2 * x]
                            break
        else:
            index = roman.index(letters[cnt])
            cntoj = arab[index]
            sum += cntoj

        cnt += 1

    return sum


def modify(input, words, big_words):
    words_tz = input.split()
    output_list = []
    for i in range(len(big_words)):
        arab_cntoj = str(convert(big_words[i]))

        for n in range(len(words)):
            if words[n] == big_words[i]:
                words_tz[n] = words_tz[n].replace(big_words[i], arab_cntoj)

        output_list = words_tz
    output = ' '.join(output_list)
    return output


sentence = get()
words_no_tz = get_list(sentence)
words_big = get_big_words(words_no_tz)

if check(words_big):
    print(modify(sentence, words_no_tz, words_big), end="")

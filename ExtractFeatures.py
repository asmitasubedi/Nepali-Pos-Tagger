
def get_features(tokens, index):
    word = tokens[index]
    pos = tokens[index + 1]
    if index == 0:
        prevword = ''
        prevpos = ''
        prevprevword = ''
        prevprevpos = ''
    elif index == 2:
        prevword = tokens[index - 2]
        prevpos = tokens[index - 1]
        prevprevword = ''
        prevprevpos = ''
    else:
        prevword = tokens[index - 2]
        prevpos = tokens[index-1]
        prevprevword = tokens[index-4]
        prevprevpos = tokens[index-3]

    if index == len(tokens) - 2:
        nextword = ''
        nextpos = ''
        nextnextword = ''
        nextnextpos = ''
    elif index == len(tokens) - 4:
        nextword = tokens[index + 2]
        nextpos = tokens[index + 3]
        nextnextword = ''
        nextnextpos = ''
    else:
        nextword= tokens[index + 2]
        nextpos = tokens[index+3]
        nextnextword = tokens[index+4]
        nextnextpos = tokens[index+5]

    features={'feature':{'word': word,'pos': pos,'next-word': nextword,'next-pos': nextpos,'next-next-word': nextnextword,
                         'next-next-pos': nextnextpos,'prev-word': prevword,'prev-pos': prevpos,'prev-prev-word': prevprevword,
                         'prev-prev-pos': prevprevpos}, 'pos': pos}

    # with open('data.json', 'a+', encoding="utf-8") as f:
    #     json.dump(features, f, ensure_ascii=False)

    # print(json.dumps(features, ensure_ascii=False))

    return {
            'word': word,
            'pos': pos,

            'next-word': nextword,
            'next-pos': nextpos,

            'next-next-word': nextnextword,
            'nextnextpos': nextnextpos,

            'prev-word': prevword,
            'prev-pos': prevpos,

            'prev-prev-word': prevprevword,
            'prev-prev-pos': prevprevpos,

    }

def get_wordFeatures(tokens, index):
    word = tokens[index]
    # pos = tokens[index + 1]

    if index == 0:
        prevword = ''
        prevprevword = ''
    elif index == 1:
        prevword = tokens[index - 1]
        prevprevword = ''
    else:
        prevword = tokens[index-1]
        prevprevword = tokens[index - 2]

    if index == len(tokens) - 1:
        nextword = ''
        nextnextword = ''

    elif index == len(tokens) - 2:
        nextword = tokens[index + 1]
        nextnextword = ''

    else:
        nextword= tokens[index + 1]
        nextnextword = tokens[index + 2]

    return {
            'word': word,
            # 'pos': '',

            'next-word': nextword,
            # 'next-pos': '',

            'next-next-word': nextnextword,
            # 'nextnextpos': '',

            'prev-word': prevword,
            # 'prev-pos': '',

            'prev-prev-word': prevprevword,
            # 'prev-prev-pos': '',
    }

def get_testfeatures(tokens, index):
    word = tokens[index]

    if index == 0:
        prevword = ''
        prevprevword = ''

    elif index == 2:
        prevword = tokens[index - 2]
        prevprevword = ''

    else:
        prevword = tokens[index - 2]
        prevprevword = tokens[index - 4]

    if index == len(tokens) - 2:
        nextword = ''
        nextnextword = ''

    elif index == len(tokens) - 4:
        nextword = tokens[index + 2]
        nextnextword = ''
    else:
        nextword= tokens[index + 2]
        nextnextword = tokens[index+4]

    return {
            'word': word,
            # 'pos': '',

            'next-word': nextword,
            # 'next-pos': '',

            'next-next-word': nextnextword,
            # 'nextnextpos': '',

            'prev-word': prevword,
            # 'prev-pos': '',

            'prev-prev-word': prevprevword,
            # 'prev-prev-pos': '',

    }

    # def get_features(tokens, index):
    #     word = tokens[index]
    #     pos = tokens[index + 1]
    #     if index == 0:
    #         prevword = ''
    #         prevpos = ''
    #         prevprevword = ''
    #         prevprevpos = ''
    #     elif index == 2:
    #         prevword = tokens[index - 2]
    #         prevpos = tokens[index - 1]
    #         prevprevword = ''
    #         prevprevpos = ''
    #     else:
    #         prevword = tokens[index - 2]
    #         prevpos = tokens[index-1]
    #         prevprevword = tokens[index-4]
    #         prevprevpos = tokens[index-3]
    #
    #     if index == len(tokens) - 2:
    #         nextword = ''
    #         nextpos = ''
    #         nextnextword = ''
    #         nextnextpos = ''
    #     elif index == len(tokens) - 4:
    #         nextword = tokens[index + 2]
    #         nextpos = tokens[index + 3]
    #         nextnextword = ''
    #         nextnextpos = ''
    #     else:
    #         nextword= tokens[index + 2]
    #         nextpos = tokens[index+3]
    #         nextnextword = tokens[index+4]
    #         nextnextpos = tokens[index+5]
    #
    #     features={'feature':{'word': word,'pos': pos,'next-word': nextword,'next-pos': nextpos,'next-next-word': nextnextword,
    #                          'next-next-pos': nextnextpos,'prev-word': prevword,'prev-pos': prevpos,'prev-prev-word': prevprevword,
    #                          'prev-prev-pos': prevprevpos}, 'pos': pos}
    #
    #     # with open('data.json', 'a+', encoding="utf-8") as f:
    #     #     json.dump(features, f, ensure_ascii=False)
    #
    #     # print(json.dumps(features, ensure_ascii=False))
    #
    #     return {
    #             'word': word,
    #             'pos': pos,
    #
    #             'next-word': nextword,
    #             'next-pos': nextpos,
    #
    #             'next-next-word': nextnextword,
    #             'nextnextpos': nextnextpos,
    #
    #             'prev-word': prevword,
    #             'prev-pos': prevpos,
    #
    #             'prev-prev-word': prevprevword,
    #             'prev-prev-pos': prevprevpos,
    #
    #     }
    # def get_feats(tokens, index):
    #     word = tokens[index]
    #     # pos = tokens[index + 1]
    #     if index == 0:
    #         prevword = ''
    #         # prevpos = ''
    #     else:
    #         # prevword = tokens[index - 2]
    #         prevword = tokens[index-1]
    #     if index == len(tokens) - 1:
    #         nextword = ''
    #         # nextpos = ''
    #     else:
    #         nextword= tokens[index + 1]
    #         # nextpos = tokens[index+3]
    #
    #     return {
    #             'word': word,
    #             'pos': '',
    #
    #             'next-word': nextword,
    #             'next-pos': '',
    #
    #             # 'next-next-word': nextnextword,
    #             # 'nextnextpos': nextnextpos,
    #
    #             'prev-word': prevword,
    #             'prev-pos': '',
    #
    #             # 'prev-prev-word': prevprevword,
    #             # 'prev-prev-pos': prevprevpos,
    # }
    #
    # def get_testfeatures(tokens, index):
    #     word = tokens[index]
    #     # pos = tokens[index + 1]
    #     if index == 0:
    #         prevword = ''
    #         # prevpos = ''
    #     else:
    #         prevword = tokens[index - 2]
    #         # prevword = tokens[index-1]
    #     if index == len(tokens) - 2:
    #         nextword = ''
    #         # nextpos = ''
    #     else:
    #         nextword= tokens[index + 2]
    #         # nextpos = tokens[index+3]
    #
    #     return {
    #             'word': word,
    #             'pos': '',
    #
    #             'next-word': nextword,
    #             'next-pos': '',
    #
    #             # 'next-next-word': nextnextword,
    #             # 'nextnextpos': nextnextpos,
    #
    #             'prev-word': prevword,
    #             'prev-pos': '',
    #
    #             # 'prev-prev-word': prevprevword,
    #             # 'prev-prev-pos': prevprevpos,
    #
    #     }
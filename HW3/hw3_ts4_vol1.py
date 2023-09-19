# sent = ["This is a sample sentence ",
# "Python programming is fun"
#
# def get_sorted_sent(sentence):
#     words = [word for sentence in sent for word in sentence.split()]
#     words = [word.strip(",") for word in words]
#     return sorted(set(str(words).split()))
# sorted_sent = get_sorted_sent(sent)
#
# print(sorted_sent)

# def unique_words(sentence):
#     return set(sentence.split())
# print(unique_words(sent))
import itertools
# sent = input("text:")
sent = ["This is a sample sentence ", "Python programming is fun"]

def get_sorted_sent(sent):
    # print(str(sent).strip(","))
    # tst
    # words = [word for sentence in sent for word in sentence.split()]
    # sent = ["This is a sample sentence", ["Python programming is fun"]]
    # fsent = list(itertools.chain.from_iterable(sent))
    words = list(itertools.chain.from_iterable(map(str.split, sent)))
    # words2 = [word.strip(",") for sentence in sent for word in sentence.split()]
    # print(words2)
    # print(words1)
    return sorted(set(words))
sorted_sent = get_sorted_sent(sent)
print(sorted_sent)
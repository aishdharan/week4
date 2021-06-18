import sys

"""
Notes/Questions:
- apply the suggestion to wrap the long text below
- do the results depend on whether the words are upper or lower?
- suggestion: use a simple sentence (like one added below) to test before using the 
full dataset; this is a powerful trick to help with debugging since you can
do a quick manual inspection to verify the results
- top 10: try slicing
"""


def main():
    # long strings may be wrapped inside parentheses;
    # see https://github.com/sci2pro/pl1c-solutions/blob/master/week2/problem2.py
    # text = "When Princess Mary came down, Prince Vasíli and his son were already in the drawing room, talking to the little princess and Mademoiselle Bourienne. When she entered with her heavy step, treading on her heels, the gentlemen and Mademoiselle Bourienne rose and the little princess, indicating her to the gentlemen, said: “Voilà Marie!” Princess Mary saw them all and saw them in detail. She saw Prince Vasíli’s face, serious for an instant at the sight of her, but immediately smiling again, and the little princess curiously noting the impression “Marie” produced on the visitors. And she saw Mademoiselle Bourienne, with her ribbon and pretty face, and her unusually animated look which was fixed on him, but him she could not see, she only saw something large, brilliant, and handsome moving toward her as she entered the room. Prince Vasíli approached first, and she kissed the bold forehead that bent over her hand and answered his question by saying that, on the contrary, she remembered him quite well. Then Anatole came up to her. She still could not see him. She only felt a soft hand taking hers firmly, and she touched with her lips a white forehead, over which was beautiful light-brown hair smelling of pomade. When she looked up at him she was struck by his beauty. Anatole stood with his right thumb under a button of his uniform, his chest expanded and his back drawn in, slightly swinging one foot, and, with his head a little bent, looked with beaming face at the princess without speaking and evidently not thinking about her at all. Anatole was not quick-witted, nor ready or eloquent in conversation, but he had the faculty, so invaluable in society, of composure and imperturbable self-possession. If a man lacking in self-confidence remains dumb on a first introduction and betrays a consciousness of the impropriety of such silence and an anxiety to find something to say, the effect is bad. But Anatole was dumb, swung his foot, and smilingly examined the princess’ hair. It was evident that he could be silent in this way for a very long time. “If anyone finds this silence inconvenient, let him talk, but I don’t want to,” he seemed to say. Besides this, in his behavior to women Anatole had a manner which particularly inspires in them curiosity, awe, and even love—a supercilious consciousness of his own superiority. It was as if he said to them: “I know you, I know you, but why should I bother about you? You’d be only too glad, of course.” Perhaps he did not really think this when he met women—even probably he did not, for in general he thought very little—but his looks and manner gave that impression. The princess felt this, and as if wishing to show him that she did not even dare expect to interest him, she turned to his father. The conversation was general and animated, thanks to Princess Lise’s voice and little downy lip that lifted over her white teeth. She met Prince Vasíli with that playful manner often employed by lively chatty people, and consisting in the assumption that between the person they so address and themselves there are some semi-private, long-established jokes and amusing reminiscences, though no such reminiscences really exist—just as none existed in this case. Prince Vasíli readily adopted her tone and the little princess also drew Anatole, whom she hardly knew, into these amusing recollections of things that had never occurred. Mademoiselle Bourienne also shared them and even Princess Mary felt herself pleasantly made to share in these merry reminiscences."
    text = "the enemy of my enemy is my friend"
    txt_split = text.split()
    txt_wordcount = dict()
    txt_set = set(txt_split)
    # todo: write a brief description of what this does
    # fixme: 'words' implies that each item from the set is a more than one word
    for words in txt_set:
        txt_count = txt_split.count(words)
        print(f"Occurrences of '{words}' is: {txt_count}")

    # todo: write a brief description of what this does
    for word in txt_split:
        txt_wordcount[word] = txt_wordcount.get(word, 0) + 1

    # todo: write a brief description of what this does
    txt_list = list()
    for wrd, count in txt_wordcount.items():
        txt_list.append((count, wrd))

    txt_list = sorted(txt_list, reverse=True)

    for wrd in txt_list:
        print(wrd)
    # I'm not getting how to sort the list in top 10 in descending order.
    return 0  # if os.EX_OK  fails; please avoid os.X_OK


if __name__ == '__main__':
    sys.exit(main())

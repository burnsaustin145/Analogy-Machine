from nltk.tokenize import sent_tokenize
class Parsing:

    def __init__(self, text=None):
        if text == None:
            self.text = ""
        else:
            self.text = text

    def sentece_tokenizer(self):
        tokenized = sent_tokenize(self.text)
        return tokenized

if __name__ == "__main__":

    sent = "This is my excellent test sentence; no one shall talk shit." \
           "heres what happens when I add one more sentence"
    parse = Parsing(sent)

    print(parse.sentece_tokenizer())

from collections import defaultdict

# TODO: implement n-gram


class BagOfWords:
    def __init__(self, sentences: list, ngram: int = 1):
        self.sentences = sentences
        self.ngram = ngram
        self.tokenized = [self.tokenize(sentence) for sentence in self.sentences]

    def tokenize(self, sentence):
        return sentence.split()

    def encode(self):

        # count total number of tokens
        token_count = defaultdict(int)
        for sentence in self.tokenized:
            for token in sentence:
                token_count[token] += 1

        # re-order so that most frequent is at the front, alphabetically
        temp = [(token, freq) for token, freq in token_count.items()]
        self.bag = sorted(temp, key=lambda x: (-x[1], x[0]))

        tokens, token_count = list(zip(*self.bag))
        self.vocab = {token: i for i, token in enumerate(tokens)}

        n = len(self.vocab)
        result = []
        for sentence in self.tokenized:
            token_count = defaultdict(int)
            for token in sentence:
                token_count[self.vocab[token]] += 1
            temp = [0] * n

            for key, value in token_count.items():
                temp[key] = value

            result.append(temp)

        return result

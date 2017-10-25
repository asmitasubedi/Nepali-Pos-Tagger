import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
loadModel = pickle.load(open("RESULT.pickle", "rb"))


def assignTag(testFeatures):
    output = loadModel.predict(testFeatures)
    # for x in range(0, len(output)):
    #     if output[x] =='NN':
    #         desc.append('Common Noun')
    #     elif output[x] == 'NP':
    #         desc.append('Proper Noun')
    #     elif output[x] == 'IKM':
    #         desc.append('Masculine genitive postposition')
    #     elif output[x] == 'II':
    #         desc.append('Postposition')
    #     elif output[x] == 'VN':
    #         desc.append('ne-participle verb::')
    #     elif output[x] == 'VN':
    #         desc.append('ne-participle verb::')
    #     elif output[x] == 'YF':
    #         desc.append('Sentence-final punctuation')
    #     else:
    #         desc.append('Others')
    # return desc
    return output

def get_wordFeatures(tokens, index):
    word = tokens[index]
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
            'next-word': nextword,
            'next-next-word': nextnextword,
            'prev-word': prevword,
            'prev-prev-word': prevprevword,
    }

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    testFeatures, token, tags, desc = [], [], [], []
    text = request.form['testSentence']
    i = len(text.split())
    splits = (text.split())
    for y in range(0, i):
        token.append(splits[y])
    for x in range(0, len(token)):
        testFeatures.append(get_wordFeatures(token, x))
    tags = assignTag(testFeatures)
    return render_template("predict.html", sen_pos = zip(token,tags))

if __name__ == '__main__':
    app.run(debug=True)
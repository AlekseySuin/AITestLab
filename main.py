from transformers import pipeline

class emotions():
    def __init__(self):
        pass

    def takeEmotion(string):
        model = "blanchefort/rubert-base-cased-sentiment"
        classifier = pipeline("sentiment-analysis", model)

        list = classifier(string)
        list = list[0]
        return list['label']


str_user = input("введите строку:")
str_to_print = emotions.takeEmotion(str_user)

print(str_to_print)

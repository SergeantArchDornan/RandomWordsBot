import markovify

def get_words():
    
    text = open('corpus/chekhov-8.txt', encoding='utf8').read()

    text_model = markovify.Text(text)
    
    return text_model.make_sentence()


        

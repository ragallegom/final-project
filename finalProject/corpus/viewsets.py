from curses.ascii import NL
from unittest import result
from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from .library.binary_expression_tree import BinaryExpressionTree

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
corpus_sum = ['plus','plu']
corpus_mul = ['mul']
corpus_minus = ['minus']
corpus_div = ['div']
corpus_eq = ['equal','eq']
custom_stop_words = ['is','to','the']

class corpusViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.corpusSerializer

    def list(self, request):
        queryset = None
        serializer = serializers.corpusSerializer

        return Response({"msg", "success"})

    def create(self, request):
        serializer = serializers.corpusSerializer(data=request.data)
        
        if serializer.is_valid():
 
            corpus_sum =['plus','plu','+']
            corpus_mul =['mul','*']
            corpus_minus =['minus']
            corpus_div =['div']
            corpus_eq =['equal','eq','=']
            custom_stop_words =['is','to','the','evaluate','follow',"equat","slope","intercept"]

            result = {}
            words_list = []
            stopwords_list = []
            lemma_list = []
            equations = []
            binary_exp_tree_list = []

            sentence_in_quote = sent_tokenize(request.data['corpus'])
            result['sentences'] = sentence_in_quote

            for sentence in sentence_in_quote:
                filtered_list = []

                sentence_in_words = word_tokenize(sentence)
                words_list.append(sentence_in_words)

                for word in sentence_in_words:
                    if word.casefold() not in stop_words:
                        filtered_list.append(word)

                stopwords_list.append(filtered_list)

                lemmatizer = WordNetLemmatizer()
                lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]
                lemma_list.append(lemmatized_words)
                
                check_eq = any(item in lemmatized_words for item in corpus_eq)
                equation = '('

                if check_eq :
                    for word in lemmatized_words:
                        if word.casefold() not in custom_stop_words :
                            print(word.casefold())
                            if word.casefold() in corpus_sum:
                                equation += '+'
                            elif word.casefold() in corpus_mul:
                                equation += '*'
                            elif word.casefold() in corpus_div:
                                equation += '/'
                            elif word.casefold() in corpus_minus:
                                equation += '-'
                            elif word.casefold() in corpus_eq:
                                equation += ')=('
                            else:
                                equation += word
                    equations.append(equation + ')')
            
            for eq in equations:
                tree_obj = BinaryExpressionTree('(' + eq + ')')
                binary_exp_tree_list.append(tree_obj.evaluate())

            result['words'] = words_list
            result['stopwords'] = stopwords_list
            result['lemmatization'] = lemma_list
            result['equations'] = equations
            result['binaryExpTree'] = binary_exp_tree_list
            
            print(result)

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

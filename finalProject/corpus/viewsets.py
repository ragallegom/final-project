from curses.ascii import NL
from unittest import result
from rest_framework.response import Response
from rest_framework import viewsets, status

from . import serializers
from .library.binary_expression_tree import BinaryExpressionTree

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from nltk_identify.models import Nltk

from word2number import w2n
import PyPDF2

stop_words = set(stopwords.words("english"))

object_addition = Nltk.objects.filter(corpus_type="addition")
object_multiplication = Nltk.objects.filter(corpus_type="multiplication")
object_subtraction = Nltk.objects.filter(corpus_type="subtraction")
object_equality = Nltk.objects.filter(corpus_type="equality")
object_division = Nltk.objects.filter(corpus_type="division")
object_stopwords = Nltk.objects.filter(corpus_type="stop_words")

corpus_sum = [obj.corpus for obj in object_addition]
corpus_mul = [obj.corpus for obj in object_multiplication]
corpus_minus = [obj.corpus for obj in object_subtraction]
corpus_div = [obj.corpus for obj in object_division]
corpus_eq = [obj.corpus for obj in object_equality]
custom_stop_words = [obj.corpus for obj in object_stopwords]

class corpusViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.corpusSerializer

    def list(self, request):
        queryset = None
        serializer = serializers.corpusSerializer

        return Response({"msg", "success"})

    def create(self, request):
        serializer = serializers.corpusSerializer(data=request.data)
        flag_file = False

        if request.FILES:
            file = request.FILES['file']
            pdfReader = PyPDF2.PdfFileReader(file) 
            pageObj = pdfReader.getPage(0) 
            corpus_file = pageObj.extractText()
            flag_file = True

        if serializer.is_valid() or flag_file:
            
            if flag_file:
                corpus = corpus_file
                corpus = corpus.replace('.', '. ')
            else:
                corpus = request.data['corpus']

            result = {}
            words_list = []
            stopwords_list = []
            lemma_list = []
            equations = []
            binary_exp_tree_list = []

            sentence_in_quote = sent_tokenize(corpus)
            result['sentences'] = sentence_in_quote

            flag_operating = True

            for sentence in sentence_in_quote:
                filtered_list = []

                sentence_in_words = word_tokenize(sentence)
                words_list.append(sentence_in_words)

                for word in sentence_in_words:
                    if word.casefold() not in custom_stop_words:
                        filtered_list.append(word)

                stopwords_list.append(filtered_list)

                lemmatizer = WordNetLemmatizer()
                lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]
                lemma_list.append(lemmatized_words)
                
                check_eq = any(item in lemmatized_words for item in corpus_eq)
                equation = '('

                if check_eq :
                    for word in lemmatized_words:
                        if (word.casefold() in corpus_sum):
                            if flag_operating:
                                flag_operating = False
                                equation += '+'
                        elif (word.casefold() in corpus_mul):
                            if flag_operating:
                                flag_operating = False
                                equation += '*'
                        elif (word.casefold() in corpus_div): 
                            if flag_operating:
                                flag_operating = False
                                equation += '/'
                        elif (word.casefold() in corpus_minus):
                            if flag_operating:
                                flag_operating = False
                                equation += '-'
                        elif (word.casefold() in corpus_eq):
                            if flag_operating:
                                flag_operating = False
                                equation += ')=('
                        else:
                            flag_operating = True
                            try:
                                word = w2n.word_to_num(word)
                                equation += str(word)
                            except:
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

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

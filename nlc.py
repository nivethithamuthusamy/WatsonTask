# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:50:41 2017

@author: Nivi
"""
import json
from watson_developer_cloud import NaturalLanguageClassifierV1

# get the input from user
input_text = input("Feeling? : ")

natural_language_classifier = NaturalLanguageClassifierV1(
    username='d714bbfb-efd2-4905-8291-8c837591e1f4',
    password='TcYBcX8MD2MH')

# to get the list of classifiers we have 
classifiers = natural_language_classifier.list()
# print(json.dumps(classifiers, indent=2))

# to get the status of our classifier
status = natural_language_classifier.status('90e7b4x199-nlc-37326')
# print(json.dumps(status, indent=2))

if status['status'] == 'Available':
    response = natural_language_classifier.classify('90e7b4x199-nlc-37326', input_text)
    # print(json.dumps(response, indent=2))
    print(response)
    value = json.loads(json.dumps(response))
    print('You are feeling : ', value["top_class"])
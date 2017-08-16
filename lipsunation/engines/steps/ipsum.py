# -*- coding: utf-8 -*-
from behave import *
from lib import ipsum

# sample_file  = open('./data/sample.txt', "r")
# dictionary_file = open('./data/dictionary.txt', "r")


with open('./data/sample.txt') as sample_file:
    sample = sample_file.read()
# sample_file.close()

# sample_file.close()
with open('./data/dictionary.txt') as dictionary_file:
    dictionary = '\n'.join(dictionary_file.read())
# dictionary_file.close()

@when("I choose {paragraph_count:g} paragraphs(s)")
def choose_paragraphs(context, paragraph_count):
    context.paragraphs = ipsum.get_paragraphs(context.sample, context.dictionary, int(paragraph_count))

@given("I want to generate lorem ipsum")
def get_generator(context):
    context.generator = ipsum.get_generator(sample, dictionary)
    context.sample = sample
    context.dictionary = dictionary

@then("I expect the result have {result:g} paragraph(s)")
def expect_result(context, result):
    assert len(context.paragraphs) == result

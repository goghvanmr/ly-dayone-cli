# -*- coding: utf-8 -*-

import plistlib
import os

QUESTION_DIR = 'questions/'
DEFAULT_ANSWER = ''
INVALID_ANSWER_SCORE = 0

def practice_zen():
    total_score = read_total_score_from('total.score')

    for root, dirs, files in os.walk(QUESTION_DIR):
        for f in files:
            file_path = root + f
            question_plist = plistlib.readPlist(file_path)
            question, bonus, penalty = read_question_info_from(question_plist)
            answer = get_answer_from(question)

            total_score += bonus_or_penalty(answer, penalty, bonus)

            print total_score

    write_total_score_into('total.score', total_score)

def get_answer_from(question):
    answer = DEFAULT_ANSWER
    return raw_input('%s (y/n)' % question)

def read_total_score_from(plist_file):
    return plistlib.readPlist(plist_file)['score']

def read_question_info_from(question_plist_file):
    question = question_plist_file['question']
    bonus = question_plist_file['bonus']
    penalty = question_plist_file['penalty']

    return question, bonus, penalty

def bonus_or_penalty(answer, penalty, bonus):
    if answer is 'y' or answer is DEFAULT_ANSWER:
        return bonus
    elif answer is 'n':
        return penalty
    else:
        return INVALID_ANSWER_SCORE

def write_total_score_into(plist_file, total_score):
    pl = plistlib.readPlist(plist_file)
    pl['score'] = total_score
    plistlib.writePlist(pl, 'total.score')

if __name__ == '__main__':
    practice_zen()
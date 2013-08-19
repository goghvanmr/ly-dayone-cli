# -*- coding: utf-8 -*-

import plistlib

def practice_zen():
    question_plist = plistlib.readPlist('test.question')

    question = question_plist['question']
    bonus = question_plist['bonus']
    penalty = question_plist['penalty']

    answer = raw_input('%s (y/n)' % question)

    score = plistlib.readPlist('total.score')['score']

    if answer is 'y' or answer is '':
        score += bonus
    elif answer is 'n':
        score += penalty
    else:
        print 'wrong input: %s' % answer

    print score

if __name__ == '__main__':
    practice_zen()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from carry_my_luggage.srv import SpeechToText, isMeaning

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# 音声認識の関数 (vosk)
from speech_and_NLP.src.tools.speech_to_text.speechToText import recognize_speech 
from speech_and_NLP.src.tools.speech_to_text.isMeaning import is_meaning
from speech_and_NLP.src.tools.text_to_speech.textToSpeech import textToSpeech

class Audio():
    def __init__(self):
        self.sub = rospy.Subscriber("/audio", String, self.callback)
        self.speechToTextSrv = rospy.Service("/speechToText", SpeechToText, self.calbkSTT)
        self.isMeaningSrv = rospy.Service("/isMeaning", isMeaning, self.calbkIsMeaning)

    def calbkIsMeaning(self, msg):
        return is_meaning(msg.text, msg.word_list, msg.path)

    def calbkSTT(self, msg):
        return recognize_speech(msg.print_partial, msg.use_break, msg.return_extract_person_name, msg.remove_space, msg.voskLogLevel, msg.path)
    
    def callback(self, msg):
        textToSpeech(msg.data, verbose=True)

if __name__ == '__main__':
    rospy.init_node("audio")
    audio = Audio()
    
    while not rospy.is_shutdown():
        rospy.Rate(10).sleep()
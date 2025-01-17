import pvporcupine
import struct
import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import time
import platform
import psutil
import random
import socket
import subprocess
import json
from word2number import w2n
import datetime






with open("access_key.txt", 'r') as file:
    
    ACCESS_KEY = file.read().strip()


""" 
porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[KEYWORD_PATH])
"""

"""
pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)
"""


engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')





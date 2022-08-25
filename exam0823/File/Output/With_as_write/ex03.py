# 디렉토리 만들기 import 해야함 모듈임
import os


if not os.path.isdir(): # 만드려는 디렉토리가 없으면 만들어라
    os.mkdir('e://temp/log')
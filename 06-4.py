# 1)
def chat(name1, name2):      #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 20살이야!" % name2)
chat("정수", "태희")
chat("환준", "세영")
# 2)
def chat(name1, name2, age):     #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
    print("%s: 안녕? 넌 몇 살이니" % name1)
    print("%s: 나? 나는 %d" % (name2, age) + "살이야!")
chat("정수", "태희", 20)
chat("환준", "세영", 19)
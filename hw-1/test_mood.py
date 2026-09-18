from mood import predict_message_mood


def test_mood_good():
    assert predict_message_mood("aaaaaa") == "отл"
    assert predict_message_mood("Чапаев и пустота", 0.1, 0.2) == "отл"
    assert predict_message_mood("AEUOOU") == "отл"


def test_mood_ok():
    assert predict_message_mood("Чапаев и пустота") == "норм"


def test_mood_bad():
    assert predict_message_mood("Чапаев и пустота", 0.7, 0.9) == "неуд"
    assert predict_message_mood("000") == "неуд"
    assert predict_message_mood("") == "неуд"
    assert predict_message_mood("我要去吃饺子") == "неуд"

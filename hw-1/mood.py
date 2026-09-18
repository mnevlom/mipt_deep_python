class SomeModel:
    def predict(self, message: str) -> float:
        message = message.lower()
        vowels = {
            "a",
            "e",
            "i",
            "o",
            "u",
            "а",
            "у",
            "о",
            "и",
            "ы",
            "э",
            "е",
            "ю",
            "ё",
            "я",
        }
        counter = 0
        for char in message:
            if char in vowels:
                counter += 1
        return counter / len(message) if len(message) > 0 else 0


def predict_message_mood(message: str, bad_thresh=0.3, good_thresh=0.8) -> str:
    model = SomeModel()
    score = model.predict(message)
    if score > good_thresh:
        return "отл"
    elif bad_thresh <= score <= good_thresh:
        return "норм"
    else:
        return "неуд"

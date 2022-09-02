
class Words:
    size_word = int
    word = str
    score = int
    _status = bool

    def __init__(self,word:str) -> None:
        self.word = word
        self.score = len(word)*2
        if "z" in word or "q" in word or "ñ" in word or "y" in word or "k" in word or "x" in word or "w" in word:
            self.score += 2
        self._status = False

    def _modify_score(self, new_score):
        self.score = new_score
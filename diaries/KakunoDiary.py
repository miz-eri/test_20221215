from diaries.AbstractDiary import AbstractDiary

class KakunoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-01"

    def get_summary(self):
        return """これでいいのかな？
        gitって難しい，，，！！"""

    def get_author(self):
        return "Kakuno"
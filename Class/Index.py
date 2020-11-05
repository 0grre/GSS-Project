class Index:

    def __init__(self, charset, lang, description, title):
        self.charset = charset
        self.lang = lang
        self.description = description
        self.title = title

    def get_index(self):
        return [self.charset, self.lang, self.description, self.title]

class Author:

    def __init__(self, name, mail, phone, avatar, link=None):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.avatar = avatar
        self.link = link

    def get_author(self):
        return [self.name, self.mail, self.phone, self.avatar, self.link]

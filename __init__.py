from mycroft import MycroftSkill, intent_file_handler


class CopyPasteCut(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cut.paste.copy.intent')
    def handle_cut_paste_copy(self, message):
        self.speak_dialog('cut.paste.copy')


def create_skill():
    return CopyPasteCut()


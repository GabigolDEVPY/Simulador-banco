from ..utils.bd_connect import BD_execute

class Notify():
    @staticmethod
    def create_notify(user_id, title_notify, subtitle_notify):
        dados = BD_execute.execute_comand("INSERT INTO user_notifications (user_id, title_notify, subtitle_notify) VALUES (%s, %s, %s)", user_id, title_notify, subtitle_notify)
        return

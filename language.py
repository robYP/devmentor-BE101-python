class Language():
    msg_key: str
    lang_code: str

    def __init__(self, lang_code):
        self.lang_code = lang_code
        self.msg = {
            "enus": {
                "signup": "signed up SUCCESSFULLY",
                "subscribe": "subscribed SUCCESSFULLY",
                "cancel": "cancelled SUCCESSFULLY",
                "ChineseNewYear": "Happy Chinese New Year"
            },
            "zhtw": {
                "signup": "註冊成功",
                "subscribe": "訂閱成功",
                "cancel": "取消成功",
                "ChineseNewYear": "新年快樂！"
            }
        }

    def get_msg(self, msg_key: str) -> str:
        return self.msg[self.lang_code][msg_key]

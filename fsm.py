from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def coffee_train(self, event):
        text = event.message.text
        return "學習手沖" in text

    def on_enter_player(self, event):
        reply = ("咖啡有很多學問的\n " +
                "請輸入關鍵字來學習相關知識\n\n " +
                "[咖啡豆]\n[手沖工具]\n[豆子熟度]\n")
        reply_token = event.reply_token
        send_text_message(reply_token, reply)

    def coffee_knowledge(self, event):
        text = event.message.text
        reply_token = event.reply_token

        basis = {"咖啡豆":"分為兩種，羅布斯塔與阿拉比卡", "手沖工具":"手沖壺、濾紙、濾杯、磨豆機",
                 "豆子熟度":"共有淺培、中培與深培",}
        for key in basis:
            if key in text:
                send_text_message(reply_token, basis[key])
        # return True
    
    def on_enter_master(self, event):
        reply_token = event.reply_token
        reply = "沒想到你有勇氣參加比賽，你在經歷多場比賽後變成大師了"
        send_text_message(reply_token, reply)

    def contest(self, event):
        text = event.message.text
        return "更多練習" in text

    def finish(self, event):
        text = event.message.text
        reply_token = event.reply_token
        
        reply = "學無止境，從頭來過吧!"
        send_text_message(reply_token, reply)
        return "退休" in text

    def on_enter_free(self, event):
        print("entering free")
        

    def on_enter_beginner(self, event):
        print("I'm entering beginner")
        reply_token = event.reply_token
        reply = '歡迎來到來到本店，是來當學徒還是客人?'
        send_text_message(reply_token, reply)

    def on_enter_customer(self, event):
        print("I'm entering customer")
        reply_token = event.reply_token
        reply = "請選要什麼咖啡, 不過目前只賣美式與拿鐵"
        send_text_message(reply_token, reply)

    def menu(self, event):
        text = event.message.text
        return "點餐" in text

    def leave(self, event):
        text = event.message.text
        return "離開" in text

    def select_coffee(self, event):
        text = event.message.text
        reply_token = event.reply_token

        basis = {"美式":"美式為100元",
                 "拿鐵":"拿鐵為120元",}
        for key in basis:
            if key in text:
                send_text_message(reply_token, basis[key])
    
    def on_exit_customer(self, event):
        print("Leaving shop")
        

    def turn_new_leaf(self, event):
        text = event.message.text
        reply_token = event.reply_token
        
        reply = "沒關係的，當客人也好"
        send_text_message(reply_token, reply)
        return "後悔" in text   
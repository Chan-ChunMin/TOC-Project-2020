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
        reply = "請選要什麼咖啡, 不過目前只賣美式"
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
        reply = '好的 100元'
        send_text_message(reply_token, reply)
    
    def on_exit_customer(self, event):
        print("Leaving shop")
        

    def turn_new_leaf(self, event):
        text = event.message.text
        reply_token = event.reply_token
        
        reply = "沒關係的，當客人也好"
        send_text_message(reply_token, reply)
        return "後悔" in text   



#     def fulfill_obligations(self, event):
#         text = event.message.text
#         return "入伍" in text

#     def not_passing_checkup(self, event):
#         text = event.message.text
#         return "體檢沒過" in text

#     def honorary_discharged(self, event):
#         text = event.message.text
#         return "退伍" in text

#     def with_a_separation(self, event):
#         text = event.message.text
#         return "驗退" in text

#     def some_basic_things(self, event):
#         text = event.message.text
#         reply_token = event.reply_token
#         # send_text_message(reply_token, text)
#         basis = {"稍息":"回復上一動", "立正":"站就要有站樣", "起床":"現在時間洞六洞洞，部隊起床",
#                  "精神答數":"雄壯、威武、嚴肅、剛直、安靜、堅強、確實、速捷、沉著、忍耐、機警、勇敢",
#                  "吃飯":"親愛精誠，服從", "站哨":"站住、口令、誰", "懇親":"醒醒吧你沒有女朋友",
#                  "新訓":"左線預備，右線預備，前線預備，開始射擊", "掃地":"每天除了掃地、掃地，還是掃地",
#                  "軍歌":"風雲起，山河動，黃埔建軍聲勢雄", "下餐廳":"起立，移位，靠板凳，取餐具，向左向右轉，起步走",
#                  "睡覺":"誰的拖鞋亂放ㄏㄚˋ，想放洞八是不是",}
#         for key in basis:
#             if key in text:
#                 send_text_message(reply_token, basis[key])
#         return True

#     def go_checkup_again(self, event):
#         text = event.message.text
#         return "複檢" in text

#     def exempt_from_duty(self, event):
#         text = event.message.text
#         return "免役" in text

#     def on_enter_conscription(self, event):
#         print("I'm entering conscription")
#         reply_token = event.reply_token

#         send_text_message(reply_token,"\
# 歡迎來到國軍online，恭喜您完成體檢！\n\
# 體檢報告即將出爐，沒意外的話您將在兩個月後入伍，敬請期待~~\n\
# 輸入特定關鍵字(如:入伍)便可以進行更多對話。")
        
#     def on_exit_conscription(self, event):
#         print("Leaving conscription")

#     def on_enter_soldier(self, event):
#         print("I'm entering soldier")
#         reply_token = event.reply_token
#         send_text_message(reply_token, "你各位啊，班長我知道你們都是不願役，給我皮繃緊點，四個月很快就過了")
        
#     def on_exit_soldier(self, event):
#         print("Leaving soldier")

#     def on_enter_exemption(self, event):
#         print("I'm entering exemption")
#         reply_token = event.reply_token
#         send_text_message(reply_token, "計画通り")

#     def on_exit_exemption(self, event):
#         print("Leaving exemption")

#     def on_enter_freedom(self, event):
#         print("I'm entering freedom")
#         reply_token = event.reply_token
#         send_text_message(reply_token, "幹！還好我退了")
#         # self.go_back()

#     def on_exit_freedom(self, event):
#         print("Leaving freedom")
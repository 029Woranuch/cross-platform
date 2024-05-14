from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Scr_bmi(Screen):
    def cal_bmi(self):
        weight = float(self.ids.txt_weight.text)
        height = float(self.ids.txt_height.text)
        height = height/100

        bmi = weight/(height*height)
        self.ids.lbl_bmi.txt ="1123123"
        if bmi > 35:
            self.ids.lbl_bmi.color="red"
            self.ids.img_bmi.source="5.PNG"
        elif bmi > 30:
            self.ids.lbl_bmi.color="orange"
            self.ids.img_bmi.source="4.PNG"
        elif bmi > 25:
            self.ids.lbl_bmi.color="yellow"
            self.ids.img_bmi.source="3.PNG"
        else:
            self.ids.lbl_bmi.color="green"
            self.ids.img_bmi.source="2.PNG"
                    
class Scr_knowledge(Screen):
    pass

class UI(ScreenManager):
    pass

class bmiApp(App):
    def build(self):
        return UI()

if __name__=='__main__':
    bmiApp().run()
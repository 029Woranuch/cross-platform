from kivymd.app import MDApp


class login(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Darkslateblue"
        return


login().run()
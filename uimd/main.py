from kivy.lang import Builder

from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return 

    def on_start(self):
        for style in theme_font_styles:
            if style != "Icon":
                for role in theme_font_styles[style]:
                    font_size = int(theme_font_styles[style][role]["font-size"])
                    self.root.ids.rv.data.append(
                        {
                            "viewclass": "MDLabel",
                            "text": f"{style} {role} {font_size} sp",
                            "adaptive_height": "True",
                            "font_style": style,
                            "role": role,
                        }
                    )


Example().run()
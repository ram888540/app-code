from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class Demo(MDApp):

    def build(self):
        # defining screen
        screen = Screen()

        # defining 1st label
        l = MDLabel(text="Wel!",
                    theme_text_color="Custom", pos_hint={'center_x':0.5,
                                                         'center_y':0.9},
                    text_color='red',
                    font_style='H4')

        l2 = MDLabel(text="co!",
                    theme_text_color="Custom", pos_hint={'center_x': 0.5,
                                                         'center_y': 0.5},
                    text_color='red',
                    font_style='H4')

        l3 = MDLabel(text="me!",
                    theme_text_color="Custom", pos_hint={'center_x': 0.5,
                                                         'center_y': 0.10},
                    text_color='red',
                    font_style='H4')


        # defining 2nd label
        l4 = MDLabel(text="TO medisys", pos_hint={'center_x': 0.86,
                                                'center_y': 0.9},
                     theme_text_color="Custom",
                     text_color=(0.5, 0, 0.5, 1),
                     font_style='H2')

        # defining 3rd label
        l5 = MDLabel(text="Edutech", pos_hint={'center_x': 0.91,
                                                'center_y': 0.10},
                     text_color='green',
                     font_style='H4')

        btn = Button(text="Push Me !",
                     font_size="16sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(10, 0),
                     size_hint=(.1, .1),
                     pos_hint={'center_x': 0.45,
                               'center_y': 0.5})
        l6 = MDLabel(text="R!",
                    theme_text_color="Custom", pos_hint={'center_x': 1.45,
                                                         'center_y': 0.9},
                    text_color='red',
                    font_style='H4')

        l7 = MDLabel(text="s!",
                     theme_text_color="Custom", pos_hint={'center_x': 1.45,
                                                          'center_y': 0.5},
                     text_color='red',
                     font_style='H4')

        l8 = MDLabel(text="p!",
                     theme_text_color="Custom", pos_hint={'center_x': 1.45,
                                                          'center_y': 0.1},
                     text_color='red',
                     font_style='H4')

        screen.add_widget(l)

        screen.add_widget(l2)

        screen.add_widget(l3)
        screen.add_widget(l4)
        screen.add_widget(l5)
        screen.add_widget(l6)
        screen.add_widget(l7)
        screen.add_widget(l8)
        screen.add_widget(btn)
        return screen


if __name__ == "__main__":
    Demo().run()

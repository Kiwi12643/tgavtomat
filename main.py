from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.metrics import dp

Window.size = (420, 740)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(15)
        
        # Заголовок
        title = Label(
            text='TG BlockFlow',
            font_size=28,
            bold=True,
            color=(0.1, 0.9, 0.4, 1),
            size_hint_y=None,
            height=dp(60)
        )
        self.add_widget(title)
        
        # Подзаголовок
        sub = Label(
            text='Меню готово\nФункционал скоро',
            color=(0.6, 0.6, 0.6, 1),
            size_hint_y=None,
            height=dp(60)
        )
        self.add_widget(sub)
        
        # Кнопки меню (заглушки)
        buttons = [
            ('📱 Аккаунты', self.dummy),
            ('📋 Блоки', self.dummy),
            ('▶ Запустить', self.dummy),
            ('📂 Схемы', self.dummy),
            ('⚙ Настройки', self.dummy),
        ]
        
        for text, func in buttons:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=dp(55),
                font_size=18,
                background_color=(0.12, 0.13, 0.2, 1)
            )
            btn.bind(on_press=func)
            self.add_widget(btn)
        
        # Место для лога
        self.log = Label(
            text='Готов к работе\n',
            color=(0.4, 0.8, 0.4, 1),
            size_hint_y=None,
            height=dp(100),
            font_size=12
        )
        self.add_widget(self.log)
    
    def dummy(self, instance):
        self.log.text += f'Нажато: {instance.text}\n'

class BlockFlowApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    BlockFlowApp().run()

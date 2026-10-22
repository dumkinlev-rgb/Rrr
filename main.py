import random
from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        # Создаем кнопку, которая займет весь экран
        self.btn = Button(
            text="Нажми на меня!",
            font_size='24sp',
            background_color=(0.2, 0.6, 1, 1)  # Красивый синий цвет
        )
        # Привязываем нажатие кнопки к нашей функции
        self.btn.bind(on_press=self.change_text)
        return self.btn

    def change_text(self, instance):
        # Список фраз, которые будут меняться при клике
        phrases = [
            "Привет, мир! 🌍",
            "Всё отлично работает! 🚀",
            "Ты супер! ⭐",
            "Код успешно запущен! 🎉",
            "Python + Kivy = ❤️"
        ]
        # Выбираем случайную фразу и меняем текст на кнопке
        self.btn.text = random.choice(phrases)

if __name__ == "__main__":
    SimpleApp().run()
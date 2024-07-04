from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import random

class TestApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=[10])
        self.image = Image(source='clasic.jpeg', allow_stretch=True)
        self.layout.add_widget(self.image)
        self.question_label = Label(text='', font_size=24)
        self.layout.add_widget(self.question_label)
        self.answer_layout = BoxLayout(spacing=10)
        self.button1 = Button(text='')
        self.button2 = Button(text='')
        self.button3 = Button(text='')
        self.answer_layout.add_widget(self.button1)
        self.answer_layout.add_widget(self.button2)
        self.answer_layout.add_widget(self.button3)
        self.layout.add_widget(self.answer_layout)
        self.result_label = Label(text='', font_size=24)
        self.layout.add_widget(self.result_label)
        self.questions = [
            {'question': 'Даты жизни Прокофьева', 'answers': ['1900-1955', '1891-1953', '1881-1950'], 'correct': 1, 'image': 'prokofiev.jpg'},
            {'question': 'Название первой симфонии Прокофьева', 'answers': ['Классическая', 'Романтическая', 'Юношеская'], 'correct': 0, 'image': 'clasic.jpeg'},
            {'question': 'Жанр произведения Шостаковича "Золотой век"', 'answers': ['Опера', 'Балет', 'Оперетта'], 'correct': 1, 'image': 'Goldenes.jpg'},
            {'question': 'Хобби Шостаковича', 'answers': ['Шахматы', 'Футбол', 'Чтение'], 'correct': 0, 'image': 'Hobbi.jpg'},
            {'question': 'Был ли Хачатурян дирижером', 'answers': ['Да', 'Нет', 'Иногда'], 'correct': 0, 'image': 'Dirijor.jpg'},
            {'question': 'Автор оперы "Борис Годунов"','answers': ['Мусоргский', 'Римский-Корсаков', 'Чайковский'], 'correct': 0, 'image': 'Godunov.jpg'},
            {'question': 'Название знаменитого балета Чайковского','answers': ['Лебединое Озеро', 'Спящая Красавица', 'Щелкунчик'], 'correct': 0, 'image': 'Lebedin ozero.jpg'},
            {'question': 'Композитор, написавший музыку к фильму "Летят Журавли"','answers': ['Шостакович', 'Хачатурян', 'Мясковский'], 'correct': 1, 'image': 'Letat-Juravli.jpg'},
            {'question': 'Автор цикла песен "Веснянка"','answers': ['Рахманинов', 'Мусоргский', 'Римский-Корсаков'], 'correct': 0, 'image': 'vesnyanka.jpg'},
            {'question': 'Название оркестрового сочинения Римского-Корсакова','answers': ['Шехеразада', 'Испанское Каприччио', 'Русская Пасхальная Овертюра'],'correct': 0, 'image': '12122511.jpg'}
        ]
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.show_question()
        return self.layout

    def show_question(self):
        question = self.questions[self.current_question]
        self.image.source = question['image']
        self.question_label.text = question['question']
        random_answers = question['answers'].copy()
        random.shuffle(random_answers)
        self.button1.text = random_answers[0]
        self.button2.text = random_answers[1]
        self.button3.text = random_answers[2]
        self.result_label.text = ''

    def on_button_press(self, instance):
        question = self.questions[self.current_question]
        correct_answer = question['answers'][question['correct']]
        if instance.text == correct_answer:
            self.result_label.text = 'Correct!'
            self.score += 1
        else:
            self.result_label.text = 'Incorrect. Correct answer is ' + correct_answer
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.result_label.text = 'Quiz finished! Your score is ' + str(self.score) + '/' + str(len(self.questions))

    def on_start(self):
        self.button1.bind(on_press=self.on_button_press)
        self.button2.bind(on_press=self.on_button_press)
        self.button3.bind(on_press=self.on_button_press)

if __name__ == '__main__':
    TestApp().run()
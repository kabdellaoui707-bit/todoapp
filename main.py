from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from plyer import notification
from datetime import datetime, timedelta
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.uix.image import Image # Assurez-vous d'importer Image

# Définition du TaskCard en Python (inchangé)
class TaskCard(BoxLayout):
    task_title = StringProperty('')
    task_time = StringProperty('')
    task_duration = StringProperty('')
    task_notes = StringProperty('')
    
    def init(self, **kwargs):
        super().init(**kwargs)
        self.size_hint_y = None
        self.height = "70dp" 

KV = """
#:import dp kivy.metrics.dp

# Définition de la carte de tâche personnalisée (inchangé)
<TaskCard>:
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(5)
    size_hint_y: None
    height: dp(70)
    
    canvas.before:
        Color:
            rgba: 1, 0.9, 0.95, 1 # Arrière-plan blanc cassé/rose très clair
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(15), dp(15), dp(15), dp(15)]
        
        Color:
            rgba: 1, 0.4, 0.7, 1
        RoundedRectangle:
            pos: self.right - dp(10), self.y
            size: dp(10), self.height
            radius: [0, dp(15), dp(15), 0]
            
    BoxLayout:
        orientation: 'horizontal'
        
        MDLabel:
            text: root.task_title
            font_style: 'H6'
            theme_text_color: 'Custom'
            text_color: 0.1, 0.1, 0.1, 1 
            size_hint_x: 0.7
            
        BoxLayout:
            orientation: 'horizontal'
            size_hint_x: 0.3
            spacing: dp(10)
            
            MDLabel:
                text: root.task_time
                font_style: 'Caption'
                halign: 'right'
                theme_text_color: 'Custom'
                text_color: 0.4, 0.4, 0.4, 1 
                
            MDLabel:
                text: root.task_duration + ' min'
                font_style: 'Caption'
                halign: 'right'
                theme_text_color: 'Custom'
                text_color: 0.4, 0.4, 0.4, 1 


ScreenManager:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: "first"

    FloatLayout:
        # NOUVEAU: Couleur d'arrière-plan féminine
        canvas.before:
            Color:
                rgba: 0.98, 0.90, 0.95, 1  # Rose clair/Lavande
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            orientation: "vertical"
            spacing: dp(35) # Augmentation de l'espacement pour mieux séparer les éléments
            padding: dp(30)
            size_hint: 0.9, 0.8 # Augmentation de la hauteur
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDLabel:
                text: "What’s your plan for today?"
                font_style: "H4"
                halign: "center"
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: None
                height: self.texture_size[1] # Hauteur minimale

            # NOUVEAU: Image book.jpg positionnée entre le titre et le bouton
            Image:
                source: "book.jpg" # Changement à book.jpg
                size_hint_y: 0.7 # Prend la majorité de l'espace vertical disponible
                allow_stretch: True
                keep_ratio: True
                pos_hint: {"center_x": 0.5}

            Button:
                text: "Next"
                size_hint: None, None
                size: dp(160), dp(55) # Bouton plus grand
                pos_hint: {"center_x": 0.5}
                background_normal: ""
                background_color: 1, 0.4, 0.7, 1 # Rose plus foncé
                font_size: "18sp"
                on_release:
                    app.root.current = "second"
                    
                    
<SecondScreen>:
    name: "second"

    FloatLayout:
        # NOUVEAU: Même couleur d'arrière-plan pour la cohérence
        canvas.before:
            Color:
                rgba: 0.98, 0.90, 0.95, 1  # Rose clair/Lavande
            Rectangle:
                pos: self.pos
                size: self.size
                
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            size_hint: 1, 1

            BoxLayout:
                id: task_list
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: dp(10)

        # Bouton '+' flottant (inchangé)
        Button:
            text: "+"
            background_normal: ""
            background_color: 1, 0.4, 0.7, 1 
            color: 1, 1, 1, 1
            font_size: "30sp"
            size_hint: None, None
            size: dp(60), dp(60)
            pos_hint: {"right": 0.95, "bottom": 0.05}
            canvas.before:
                Color:
                    rgba: self.background_color
                Ellipse:
                    pos: self.pos
                    size: self.size
            on_release: app.open_add_task_popup()
"""

# Le reste du code Python (classes FirstScreen, SecondScreen, ToDoApp, save_task, etc.)
# reste EXACTEMENT le même que dans la réponse précédente.
# Assurez-vous de coller la section KV ci-dessus dans votre fichier Python.

# ... (le code Python des classes et fonctions ici) ...

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ToDoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light" 
        return Builder.load_string(KV)

    def open_add_task_popup(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        self.title_input = TextInput(hint_text="Task title (e.g., Morning azkar)", multiline=False, size_hint_y=None, height=40)
        self.notes_input = TextInput(hint_text="Notes (optional)", multiline=True, size_hint_y=None, height=60)
        self.time_input = TextInput(hint_text="Start time (HH:MM) e.g., 06:00", multiline=False, size_hint_y=None, height=40)
        self.duration_input = TextInput(hint_text="Duration (minutes) e.g., 15", multiline=False, size_hint_y=None, height=40)
        save_button = Button(text="Save Task", size_hint_y=None, height=40, background_normal="", background_color=(1, 0.4, 0.7, 1))
        save_button.bind(on_release=self.save_task_from_popup)
        layout.add_widget(self.title_input)
        layout.add_widget(self.notes_input)
        layout.add_widget(self.time_input)
        layout.add_widget(self.duration_input)
        layout.add_widget(save_button)
        self.popup = Popup(title="Add Task", content=layout, size_hint=(0.85, 0.65))
        self.popup.open()

    def save_task_from_popup(self, instance):
        title = self.title_input.text.strip()
        notes = self.notes_input.text.strip()
        time_str = self.time_input.text.strip()
        duration_str = self.duration_input.text.strip()
        self.popup.dismiss()
        self.save_task(title, notes, time_str, duration_str)

    def save_task(self, title, notes, time_str, duration_str):
        if not title or not time_str or not duration_str.isdigit():
            return

        new_task_card = TaskCard(
            task_title=title,
            task_time=time_str,
            task_duration=duration_str,
            task_notes=notes
        )
        
        self.root.get_screen("second").ids.task_list.add_widget(new_task_card)
        try:
            today = datetime.now().date()
            start_datetime_str = f"{today} {time_str}"
            start_time = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")
            
            duration = int(duration_str)
            end_time = start_time + timedelta(minutes=duration)

            now = datetime.now()
            start_delay = (start_time - now).total_seconds()
            end_delay = (end_time - now).total_seconds()

            if start_delay > 0:
                Clock.schedule_once(lambda dt: self.send_notification(f"⏰ Task Started: {title}"), start_delay)
            if end_delay > 0:
                Clock.schedule_once(lambda dt: self.send_notification(f"✅ Task Finished: {title}"), end_delay)

        except Exception as e:
            print("Error parsing time or scheduling:", e)

    def send_notification(self, message):
        notification.notify(
            title="ToDo Reminder",
            message=message,
            timeout=5
        )

if __name__ == '__main__':
    ToDoApp().run()
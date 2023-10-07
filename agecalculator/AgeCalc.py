from datetime import datetime
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



class AgeCalculator(App):
    def getAge(self,event):
        try:
            today=datetime.today().year
            dob=self.date.text
            age=int(today)-int(dob)
            self.ageRequest.text="You are "+str(int(age))+" years old!"
        except ValueError:
            self.ageRequest.text = "Invalid input. Please enter a valid year."
            self.date.text = ""  # Clear the input field

    def build(self):
        self.window=GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        # self.window.add_widget(Image(source("burhan_dp.jpeg")))
        self.ageRequest=Label(
            text="Enter your date of birth...",
            font_size=50,
            color="#FFFFFF",
            bold=True
        )
        self.window.add_widget(self.ageRequest)
        self.date=TextInput(
            multiline=False,
            padding_y=(30,30),
            size_hint=(1,0.7),
            font_size=30
        )
        self.window.add_widget(self.date)
        self.button=Button(
            text="calculate Age",
            size_hint=(0.5,0.5),
            bold=True,
            font_size=30            
        )
        self.button.bind(on_press=self.getAge)
        self.window.add_widget(self.button)
        return self.window

if __name__ =="__main__":
    AgeCalculator().run()

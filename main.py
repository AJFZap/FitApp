from kivy.core.window import Window
from kivy.clock import Clock
from random import randint
from plyer import notification
from kivymd.toast import toast
from libs.uix.root import Root
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
import re

class ItemConfirm(OneLineAvatarIconListItem):
    """
    Checks that are to the left of the MDDialog that serves as the routine form.
    """
    divider = None

    def set_icon(self, instance_check):
        """
        When one is checked it calls the ApplyRoutine function that schedules the selected routine.
        """
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False
            else:
                FitApp.ApplyRoutine(self, check_list.index(instance_check))
                check.disabled = True

class FitApp(MDApp):
    from motivation import phrases
    
    dialog = None

    exercises = {"pushups": 0, "abs": 0, "squats": 0, "pullups": 0, "bridges": 0, "handstand": 0}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Fit App"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        # Don't change self.root to self.some_other_name
        # refer https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App.root
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        self.icon = "images/icon.png"
        self.root = Root()
        self.root.set_current("SplashScreen")

    def RoutineForm(self):
        """
        Creates the Routine Form from a Dialog.
        """
        if not self.dialog:
            self.dialog = MDDialog(title= "Select a Routine",
                                   type= "confirmation",
                                   auto_dismiss= False,
                                   items=[
                                       ItemConfirm(text= "New Blood"),
                                       ItemConfirm(text= "Good Behavior"),
                                       ItemConfirm(text= "Veterano"),
                                       ItemConfirm(text= "Solitary Confinement"),
                                       ItemConfirm(text= "Supermax"),
                                       ItemConfirm(text= "None"),
                                   ],
                                   buttons=[
                                       MDFlatButton(
                                            text="Close",
                                            theme_text_color="Custom",
                                            text_color= self.theme_cls.primary_color,
                                            on_press= self.CloseDialog,
                                       ),],)
        self.dialog.open()

    def CloseDialog(self, obj):
        """
        Used to close the Dialog popup when the button called "Close" is clicked.
        """
        self.dialog.dismiss()
    
    def ProgressButton(self):
        """
        TODO: Progress should give a screen where you check the exercises that you have done and give you a visual percentage of the completion.
        """
        # get_screen('main').ids.bottom_nav.textSize)
        print(App.get_running_app().root.get_screen('main').ids)
        toast("Not implemented yet,sorry!")

    def ApplyRoutine(self, obj):
        """
        It applies the selected routine to sends local push notifications to the user when required.
        """
        if obj == 0:
            toast("New Blood selected, you 'll be notified each Monday and Friday!")
            
            notification.notify(
                app_icon= "images/icon.png",
                title= "Time to Exercise!",
                message= "Notifications Just like this!",

                timeout= 10
            )

        elif obj == 1:
            toast("Good Behavior selected, you 'll be notified each Monday, Wednesday and Friday!")

            notification.notify(
                app_icon= "images/icon.png",
                title= "Time to Exercise!",
                message= "Notifications Just like this!",

                timeout= 10
            )

        elif obj == 2:
            toast("Veterano selected, you 'll be notified every day except Sundays!")

            notification.notify(
                app_icon= "images/icon.png",
                title= "Time to Exercise!",
                message= "Notifications Just like this!",

                timeout= 10
            )

        elif obj == 3:
            toast("Solitary Confinement selected, you 'll be notified every day except Sundays!")

            notification.notify(
                app_icon= "images/icon.png",
                title= "Time to Exercise!",
                message= "Notifications Just like this!",

                timeout= 10
            )

        elif obj == 4:
            toast("Supermax, selected, you 'll be notified every day except Sundays!")

            notification.notify(
                app_icon= "images/icon.png",
                title= "Time to Exercise!",
                message= "Notifications Just like this!",

                timeout= 10
            )

        else:
            toast("All appointed schedules have been erased!")

    def MotivQuote(self):
        """
        Returns a random motivational quote from the list.
        """
        toast(self.phrases[randint(0, len(self.phrases)-1)])

    def ExerciseTasks(self, buttonObj):
        """
        When the MDCards with the selected exercise is clicked it creates the exercise buttons with the required information for them to be usable.
        """
        # Amount of levels per exercise.
        names = ["Basic Concepts","Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", "Level 10"]
        
        # Names for each exercise in the big six.
        absName = ["Leg Raises","Knee Tucks", "Flat Knee Raises", "Flat Bent Leg Raises", "Flat Frog Raises", "Flat Straight Leg Raises", "Hanging Knee Raises", "Hanging Bent Leg Raises", "Hanging Frog Raises", "Partial Straight Leg Raises", "Hanging Straight Leg Raises"]
        pushName = ["Pushups","Wall Pushups", "Incline Pushups", "Kneeling Pushups", "Half Pushups", "Full Pushups", "Close Pushups", "Uneven Pushups", "Half One-Arm Pushups", "Lever Pushups", "One-Arm Pushups"]
        pullName = ["Pull Ups", "Vertical Pulls", "Horizontal Pulls", "Jackknife Pulls", "Half Pullups", "Full Pullups", "Close Pullups", "Uneven Pullups", "Half One-Arm Pullups", "Assisted One-Arm Pullups", "One-Arm Pullups"]
        squatName = ["Squats", "Shoulderstand Squats", "Jackknife Squats", "Supported Squats", "Half Squats", "Full Squats", "Close Squats", "Uneven Squats", "Half One-Leg Squats", "Assisted One-Leg Squats", "One-Leg Squats"]
        handName = ["Handstand", "Wall Headstands", "Crow Stands", "Wall Handstands", "Half Handstand Pushups", "Handstand Pushups", "Close Handstand Pushups", "Uneven Handstand Pushups", "Half One-Arm Handstand Pushups", "Lever Handstand Pushups", "One-Arm Handstand Pushups"]
        bridgeName = ["Bridges","Short Bridges", "Straight Bridges", "Angled Bridges", "Head Bridges", "Half Bridges", "Full Bridges", "Wall Walking Bridges 'D'", "Wall Walking Bridges 'U'", "Closing Bridges", "Stand-To-Stand Bridges"]

        if buttonObj == "abs":
            self.root.set_current("abs")
            
            if self.exercises["abs"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {absName[names.index(name)]}",
                                        size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                        on_press= self.ButtonBind,
                                        )
                    self.root.get_screen('abs').ids.abs_container.add_widget(button)
                self.exercises["abs"] = 1
            
        
        elif buttonObj == "pushups":
            self.root.set_current('pushup')
            
            if self.exercises["pushups"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {pushName[names.index(name)]}",
                                                size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                                on_press= self.ButtonBind,
                                                )
                    self.root.get_screen('pushup').ids.pushup_container.add_widget(button)
                self.exercises["pushups"] = 1
        
        elif buttonObj == "pullups":
            self.root.set_current("pullups")

            if self.exercises["pullups"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {pullName[names.index(name)]}",
                                                size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                                on_press= self.ButtonBind,
                                                )
                    self.root.get_screen('pullups').ids.pullup_container.add_widget(button)
                self.exercises["pullups"] = 1
        
        elif buttonObj == "squats":
            self.root.set_current("squats")
            
            if self.exercises["squats"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {squatName[names.index(name)]}",
                                                size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                                on_press= self.ButtonBind,
                                                )
                    self.root.get_screen('squats').ids.squats_container.add_widget(button)
                self.exercises["squats"] = 1

        elif buttonObj == "bridges":
            self.root.set_current("bridges")
            
            if self.exercises["bridges"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {bridgeName[names.index(name)]}",
                                                size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                                on_press= self.ButtonBind,
                                                )
                    self.root.get_screen('bridges').ids.bridges_container.add_widget(button)
                self.exercises["bridges"] = 1
        
        elif buttonObj == "handstand":
            self.root.set_current("handstand")
            
            if self.exercises["handstand"] == 0:
                for name in names:
                    button = MDFlatButton(text= f"{names[names.index(name)]}:\n {handName[names.index(name)]}",
                                                size_hint= (.8,1), md_bg_color= '#673AB7', line_color= '#673AB7',
                                                on_press= self.ButtonBind,
                                                )
                    self.root.get_screen('handstand').ids.handstand_container.add_widget(button)
                self.exercises["handstand"] = 1
    
    def on_start(self):
        """
        Whe the app runs it transitions from the loading screen to the main screen.
        """
        # Splash Screen timers for both the Logo and the GIF
        Clock.schedule_once(self.ChangeMain, 10)

    def ButtonBind(self, buttonObj):
        """
        Gives the exercise buttons the trigger to change screen to the required one.
        """
        exerciseNameStart = re.findall('\n (.*)', buttonObj.text)[0]
        self.root.set_current(exerciseNameStart)
        self.root.get_screen(exerciseNameStart).ids.exercise.title = exerciseNameStart
    
    def ChangeMain(self, DT):
        """
        Changes the Screen to the main one.
        """
        self.root.set_current("main")

if __name__ == "__main__":
    FitApp().run()

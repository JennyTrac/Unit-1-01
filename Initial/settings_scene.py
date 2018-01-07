# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import time

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.CENTRE_OF_SCREEN = self.size / 2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/space_background.JPG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        # page title
        settings_label_position = self.CENTRE_OF_SCREEN
        settings_label_position.y = self.size.y - 100
        self.settings_label = LabelNode(text = "Settings",
                                            font = ('ChalkboardSE-Light', 100),
                                            parent = self,
                                            position = settings_label_position)
        #sound
        sound_label_position = self.CENTRE_OF_SCREEN
        sound_label_position.x = self.size.x - 850
        sound_label_position.y = self.size.y - 270
        self.sound_label = LabelNode(text = "Sound",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = sound_label_position)
        sound_slider_position = self.CENTRE_OF_SCREEN
        sound_slider_position.x = self.size.x - 650
        sound_slider_position.y = self.size.y - 260
        self.sound_slider = SpriteNode('./assets/sprites/yes_no_slider.PNG',
                                  position = sound_slider_position,
                                  parent = self,
                                  scale = 0.2,
                                  alpha = 0.7)
        self.sound_slider_cursor_position = self.CENTRE_OF_SCREEN
        self.sound_slider_cursor_position.x = self.size.x - 690
        self.sound_slider_cursor_position.y = self.size.y - 275
        self.sound_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                         parent = self,
                                         position = self.sound_slider_cursor_position,
                                         scale = 0.15,
                                         alpha = 0.8)
        #display slider
        displayslider_label_position = self.CENTRE_OF_SCREEN
        displayslider_label_position.x = self.size.x - 760
        displayslider_label_position.y = self.size.y - 340
        self.displayslider_label = LabelNode(text = "Display slider",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = displayslider_label_position)
        display_slider_position = self.CENTRE_OF_SCREEN
        display_slider_position.x = self.size.x - 500
        display_slider_position.y = self.size.y - 330
        self.display_slider = SpriteNode('./assets/sprites/yes_no_slider.PNG',
                                  position = display_slider_position,
                                  parent = self,
                                  scale = 0.2,
                                  alpha = 0.7)
        self.display_slider_cursor_position = self.CENTRE_OF_SCREEN
        self.display_slider_cursor_position.x = self.size.x - 540
        self.display_slider_cursor_position.y = self.size.y - 345
        self.display_slider_cursor = SpriteNode('./assets/sprites/slider_cursor.PNG',
                                         parent = self,
                                         position = self.display_slider_cursor_position,
                                         scale = 0.15,
                                         alpha = 0.8)
        #characters
        characteroptions_label_position = self.CENTRE_OF_SCREEN
        characteroptions_label_position.x = self.size.x - 710
        characteroptions_label_position.y = self.size.y - 410
        self.characteroptions_label = LabelNode(text = "Character options:",
                                    font = ('ChalkboardSE-Light', 50),
                                    parent = self,
                                    position = characteroptions_label_position)
        classicgingerbat_label_position = self.CENTRE_OF_SCREEN
        classicgingerbat_label_position.x = self.size.x - 520
        classicgingerbat_label_position.y = self.size.y - 700
        self.classicgingerbat_label = LabelNode(text = "Classic Ninja      Ginger Ninja      Bat Ninja",
                                    font = ('ChalkboardSE-Light', 40),
                                    parent = self,
                                    position = classicgingerbat_label_position)
        
        # classic ninja
        classic_ninja_position = self.CENTRE_OF_SCREEN
        classic_ninja_position.x = 200
        classic_ninja_position.y = 200
        self.classic_ninja = SpriteNode('./assets/sprites/classic_ninja/c1.PNG',
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.1)
        # ginger ninja
        ginger_ninja_position = self.CENTRE_OF_SCREEN
        ginger_ninja_position.x = 540
        ginger_ninja_position.y = 200
        self.ginger_ninja = SpriteNode('./assets/sprites/ginger_ninja/g1.PNG',
                                    parent = self,
                                    position = ginger_ninja_position,
                                    scale = 0.1)
        # bat ninja
        bat_ninja_position = self.CENTRE_OF_SCREEN
        bat_ninja_position.x = self.size.x - 210
        bat_ninja_position.y = 200
        self.bat_ninja = SpriteNode('./assets/sprites/bat_ninja/b1.PNG',
                                    parent = self,
                                    position = bat_ninja_position,
                                    scale = 0.1)
        # back button
        back_arrow_button_position = self.CENTRE_OF_SCREEN
        back_arrow_button_position.x = 120
        back_arrow_button_position.y = self.size.y - 100
        self.back_arrow_button = SpriteNode('./assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_arrow_button_position,
                                       size = self.size / 8)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
        
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #pass
        if self.back_arrow_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        if self.sound_slider.frame.contains_point(touch.location):
            self.sound_slider_cursor_position.x = self.sound_slider_cursor_position.x - 10
            print("sound slider pressed")
        if self.display_slider.frame.contains_point(touch.location):
            self.display_slider_cursor_position.x = self.display_slider_cursor_position.x - 10
            print("display slider pressed")
        # animate characters when they are clicked for only 1 cycle
        if self.classic_ninja.frame.contains_point(touch.location):
            print('classic chosen')
            classic_counter = 1
            while classic_counter <= 8:
                self.animate_classic_ninja(classic_counter)
                time.sleep(0.1)
                classic_counter = classic_counter + 1
        if self.ginger_ninja.frame.contains_point(touch.location):
            print('ginger chosen')
        if self.bat_ninja.frame.contains_point(touch.location):
            print('bat chosen')
        
        
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def animate_classic_ninja(self, c_count):
        # animates the classic ninja
        #pass
        
        # takes out existing sprite
        self.classic_ninja.remove_from_parent()
        # shows next sprite
        classic_ninja_file = "./assets/sprites/classic_ninja/c" + str(c_count) + ".PNG"
        classic_ninja_position = self.CENTRE_OF_SCREEN
        classic_ninja_position.x = 200
        classic_ninja_position.y = 200
        self.classic_ninja = SpriteNode(classic_ninja_file,
                                        parent = self,
                                        position = classic_ninja_position,
                                        scale = 0.1)
        

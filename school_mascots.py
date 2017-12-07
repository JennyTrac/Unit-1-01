# Created by: Jenny Trac
# Created on: September 19 2017
# This program has 3 buttons and 2 labels to show the mascot of 3 schools

import ui

def mother_teresa_touch_up_inside(sender):
    # show school name and mascot of Mother Teresa High School
    view['school_name_label'].text = "Mother Teresa High School"
    view['mascot_label'].text = "Titan"

def st_joseph_touch_up_inside(sender):
    # show school name and mascot of St. Joseph High School
    view['school_name_label'].text = "St. Joseph High School"
    view['mascot_label'].text = "Jaguar"

def longfields_davidson_touch_up_inside(sender):
    # show school name and mascot of Longfields Davidson Heights Secondary School
    view['school_name_label'].text = "Longfields Davidson Heights Secondary School"
    view['mascot_label'].text = "Raven"

view = ui.load_view()
view.present('sheet')

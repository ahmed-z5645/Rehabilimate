import customtkinter
import time
from PIL import Image


def title_page(title_image, button, hab):

    title_image.place(x=500,y=400, anchor= customtkinter.CENTER)
    button.place(x=500, y=500, anchor= customtkinter.CENTER)
    hab.place(x=510, y=180, anchor = customtkinter.CENTER)
    return

def home_screen(welcome, back, about, bg, bg_line, start, curr_streak, streak, streak_sentence,
                calendar_label, hab_talk):
    welcome.place(x=500, y=100, anchor = customtkinter.CENTER)
    back.place(x=70, y=10, anchor = customtkinter.CENTER)
    about.place(x=960, y=10, anchor = customtkinter.CENTER)
    bg.place(x=500, y=350, anchor = customtkinter.CENTER)
    bg_line.place(x=500, y=350, anchor = customtkinter.CENTER)
    start.place(x=275, y=480, anchor = customtkinter.CENTER)
    curr_streak.place(x=650, y=200, anchor = customtkinter.CENTER)
    calendar_label.place(x=725, y=370, anchor = customtkinter.CENTER)
    hab_talk.place(x=300, y=300, anchor = customtkinter.CENTER)
    return

def video_screen(countd, contin, react, routine):
    countd.place(x=500, y=200, anchor = customtkinter.CENTER)
    contin.place(x=500, y=500, anchor = customtkinter.CENTER)
    react.place(x=300, y=375, anchor = customtkinter.CENTER)
    routine.place(x=700, y= 375, anchor = customtkinter.CENTER)
    return

def done_screen(well_done, contin, picture):
    well_done.place(x=500, y=100, anchor = customtkinter.CENTER)
    contin.place(x=500, y=525, anchor = customtkinter.CENTER)
    picture.place(x=490, y=320, anchor = customtkinter.CENTER)
    return

def streaks_screen(curr_streak, contin, picture):
    curr_streak.place(x=500, y=100, anchor = customtkinter.CENTER)
    contin.place(x=500, y=525, anchor = customtkinter.CENTER)
    picture.place(x=500, y=320, anchor = customtkinter.CENTER)
    return

def abus_screen(title, back, background1, background2, desc1, desc2, desc3, desc4, desc5, ahmed, deepam, saanvi, aizah, Hab, ahmednt, deepamnt,
                saanvint, aizahnt, Habnt):
    title.place(x=500, y=100, anchor = customtkinter.CENTER)
    back.place(x=70, y=10, anchor = customtkinter.CENTER)
    background1.place(x=500, y=170, anchor = customtkinter.CENTER)
    background2.place(x= 500, y=350, anchor= customtkinter.CENTER)
    
    ahmed.place(x=160, y=250, anchor= customtkinter.CENTER)
    deepam.place(x=330, y=250, anchor= customtkinter.CENTER)
    Hab.place(x=500, y=250, anchor= customtkinter.CENTER)
    saanvi.place(x=670, y=250, anchor= customtkinter.CENTER)
    aizah.place(x=840, y=250, anchor= customtkinter.CENTER)

    ahmednt.place(x=160, y= 325, anchor = customtkinter.CENTER)
    deepamnt.place(x=330, y= 325, anchor = customtkinter.CENTER)
    Habnt.place(x=500, y= 325, anchor = customtkinter.CENTER)
    saanvint.place(x=670, y= 325, anchor = customtkinter.CENTER)
    aizahnt.place(x=840, y= 325, anchor = customtkinter.CENTER)

    desc1.place(x=500, y=400, anchor = customtkinter.CENTER)
    desc2.place(x=500, y=430, anchor = customtkinter.CENTER)
    desc3.place(x=500, y=460, anchor = customtkinter.CENTER)
    desc4.place(x=500, y=490, anchor = customtkinter.CENTER)
    desc5.place(x=500, y=520, anchor = customtkinter.CENTER)
    
    return

    

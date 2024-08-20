import customtkinter
import time
from PIL import Image

from Rehabilimate_GUI import *

def start_interactive():
    print("start mirroring")

def start_routine():
    print("start routine")

def gui(title_pic_light, title_pic_dark, hab_calm_pic, calendar_pic_light, calendar_pic_dark, hab_talk_pic_light, hab_talk_pic_dark, fire_pic_light, fire_pic_dark,
        hab_win_pic, hab_fire_pic, ahmed_pfp_pic, deepam_pfp_pic, Hab_pfp_pic, saanvi_pfp_pic, aizah_pfp_pic):

    #Functions to make the buttons work. pretty much just forget old screen, and replace it with old one

    def login():
        print("Logged in!")
        title.place_forget()
        home.place(x=500, y=300, anchor = customtkinter.CENTER)
        home_screen(welcome, ret_title_button, ab_us_button, bg, bg_line, start_button, title_streak,
                    streak, streak_sentence, calendar_label, hab_talk_label)
        return
    def titleback():
        print("Return to title page!")
        home.place_forget()
        title.place(x=500, y=300, anchor = customtkinter.CENTER)
        return
    def start():
        print("Start training")
        home.place_forget()
        video.place(x=500, y=300, anchor = customtkinter.CENTER)
        video_screen(countd, contin_done, react_poten, routine)
        return
    def aboutus():
        print("Go to about us")
        home.place_forget()
        abus.place(x=500, y=300, anchor = customtkinter.CENTER)
        abus_screen(title_abus, ret_home_button, abus_bg1, abus_bg2, desc1, desc2, desc3, desc4, desc5, ahmed_pfp_label, deepam_pfp_label, saanvi_pfp_label,
                    aizah_pfp_label, Hab_pfp_label, ahmed_nt, deepam_nt, saanvi_nt, aizah_nt, Hab_nt)
        return
    def to_well():
        print("Training complete")
        video.place_forget()
        done.place(x=500, y=300, anchor = customtkinter.CENTER)
        done_screen(well_done, contin_streak, hab_win_label)
        return
    def to_streak():
        print("Go to streak screen")
        done.place_forget()
        streaks.place(x=500, y=300, anchor = customtkinter.CENTER)
        streaks_screen(curr_streak, contin_home, hab_fire_label)
        return
    def to_home():
        print("Returning home")
        streaks.place_forget()
        home.place(x=500, y=300, anchor = customtkinter.CENTER)
        return
    def homeback():
        print("Returning to the home page")
        abus.place_forget()
        home.place(x=500, y=300, anchor = customtkinter.CENTER)
    
    
    app = customtkinter.CTk() #creates the window that the gui runs in
    app.title("RehabiliMate")
    app.geometry("1000x600")

    #Frame (these are the different pages of the gui) definition:
    title = customtkinter.CTkFrame(master=app, width=1000, height=600, fg_color=("#FFFFFF", "#242424"))
    home = customtkinter.CTkFrame(master=app, width=1000, height=600, fg_color=("#FFFFFF", "#242424"))
    video = customtkinter.CTkFrame(master=app, width=1000, height=600, fg_color=("#FFFFFF", "#242424"))
    done = customtkinter.CTkFrame(master=app, width=1000, height=600, fg_color=("#FFFFFF", "#242424"))
    streaks = customtkinter.CTkFrame(master=app, width=1000, height=600, fg_color=("#FFFFFF", "#242424"))
    abus = customtkinter.CTkFrame(master=app, width=1000, height = 600, fg_color=("#FFFFFF", "#242424"))
    
    #GUI Object definition below:
    #Page 1:
    title_image = customtkinter.CTkImage(light_image = Image.open(title_pic_light),
                                    dark_image = Image.open(title_pic_dark),
                                    size = (750,375))
    image_label = customtkinter.CTkLabel(title, image = title_image, text="")

    hab_calm = customtkinter.CTkImage(light_image= Image.open(hab_calm_pic),
                                        dark_image = Image.open(hab_calm_pic),
                                        size = (520,346.671))
    hab_calm_label= customtkinter.CTkLabel(title, image = hab_calm, text = "")
    
    title_button = customtkinter.CTkButton(title, width=200, height=50, fg_color = ("#F98486", "#C02819"), text="Continue", 
                                           font = ("Roboto", 20), command = login)
    
    #Page 2:
    
    streak = 10
    streak_sentence = ["Current", "streak:", streak]
    
    welcome = customtkinter.CTkLabel(home, text = "Welcome Back!", fg_color="transparent",
                                 width = 800, height = 100, font = ("gurajada", 100))
    
    ret_title_button = customtkinter.CTkButton(home, width=20, height=10, fg_color=("transparent"), text_color=("#000000", "#FFFFFF"),
                                           text="<<Return to title page", font = ("gurajada", 15), command = titleback)
    
    ab_us_button = customtkinter.CTkButton(home, width=20, height=10, fg_color=("transparent"), text_color=("#000000", "#FFFFFF"),
                                       text="About Us", font = ("gurajada", 15), command = aboutus)
    
    bg = customtkinter.CTkLabel(home, text="", width=900 , height=380, corner_radius=40,
                            fg_color =("#FFDFDF", "#4C2020"))
    bg_line = customtkinter.CTkLabel(home, text="", width=10, height=360,
                                 fg_color = ("#FFB5B5", "#FA8587"))
    
    start_button = customtkinter.CTkButton(home, width=400, height=75, fg_color=("#FFB5B5", "#FA8587"), text_color=("#000000", "#FFFFFF"),
                                       text= "Start Training", font = ("gurajada", 40), command = start)
    
    title_streak = customtkinter.CTkLabel(home, text= streak_sentence, fg_color=("#FFDFDF", "#4C2020"),
                                      font = ("gurajada", 30))
    
    calendar = customtkinter.CTkImage(light_image = Image.open(calendar_pic_light),
                                dark_image = Image.open(calendar_pic_dark),
                                size = (300,300))
    calendar_label = customtkinter.CTkLabel(home, image = calendar, text = "")
    
    hab_talk= customtkinter.CTkImage(light_image = Image.open(hab_talk_pic_light),
                                dark_image = Image.open(hab_talk_pic_dark),
                                size = (350,233.33))
    hab_talk_label = customtkinter.CTkLabel(home, image = hab_talk, text = "")

    for i in range(1, streak): #cover the numers on the calendar with fire emojis as our streak gets bigger
        name = "fire" + str(i)
        name_image = customtkinter.CTkImage(light_image = Image.open(fire_pic_light),
                                      dark_image = Image.open(fire_pic_dark),
                                      size = (40, 40))
        name_label = customtkinter.CTkLabel(home, image = name_image, text = "")
        if i <= 6:
            name_label.place(x=605+48*(i-1), y=315, anchor = customtkinter.CENTER)
        else:
            name_label.place(x=605+48*(i-7), y= 355, anchor = customtkinter.CENTER)


    #Page 3:
    countdown = ["Ready,", "Set,", "Go!"]

    countd = customtkinter.CTkLabel(video, text=countdown, fg_color="transparent",
                                    font = ("gurajada", 100))
    react_poten = customtkinter.CTkButton(video, text="Reaction Potential Mirroring", width=200, height=50, fg_color = ("#F98486", "#C02819"), 
                                           font = ("gurajada", 15), command = start_interactive)
    routine = customtkinter.CTkButton(video, text="Routine", width=200, height=50, fg_color=("#F98486", "#C02819"),
                                      font = ("gurajada", 15), command = start_routine)
    contin_done = customtkinter.CTkButton(video, text="Continue", width=200, height=50, fg_color = ("#F98486", "#C02819"), 
                                           font = ("gurajada", 20), command = to_well)

    #Page 4:
    
    well_done = customtkinter.CTkLabel(done, text = "Well Done!", fg_color="transparent",
                                 width = 800, height = 100, font = ("gurajada", 100))
    contin_streak = customtkinter.CTkButton(done, text="Continue", width=200, height=50, fg_color = ("#F98486", "#C02819"), 
                                           font = ("gurajada", 20), command = to_streak)
    hab_win = customtkinter.CTkImage(light_image=Image.open(hab_win_pic),
                                    size = (337.5,337.5))
    hab_win_label = customtkinter.CTkLabel(done, image = hab_win, text= "")
    #Page 5:
    curr_streak = customtkinter.CTkLabel(streaks, text = streak_sentence, fg_color="transparent",
                                 width = 800, height = 100, font = ("gurajada", 100))
    contin_home = customtkinter.CTkButton(streaks, text="WOW!!", width=200, height=50, fg_color = ("#F98486", "#C02819"), 
                                           font = ("gurajada", 20), command = to_home)
    hab_fire = customtkinter.CTkImage(light_image=Image.open(hab_fire_pic),
                                      size = (450,337.5))
    hab_fire_label = customtkinter.CTkLabel(streaks, image = hab_fire, text = "")

    #About us page:

    title_abus = customtkinter.CTkLabel(abus, text = "About Our Team:", fg_color="transparent",
                                 width = 800, height = 100, font = ("gurajada", 100))
    ret_home_button = customtkinter.CTkButton(abus, width=20, height=10, fg_color=("transparent"), text_color=("#000000", "#FFFFFF"),
                                           text="<<Return to home", font = ("gurajada", 15), command = homeback)
    abus_bg1 = customtkinter.CTkLabel(abus, width= 1000, height = 20, fg_color = ("#FFDFDF", "#4C2020"), text = "")
    abus_bg2 = customtkinter.CTkLabel(abus, width= 1000, height = 20, fg_color = ("#FFDFDF", "#4C2020"), text = "")
    
    description1 = ['Rehabilimate', 'was', 'created', 'for', 'the', 'final', 'design', 'project', 'of', 'an', 'introductory', 'design', 'class.']
    description2 = ['That', 'being', 'said,', 'this', 'project', "wasn't", 'made', 'with', 'the', 'intention', 'of', "'getting", 'a', 'good', "grade'"]
    description3 = ['or', 'to', "'build", 'a', "portfolio'.", 'Rather,', 'we', 'created', 'Rehabilimate', 'to', 'aid', 'and', 'assist', 'the', 'world']
    description4 = ['around', 'us.', 'We', 'wanted', 'to', 'curate', 'all', 'of', 'the', 'skills', 'we', 'had', 'learned', 'to', 'design', 'something']
    description5 = ['that', 'could', 'make', 'a', 'positive', 'impact', 'in', 'our', 'community.']
    
    desc1 = customtkinter.CTkLabel(abus, text= description1, fg_color="transparent", font = ("gurajada", 20))
    desc2 = customtkinter.CTkLabel(abus, text= description2, fg_color="transparent", font = ("gurajada", 20))
    desc3 = customtkinter.CTkLabel(abus, text= description3, fg_color="transparent", font = ("gurajada", 20))
    desc4 = customtkinter.CTkLabel(abus, text= description4, fg_color="transparent", font = ("gurajada", 20))
    desc5 = customtkinter.CTkLabel(abus, text= description5, fg_color="transparent", font = ("gurajada", 20))
    
    #Pictures and Labels for about us page:
    ahmed_pfp = customtkinter.CTkImage(light_image=Image.open(ahmed_pfp_pic),
                                       size = (120, 120))
    deepam_pfp = customtkinter.CTkImage(light_image=Image.open(deepam_pfp_pic),
                                       size = (120, 120))
    Hab_pfp = customtkinter.CTkImage(light_image=Image.open(Hab_pfp_pic),
                                       size = (120, 120))
    saanvi_pfp = customtkinter.CTkImage(light_image=Image.open(saanvi_pfp_pic),
                                       size = (120, 120))
    aizah_pfp = customtkinter.CTkImage(light_image=Image.open(aizah_pfp_pic),
                                       size = (120, 120))

    ahmed_pfp_label = customtkinter.CTkLabel(abus, image = ahmed_pfp, text= "")
    deepam_pfp_label = customtkinter.CTkLabel(abus, image = deepam_pfp, text = "")
    Hab_pfp_label = customtkinter.CTkLabel(abus, image = Hab_pfp, text = "")
    saanvi_pfp_label = customtkinter.CTkLabel(abus, image = saanvi_pfp, text = "")
    aizah_pfp_label = customtkinter.CTkLabel(abus, image = aizah_pfp, text = "")

    ahmed_nt = customtkinter.CTkLabel(abus, text = "Ahmed Zafar", fg_color="transparent",
                                      font = ("gurajada", 15))
    deepam_nt = customtkinter.CTkLabel(abus, text = "Deepam Patel", fg_color="transparent",
                                      font = ("gurajada", 15))
    Hab_nt = customtkinter.CTkLabel(abus, text = 'Rehab, "Habby", Crab', fg_color="transparent",
                                      font = ("gurajada", 15))
    saanvi_nt = customtkinter.CTkLabel(abus, text = "Saanvi Sood", fg_color="transparent",
                                      font = ("gurajada", 15))
    aizah_nt = customtkinter.CTkLabel(abus, text = "Aizah Malik", fg_color="transparent",
                                      font = ("gurajada", 15))

    
    
    #Function calls:
    title.place(x=500, y=300, anchor= customtkinter.CENTER)
    title_page(image_label, title_button, hab_calm_label)
    app.mainloop()
    return

def main():

    #Example Windows: = "C:/Users/ahmed/downloads/"
    #Example Raspberry Pi: = ""
    ##THE LINE BELOW THIS.
    Directory_prefix = "C:/Users/ahmed/downloads/"
    ##THIS LINE RIGHT HERE ^^^^^^ EDIT THIS LINE AND INCLUDE THE FORWARD SLASH AT THE END
    title_pic_light = Directory_prefix + "DP4/Pictures/Rehab_light.png"
    title_pic_dark = Directory_prefix + "DP4/Pictures/Rehab_dark.png"
    hab_calm_pic = Directory_prefix + "DP4/Pictures/Hab_calm.png"

    calendar_pic_light = Directory_prefix + "DP4/Pictures/calendar_light.png"
    calendar_pic_dark = Directory_prefix + "DP4/Pictures/calendar_dark.png"
    hab_talk_pic_light = Directory_prefix + "DP4/Pictures/Hab_talk_light.png"
    hab_talk_pic_dark = Directory_prefix + "DP4/Pictures/Hab_talk_dark.png"
    fire_pic_light = Directory_prefix + "DP4/Pictures/Fire_light.png"
    fire_pic_dark = Directory_prefix + "DP4/Pictures/Fire_dark.png"

    hab_win_pic = Directory_prefix + "DP4/Pictures/Hab_win.png"
    hab_fire_pic = Directory_prefix + "DP4/Pictures/Hab_fire.png"

    ahmed_pfp_pic = Directory_prefix + "DP4/Profile_Pictures/Ahmed_Profile.png"
    deepam_pfp_pic = Directory_prefix + "DP4/Profile_Pictures/Deepam_Profile.png"
    Hab_pfp_pic = Directory_prefix + "DP4/Profile_Pictures/Hab_Profile.png"
    saanvi_pfp_pic = Directory_prefix + "DP4/Profile_Pictures/Saanvi_Profile.png"
    aizah_pfp_pic = Directory_prefix + "DP4/Profile_Pictures/Aizah_Profile.png"
    
    gui(title_pic_light, title_pic_dark, hab_calm_pic, calendar_pic_light, calendar_pic_dark, hab_talk_pic_light, hab_talk_pic_dark, fire_pic_light, fire_pic_dark,
        hab_win_pic, hab_fire_pic, ahmed_pfp_pic, deepam_pfp_pic, Hab_pfp_pic, saanvi_pfp_pic, aizah_pfp_pic)
    return


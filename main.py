from tkinter import *
import time

FONT = 'Helvetica Neue'
NAVY = '#191919'
BLUE = '#2D4263'
RED = '#C84B31'
WHITE = '#ECDBBA'
word_count = 0
text = "Avatar: The Last Airbender has returned to Netflix. " \
       "The Friday release marks the first time in several years that the beloved animated series has been available on a major streaming platform in the U.S. " \
       "The release is undoubtedly meant to build anticipation for Netflix’s planned live-action adaptation of the show, but no matter how you feel about that news, Airbender’s return is a win-win for Netflix and viewers alike. " \
       "That’s true whether you’re an Airbender fan who’s feeling nostalgic, or someone who’s been meaning to check it out but never had the chance to before — or if, like me, you’ve never stopped missing Airbender since it aired. " \
       "2020 marks the 15th anniversary of the premiere of Airbender, which ran for three seasons on Nickelodeon from 2005–2008. An action-adventure set in a high fantasy world, Airbender had a huge influence on the many acclaimed, serialized animated series that followed. " \
       "But while longtime fans recognize the show’s excellence, M. Night Shyamalan’s notorious travesty of a film adaptation in 2010 thwarted Airbender’s big push into the mainstream. " \
       "That’s a huge shame, because Airbender deserves to be more widely recognized by the broader public as one of the best shows ever made. " \
       "In my experience, most viewers don’t merely like Airbender; they love it, the kind of love that usually gets reserved for shows with much broader critical and cultural clout. " \
       "There’s a multitude of reasons for that level of devotion. The animation is flawless and beautiful. " \
       "The story — a goofy kid who’s also the most powerful spiritual mage on the planet joins his friends on a quest to save the world — first surprises you, then charms you, and ultimately sweeps you up and deposits you in an entirely different headspace than where you began. Now that Airbender is on Netflix once more, it’s primed for an overdue, well-earned cultural resurgence. Here are four things to know about the show if you’re watching it for the first time, or just want to understand what makes the series great." \
       "Airbender’s storyline was unprecedented for its complexity and scope."
words = text.split(' ')
current_word = words[0]
start_time = None

#----------------------------WORD CHECKING MECHANISM------------------------#

def wordcheck(event):
    global current_word
    global word_count
    typed = entry.get()
    if typed.strip() == current_word:
        word_label.config(fg=WHITE)
        entry.delete(0, END)
        word_count+=1
        current_word = words[word_count]
        word_label.config(text=current_word)
    calc_wpm()

#---------------------------CALCULATE WPM------------------------------------#

def start_timer(event):
    global start_time
    start_time = time.time()

def calc_wpm():
    global word_count
    global start_time
    current_time = time.time()
    time_elapsed_s = current_time - start_time
    time_elapsed_m = time_elapsed_s / 60
    wpm = round(word_count / time_elapsed_m)
    wpm_label.config(text=f"Words Per Minute: {wpm}")

#--------------------------------UI SETUP------------------------------------#

window = Tk()
window.title('How Fast Can You Type?')
window.minsize(200, 200)
window.config(bg=NAVY, padx=50, pady=50)

label = Label(text='Type the words as they appear below: ', fg=RED, bg=NAVY, font=(FONT, 50, 'bold'))
label.pack()
wpm_label = Label(text='Words Per Minute: 0', fg=WHITE, bg=NAVY, font=(FONT, 30, 'bold'))
wpm_label.pack()
word_label = Label(text=current_word, fg=BLUE, bg=NAVY, font=(FONT, 35, 'bold'))
word_label.pack()
entry = Entry(fg=WHITE)
entry.bind("<Return>", wordcheck)
entry.bind("<Enter>", start_timer)
entry.pack()

window.mainloop()
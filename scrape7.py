import sys
import requests
from bs4 import BeautifulSoup
from time import sleep
from tkinter import *
import webbrowser

class App():

    w = 390
    h = 420
    bgColor = '#000000'

    def __init__(self, labeltext):

        self.url = labeltext[labeltext.find('\n') + 1:]

        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.configure(background=self.bgColor)    # setting background color

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # set the dimensions of the screen and where it is placed
        #self.root.geometry(f'{self.w}x{self.h}+{int((ws - self.w - 25)/2)}+{10}')
        self.root.geometry(f'{self.w}x{self.h}+{(ws - self.w)}+{hs - self.h -100}')

        self.label = Label(self.root, text=f"\t\tNew question on {labeltext}", anchor='w',\
            fg='#ffffff', bg=self.bgColor, bd=0, wraplength=350, highlightcolor='#ff0000',\
            justify='left', relief='raised', takefocus=True)
        
        self.label.pack(side='right', expand=True, pady=1, fill='both')    # put label on root
        self.label.bind("<Button-1>", self.bopen)   # bind bopen function on label

        self.bQuit = Button(self.root, text="Fuck it", command=self.closeSelf)
        self.bQuit.configure(background = '#4B006E')    # configure background of the button
        self.bQuit.place(x=365, y=0, height=25, width=25)   # place the quit button
        
        self.root.after(4500, lambda: self.root.destroy())  # close popup after 3 seconds itself
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)   # so that window is always topmost
        self.root.update()
        self.root.mainloop()

    def closeSelf(self):        # closes the popup
        self.root.destroy()

    def bopen(self, event):     # open the url in default webbrowser
        webbrowser.open(self.url)
        self.closeSelf()


def get_question_from_tag(tag, last_qs):
    url = f"https://stackoverflow.com/questions/tagged/{tag}?sort=newest&pageSize=30"
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    all_summaries = soup.find_all("div", class_='question-summary')
    new_summary = all_summaries[0]
    all_links = new_summary.find_all('a', class_='question-hyperlink')
    new_qs_link = all_links[0].get('href')
    #print(f'new_qs_link : {new_qs_link}')
    new_qs_title = all_links[0].text
    #print(f'new_qs_title : {new_qs_title}')
    all_exceprts = new_summary.find_all('div', class_='excerpt')
    new_qs_excerpt = all_exceprts[0].text
    #print(f'new_qs_excerpt : {new_qs_excerpt}')
    all_post_tags = new_summary.find_all('a', class_='post-tag')
    new_qs_tags = ', '.join(set([k.text for k in all_post_tags]))

    label_text = tag.capitalize() + '\n\n\n\n' + "TITLE : \t" + new_qs_title + '\n\n' + 'EXCERPT : \t' + new_qs_excerpt+ '\n\n' + 'TAG : \t' + new_qs_tags
    if last_qs != new_qs_link:
        app = App(label_text)
    return new_qs_link

def main(tag): 
    try:
        last_qs_url = ''
        while True:
            last_qs_url = get_question_from_tag(tag, last_qs_url)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main('python')

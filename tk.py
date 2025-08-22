import tkinter as tk



dcitionary = {}
def click():
    topic = Entry.get()
    upvote = upvote_count.get()
    comment = comment_count.get()
    profile = profile_name.get()
    dcitionary = {"topic":topic,"upvotes":upvote,"comment":comment,"profile":profile}
    tk.Label(root,text="Wait a little",font=("stuf/MozillaText-SemiBold.ttf",10),anchor="center",background=bg_color,fg="white").grid(row=7,column=0,sticky="s",columnspan=2)
    root.quit()
    return dcitionary
    
bg_color = "#111111"
root = tk.Tk()
root.minsize(500,190)
root.maxsize(500,190)
root.title("VIDGEN")
root.config(background=bg_color)
    
tk.Label(root,text="Enter the topic",font=("stuf/MozillaText-SemiBold.ttf",10),background=bg_color,fg="white").grid(row=1,column=0,sticky="w",padx=30)
Entry = tk.Entry(root,width=71)
Entry.grid(row=2,column=0,columnspan=2,padx=30)

tk.Label(root,text="Upvotes",font=("stuf/MozillaText-SemiBold.ttf",10),background=bg_color,fg="white").grid(row=3,column=0,sticky="w",padx=30)
upvote_count = tk.Entry(root,width=30)
upvote_count.grid(row=4,column=0,padx=30,sticky="w")

tk.Label(root,text="Comments",font=("stuf/MozillaText-SemiBold.ttf",10),background=bg_color,fg="white").grid(row=3,column=1,sticky="w",padx=30)
comment_count = tk.Entry(root,width=30)
comment_count.grid(row=4,column=1,padx=30,sticky="e")

tk.Label(root,text="Profile name",font=("stuf/MozillaText-SemiBold.ttf",10),background=bg_color,fg="white").grid(row=5,column=0,sticky="w",padx=30)
profile_name = tk.Entry(root,width=30)
profile_name.grid(row=6,column=0,padx=30,sticky="w")

Button_entry = tk.Button(root,text="Submit",fg='white',background=bg_color,anchor="center",command=click).grid(row=6,column=1,padx=30)
root.mainloop()

    
    

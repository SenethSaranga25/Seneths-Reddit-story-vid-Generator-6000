from PIL import Image, ImageDraw, ImageFont

def create_card(title,profile,Profile_name,upvotes,comments):
    print("[Title card creation started]")
    end_y = 460
    end_x = 800
    upvote_line = 420 #text
    title_array = []
    title_array = title.split(" ")
    use_array = False
    main_texty = 360
    main_textx = 20
    icon_size = 32
    # fonts 
    name_font = ImageFont.truetype("stuf\MozillaText-SemiBold.ttf",size=25)
    main_font = ImageFont.truetype("stuf\MozillaText-SemiBold.ttf",size=35)
    icon_font = ImageFont.truetype("stuf\MozillaText-SemiBold.ttf",size=20)

    #gets the length of the text
    length_main = main_font.getlength(title)
    if length_main > end_x-60:
        expo = round((length_main/(end_x-60))+0.5)
        end_y += 20 * expo
        if end_y > 800:
            end_y = 800
        upvote_line +=20 * expo
        if upvote_line > 800:
            upvote_line =800
        use_array = True
    #start creating the profile picture
    prof_pic = Image.open(profile).convert("RGBA")
    mask = Image.new('L',prof_pic.size) # make mask
    draw = ImageDraw.Draw(mask)

    width,hight = prof_pic.size
    draw.circle([width/2,hight/2], radius=hight/2,fill="white") # make white circle

    circle_img = Image.new("RGBA", prof_pic.size)
    circle_img.paste(prof_pic, (0, 0), mask)
    lr = (width-hight)/2
    circle_img = circle_img.resize([hight,hight],Image.Resampling.NEAREST,box =[lr,0,lr+hight,hight]) 
    #resizing profile picture to make it a square
    circle_img.save("stuf/prof_pic.png")
    #end creating the profile picture

    # creates the body of the card
    img = Image.new("RGBA",(800,800), (255,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0,250),(end_x,end_y)],radius=20,fill="white",outline=None)
    
    # adding the profile pic
    prof_pic = Image.open("stuf/prof_pic.png").convert("RGBA")
    prof_pic = prof_pic.resize([80,80])
    img.paste(prof_pic,(20,270),prof_pic)# paste the profile picture

    posx = 110

    for i in range(6):
        if i != 0:
            name = f"stuf\\reddit_badges\\{i}.png"
            badge = Image.open(name).convert("RGBA")
            badge = badge.resize((20,20),Image.Resampling.LANCZOS)
            img.paste(badge,(posx,320),badge)
            posx += 25

    # upvote button
    upvote_button = Image.open("stuf/icons/arrow.png").convert("RGBA")
    upvote_button = upvote_button.resize((icon_size,icon_size),Image.Resampling.LANCZOS)
    img.paste(upvote_button,(20,upvote_line-5),upvote_button)

    #comment button
    comment_button = Image.open("stuf\icons\chat-bubble.png").convert("RGBA")
    comment_button = comment_button.resize((icon_size,icon_size),Image.Resampling.LANCZOS)
    img.paste(comment_button,(140,upvote_line-5),comment_button)

    #share button
    share_button = Image.open("stuf\icons\share.png").convert("RGBA")
    share_button = share_button.resize((icon_size,icon_size),Image.Resampling.LANCZOS)
    img.paste(share_button,(690,upvote_line-5),share_button)


    #adds the text
    
    draw.text((110,290),Profile_name,fill="black",font=name_font)
    if not use_array:
        text = title
    elif use_array:
        text_size = 0
        prev_text = ""
        text_size_prev_cut = 0
        for word in title_array:
            if word!=title_array[0]:
                prev_text = text
                text += " "+word
            else:
                text = word
            text_size = main_font.getlength(text)
            if text_size-text_size_prev_cut >  end_x-60:
                text = prev_text
                text += "\n" + word
                text_size_prev_cut = text_size
    draw.text((main_textx,main_texty),text,fill="black",font=main_font)
    
    def add_adjective(num):
        adjective = ""
        while True:
            if len(str(round(num))) >= 4:
                num = round(num/1000,1)
                if adjective == "":
                    adjective = "K"
                elif adjective == "K":
                    adjective = "M"
                elif adjective == "M":
                    adjective = "B"
                elif adjective == "B":
                    adjective = "T"
            else:
                break
        
        num = str(num) + adjective
        return num
    upvotes = add_adjective(upvotes)
    comments = add_adjective(comments)


    #upvotes number
    draw.text((60,upvote_line),upvotes,fill="black",font=icon_font)

    #comments number
    draw.text((185,upvote_line),comments,fill="black",font=icon_font)

    #share
    draw.text((735,upvote_line),"share",fill="black",font=icon_font)
    img =  img.resize([800,end_y-250],Image.Resampling.NEAREST,box =[0,250,end_x,end_y])
    img.save("stuf/title_card.png") # end saving the file
    print("[Title Card Created !!!!]")
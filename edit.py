from moviepy import ColorClip, ImageClip, CompositeVideoClip,VideoFileClip,CompositeAudioClip,AudioFileClip
from PIL import Image, ImageDraw, ImageFont
from faster_whisper import WhisperModel
import wave
import math
from random import randint

def edit():
    print("[Editing Started]")
    story_start = 0
    with wave.open("stuf\\audio\\title.wav", 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        story_start = frames / float(rate)

    audio = "stuf\\audio\\story.wav"

    with wave.open(audio, 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)

    # gets the transcribe of the voice
    model = WhisperModel("base",device="cpu",compute_type="int8")
    segments,info = model.transcribe(
        audio,
        word_timestamps=True
    )

    print(f"Detected language: {info.language}")

    bg = VideoFileClip("stuf\\bg_videos\\1.mp4")
    duration_1 = bg.duration
    cut_p = randint(0,round(duration_1-round(duration+story_start)))
    cuts = [[0,cut_p],[cut_p+duration+story_start,duration_1]]
    for cut in cuts:
        bg = bg.with_section_cut_out(start_time=cut[0],end_time=cut[1])
    card = (ImageClip("stuf\\title_card.png",duration=story_start).resized(lambda t: 1.0 + 0.3 * math.exp(-5*t) * math.sin(10*t)).with_start(0).with_position("center"))


    varible_inc = 2
    word_count = 0
    segments_count = 0
    clips = []
    all_segments = []
    for segment in segments:
        all_segments.append(segment)
        #seperates segants to a array

    #creating and settingup all the text
    for segment in all_segments:
        for word in segment.words:
            if word_count + 1 < len(segment.words):  
                # There is another word in this segment
                duration = segment.words[word_count + 1].start - word.start
            elif segments_count + 1 < len(all_segments) and all_segments[segments_count + 1].words:
                # No more words in this segment, but there is a next segment with at least one word
                next_segment = all_segments[segments_count + 1]
                duration = next_segment.words[0].start - word.start
            else:
                # Last word in the entire audio
                duration = word.end - word.start
            img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("stuf\\MozillaText-SemiBold.ttf", 90)
            text = word.word
            draw.text([1080/2,1920/2],text, font=font, fill="white",align="center",anchor='mm',stroke_fill="black",stroke_width=14,)
            img.save(f"stuf\\text_img\\text{varible_inc}.png")
            text = (ImageClip(f"stuf\\text_img\\text{varible_inc}.png",duration=duration).resized(lambda t: 1.0 + 0.3 * math.exp(-5*t) * math.sin(10*t)).with_start(story_start+word.start).with_position("center"))
            clips.append(text)
            varible_inc+=1
            word_count+=1
        segments_count+=1
        word_count = 0
    
    try:
        with open("videos\\videoC.txt","r") as VidC:
            count =  VidC.readline(-1)
        with open("videos\\videoC.txt","w") as VidC:
            VidC.write(str(int(count)+1))
    except:
        print("[Editiing Failed No file named videoC found!!!]")

    # sets sound
    title_sound = AudioFileClip("stuf\\audio\\title.wav").with_start(0)
    story_sound = AudioFileClip("stuf\\audio\\story.wav").with_start(story_start)
    # Combine
    final = CompositeVideoClip([bg]+[card]+clips)
    sound = CompositeAudioClip([title_sound,story_sound])
    final.audio = sound
    name = f"videos\\{count}.mp4"
    final.write_videofile(name, fps=30)
    print("[Editing Done!!!]")
from google import genai
from google.genai import types
import wave
import random
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

def create_story(topic):
    print("[AI Started]")
    api_key_num = 0
    voice = True
    api_keys = []
    num_lines = 0
    try:
       f = open("Api_keys.txt", "r")
       for _ in f.readlines():
          num_lines+=1
          api_keys += [_]
       if num_lines == 0:
            print("No api Keys found")
            return 1
    except:
       print("No file named Api_keys.txt found!!!")
    api_key = api_keys[api_key_num]
    client = genai.Client(api_key=api_key)
    language = 'en'

    topic
    while True:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= f"""
                        Write a realistic 2-minute Reddit-style story that might use abbrivations like "AITA" or "AITJ" and when using they are in the story part replace these abbriviations with there real meaning "Am I the jeark" and "Am I the Asshole" respectivly, ending with a matching title starting with : that is less than 12 words dont leave any space after the title the output should end with the title, the title can also contain words like AITA and AITJ.
                        the story's sructure is as follows

                        1.Story
                        2.:title for the story that is less than 12 words in length

                        Look at what kind of reddit story videos has gone viaral on the short feed close to the current date and creat a similer story to what those videos contain and use a similer type of hook for the title 
                    """
        )
        text = response.text
        text = text.split(":")
        story_text = text[0]

        title = text[1]
        while True:
            if title[0] == ' ':
                title = title[1:]
            if title[0] != ' ':
                while True:
                    if title[-1] == ' ':
                        title = title[:-2]
                    if title[-1] != ' ':
                        break
                break
        prev = False
        for i in range(len(title)):
            if i == " " and prev:
                title = title[:i] + title[i+1:]
                break
            prev = i

        if len(title) > 57:
            print("Title too long")
        else:
            break
    print("[Phase one Completed]")
    print("[Phase 2 Started]")
    while voice:
        try:
            story_voice = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=f"Say like a story teller with intrest and talk a little fast:{story_text}",
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                        ) 
                    )
                ),
            )
        )
            title_voice = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=f"Say with intrest :{title}",
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                        )
                    )
                ),
            )
        )
            voice = False
            break
        except:
           if api_key_num == num_lines:
              return 1
           api_key_num+=1
           api_key = api_keys[api_key_num]
           client = genai.Client(api_key=api_key)
           print(f"KEY changed to,{api_keys[api_key_num+1]}")

    print("[Phase two Completed]")
    data = story_voice.candidates[0].content.parts[0].inline_data.data
    wave_file("stuf\\audio\\story.wav", data)
    data = title_voice.candidates[0].content.parts[0].inline_data.data
    wave_file("stuf\\audio\\title.wav", data)
    print("[Ai is Done!!!!]")

    return title
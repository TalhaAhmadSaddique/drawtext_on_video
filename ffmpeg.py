

import ffmpeg
import os
import base64
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!!"}


@app.post("/text_on_video")
def text1(text, font_color, font_size):
  os.system(f"""ffmpeg -i result.mp4 -vf drawtext="fontfile=font.ttf: \
  text={text}: fontcolor={font_color}: fontsize={font_size}: box=1: boxcolor=black@0.5: \
  boxborderw=5: y=400-line_h:x=-50*t"  -codec:a copy output.mp4""")
  video_file = 'output.mp4'
  file = open(video_file, 'rb').read()
  enc=base64.b64encode(file)
  return enc


# print(text1('this is a good book', 'yellow', 32))

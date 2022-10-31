from flask import Flask, request
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from flask_cors import CORS


# define a variable to hold you app
app = Flask(__name__)
CORS(app)

# define your resource endpoints
@app.route('/')
def index_page():
    return "Hello world"

@app.route('/time')
def get_time():
    return str(datetime.datetime.now())


# funtion for geting transcript from youtube_trascript_api
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    s = str()
    for x in transcript:
        s += x['text']
        s+=' '
    return s

def get_videoId(url):
    from urllib.parse import urlparse, parse_qs

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url
        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError


@app.route('/api/summarize', methods=['GET'])
def extract_videoid():
    args = request.args
    url = args.get('youtube_url')
    
    video_id = get_videoId(url)
    x = get_transcript(video_id)
    return x
    

def get_summary(transcript):
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    # encode the text into tensor of integers using the appropriate tokenizer
    inputs = tokenizer.encode("summarize: " + transcript, return_tensors="pt", max_length=512, truncation=True)
    # generate the summarization output
    outputs = model.generate(
        inputs, 
        max_length=300, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True)
    # just for debugging
    # print(outputs)
    return(tokenizer.decode(outputs[0]))




# server the app when this file is run
if __name__ == '__main__':
    app.run()


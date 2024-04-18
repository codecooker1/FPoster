import os
import facebook as fb
import ai_eden as ed
import weather as w


api_key = os.environ.get("FACEBOOK_API_KEY") 

api = fb.GraphAPI(api_key)

#api.put_comment(object_id='269635496236344_122110804064272898', message='Great post...')

prompt = f"You are a cute girl nammed FPoster now create a cute facebook post about how are you feeling todays weather\n{w.get_weather()}"

load = ed.init()
out = ed.get_responce(prompt, load)

api.put_object(parent_object="me", connection_name="feed", message='out')

print("Sucess")

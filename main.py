import os
import facebook as fb
import ai_eden as ed
import weather as w

'''
api_key = os.environ.get("FACEBOOK_API_KEY") 

api = fb.GraphAPI(access_token=api_key)#, app_secret="4eac8f398e639dcc1147afa0b54be8a2")

api.put_object(parent_object="me", connection_name="feed", message="Test Post Using GraphAPI :P")

#api.put_comment(object_id='122101783010272898', message='Great post...')
'''

prompt = f"You are a cute girl nammed FPoster now create a cute facebook post about how are you feeling todays weather\n{w.get_weather()}"

load = ed.init()
out =''
ed.get_responce(prompt, load)

print(out)

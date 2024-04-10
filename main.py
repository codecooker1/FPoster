
import facebook as fb

api_key = "EAAFxFQ3wfYgBO894DLUs7Pn61smNk5MVFavVlX7iEFeBQxFgHl73DYcVOYM5STdXNtFYn7H1Rs6G43QH1sQLzqUSzLw6FTJCxxZBZBz0azPjpwqiKlc501aGZCb560RfNnwghgM256tg3iqAj7MGGo73n25s8Y6PmlDAb9jfRruJjaTmDZBZAv5XV9GeaccqEVMbHPmGAGNYaRznrV5EZCZAwNOfIkmnK4G8GLbZBWIZD"

api = fb.GraphAPI(access_token=api_key)#, app_secret="4eac8f398e639dcc1147afa0b54be8a2")

api.put_object(parent_object="me", connection_name="feed", message="Test Post Using GraphAPI :P")

#api.put_comment(object_id='122101783010272898', message='Great post...')

import os
import traceback
from pathlib import Path

print("""
 _______  ___   __    _  _______  _______  ___        
|       ||   | |  |  | ||       ||       ||   |       
|_     _||   | |   |_| ||    ___||    ___||   |       
  |   |  |   | |       ||   | __ |   |___ |   |       
  |   |  |   | |  _    ||   ||  ||    ___||   |___    
  |   |  |   | | | |   ||   |_| ||   |___ |       |   
  |___|  |___| |_|  |__||_______||_______||_______|   
 _______  _______  __    _  _______  _______  ___     
|       ||   _   ||  |  | ||       ||       ||   |    
|_     _||  |_|  ||   |_| ||    ___||    ___||   |    
  |   |  |       ||       ||   | __ |   |___ |   |    
  |   |  |       ||  _    ||   ||  ||    ___||   |___ 
  |   |  |   _   || | |   ||   |_| ||   |___ |       |
  |___|  |__| |__||_|  |__||_______||_______||_______|

""")

try:
    import yt_dlp
    url = input('What is your tingel tangel? ')
    os.chdir('Z:/music')
    argv = [ '-v', '--add-metadata', '--extract-audio', '--audio-format', 'mp3', url ]
    yt_dlp.main(argv)
except SystemExit:
    pass # error message already printed
except Exception as e:
    traceback.print_exc(limit=0)

input('TANGEL TINGEL!')


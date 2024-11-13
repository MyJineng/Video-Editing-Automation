encoder_path = 'C:\Program Files\Adobe\Adobe Media Encoder 2025\Adobe Media Encoder.exe' # Path to Adobe Media Encoder
source_path = r'C:\...' # Path to files to be encoded
processed_path = 'C:\...' # Path to files finished encoding
music_file = r'C:\...\the big game.opus' # Path for sound file when finished encoding - default included

driver_path = 'C:\...\geckodriver.exe' # Path to webdriver for selenium - usually geckodriver or chromedriver
email = 'dummy_email@dummy.me'
password = 'Fakepassword123'
send_to_list = ['dummy1_email@dummy.me, dummy2_email@dummy.me']
email_message = 'This is an automated WeTransfer upload.'

# PIPs needed to run:
# pyautogui - desktop clicks and file selections
# pygame - notification sound
# selenium - web automation
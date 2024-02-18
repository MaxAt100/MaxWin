import winsound

# Function to play the sound file continuously
def play_sound():
    while True:
        winsound.PlaySound("MaxWin.wav", winsound.SND_FILENAME)
        
# Call the function to start playing the sound
play_sound()
from pydub import AudioSegment
from pydub.playback import play

# Some magic string to give text some style
class Styles:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
    UNDERLINE = "\033[4m"
    END_FORMAT = "\033[0m"

# A helper function to give a string some style
def style(text :str, style:str = Styles.FAIL) -> str:
    return f"{style}{text}{Styles.END_FORMAT}"

# Plays the file in the parameter
def playAudio(filename :str = "calculando.wav"):
    play(AudioSegment.from_wav(f"/Users/ivanarrizabalagagetino/Projects/learning/python_kids/{filename}"))

# Presentation
print('''
 __      __       .__                                ._._._.
/  \    /  \ ____ |  |   ____  ____   _____   ____   | | | |
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  | | | |
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   \|\|\|
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  ______
       \/       \/          \/            \/     \/   \/\/\/
      '''
      )
print("I'm T.O.N.T.I.N.G a secret system that describes human after a few questions, let's try with you...\n")

# Let's ask for the details
celebrity = input("Celebrity: ")
adjetive = input("Adjective: ")
silly_food = input("Silly thing or a food: ")
things_plural = input("A thing in plural: ")
verb = input("Verb: ")
animal = input("Animal: ")
profession = input("Profession: ")
place = input("Place: ")
to_buy = input("Something you want to buy: ")
phrase = input("Lastly, a cool phrase: ")

# Some decoration
print('''
               __  .__    .__        __   .__                             
             _/  |_|  |__ |__| ____ |  | _|__| ____    ____               
             \   __\  |  \|  |/    \|  |/ /  |/    \  / ___\              
              |  | |   Y  \  |   |  \    <|  |   |  \/ /_/  >             
 /\  /\  /\   |__| |___|  /__|___|  /__|_ \__|___|  /\___  /   /\  /\  /\ 
 \/  \/  \/             \/        \/     \/       \//_____/    \/  \/  \/\n\n\n
      ''')
playAudio()
playAudio()

# List of phrases to fill in
phrases = [
    f"Hi my name is {style(celebrity)}, but my friends call me {style(adjetive)} {style(silly_food)}.",
    f"My favorite color is the color of {style(things_plural)} and my favorite thing to do is {style(verb)}.",
    f"My parents were a {style(animal)} and {style(profession)}, which is why we lived in {style(place)}.",
    f"You probably know me from my TV commercial for {style(to_buy)}.",
    f"I'm the one who says, '{style(phrase)}' at the very end!\n\n"

]

# Putting all phrases together
template = "\n".join(phrases)

#Showing the paragraph to the world
print(template)

# Bye
print('''
  ___ ___                  __           .__                 .__          __           ._._.
 /   |   \_____    _______/  |______    |  | _____    ___  _|__| _______/  |______    | | |
/    ~    \__  \  /  ___/\   __\__  \   |  | \__  \   \  \/ /  |/  ___/\   __\__  \   | | |
\    Y    // __ \_\___ \  |  |  / __ \_ |  |__/ __ \_  \   /|  |\___ \  |  |  / __ \_  \|\|
 \___|_  /(____  /____  > |__| (____  / |____(____  /   \_/ |__/____  > |__| (____  /  ____
       \/      \/     \/            \/            \/                \/            \/   \/\/
      ''')
from enum import Enum
import os


def createFighterFolders():
    os.chdir(os.path.join(os.getcwd(), os.pardir))
    char_data_folder = 'Character Data'

    try:
        os.mkdir(char_data_folder)
    except FileExistsError:
        print(f"Directory '{char_data_folder}' already exists. Skipping creation...")
    # Create "Character Data" Folder

    os.chdir(char_data_folder)
        # Inside "char. data"

    for i in PlayableCharacter:
        character_name = i.value
        try:
            os.mkdir(character_name)
        except FileExistsError:
            print(f"Directory '{character_name}' already exists. Skipping creation...")
            # Character folder created
        os.chdir(os.path.join(os.getcwd(), character_name))
        # Inside the specfied character
        character_url = base_url + i.value + suffix_url

        # Text file w/ URL
        f = open(i.value + ".txt", "w" )
        f.write(character_url)
        f.close()
        character_links.update({i.value: character_url})
        os.chdir('..')









# parse a site for table data

class PlayableCharacter(Enum):
    AYANE = "Ayane"
    BASS_ARMSTRONG = "Bass Armstrong"
    BAYMAN = "Bayman"
    BRAD_WONG = "Brad Wong"
    CHRISTIE = "Christie"
    DIEGO = "Diego"
    ELIOT = "Eliot"
    HELENA_DOUGLAS = "Helena Douglas"
    HITOMI = "Hitomi"
    HONOKA = "Honoka"
    JANN_LEE = "Jann Lee"
    KASUMI = "Kasumi"
    KOKORO = "Kokoro"
    KULA_DIAMOND = "Kula Diamond"
    LEIFANG = "Leifang"
    LISA_HAMILTON = "Lisa Hamilton"
    MAI_SHIRANUI = "Mai Shiranui"
    MARIE_ROSE = "Marie Rose"
    MILA = "Mila"
    MOMIJI = "Momiji"
    NICO = "NiCO"
    NYOTENGU = "Nyotengu"
    PHASE_4 = "Phase 4"
    RACHEL = "Rachel"
    RAIDOU = "Raidou"
    RIG = "Rig"
    RYU_HAYABUSA = "Ryu Hayabusa"
    TAMAKI = "Tamaki"
    TINA_ARMSTRONG = "Tina Armstrong"
    ZACK = "Zack"

base_url = "https://deadoralive.fandom.com/wiki/"
character_name = None
suffix_url = "/Dead_or_Alive_6_command_list"
character_links = {}


# creates dictionary with character name : url link

# create folders
createFighterFolders()






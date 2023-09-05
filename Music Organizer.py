
import os,random,shutil

print("Music organizer Program\n-----------------------")
music_folder_path=(input("Adauga calea unde se regaseste muzica:"))
new_folder_path=(input("Adauga calea unde se vor afla noile fisiere:"))

def new_folder():
    nume=input("Adaugati numele folderului: ")
    name=new_folder_path+nume
    os.mkdir(name)

def random_music_list():
    music_list=[]
    content=os.listdir(music_folder_path)
    random.shuffle(content)
    music_list.append(content)
    return content

def order_songs(music_folder_path):
    old_names = random_music_list()
    new_names = []

    for number, name_song in enumerate(old_names,start=1):
        new_name = str(number) + "." + name_song
        new_names.append(new_name)

    for i in range(len(old_names)):
        source_path = os.path.join(music_folder_path, old_names[i])
        destination_path = os.path.join(music_folder_path, new_names[i])
        os.rename(source_path, destination_path)

order_songs(music_folder_path) 


def list_99():
    lista = random_music_list()
    random.shuffle(lista)
    return lista[:99]
            
def muta_99():
    nume_folder=input("Introduceti nume folder:")
    source_folder = music_folder_path
    destination_folder =new_folder_path+nume_folder
    for file_name in list_99():
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
    print("done")

def muta_toate():
    nume_folder=input("Introduceti nume folder:")
    source_folder = music_folder_path
    destination_folder =new_folder_path+nume_folder
    for file_name in random_music_list():
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
    print("done")


def menu():
    optiune=0
    while optiune!=5:
        menu=(
"""--------------------------------------------  
    1.Create new folder
    2.Move all music from folder
    3.Move only 99 songs in new folder
    4.Order music from selected folder        
    5.Exit
--------------------------------------------""")
        print(menu)
        
        optiune=int(input("Alegeti optiune: "))
        if optiune==1:
            new_folder()
            print("Folder creat cu succes")
        if optiune ==2:
            muta_toate()
            ramase=len(os.listdir(music_folder_path))
            print(f"Muzica mutata cu succes, au mai ramas {ramase} melodii")
        if optiune ==3:
            muta_99()
            ramase=len(os.listdir(music_folder_path))
            print(f"Muzica mutata cu succes, au mai ramas {ramase} melodii")
        if optiune ==4:
            order_songs()
            print("Melodii numerotate cu succes")
        
if __name__ == "__main__":
    menu()

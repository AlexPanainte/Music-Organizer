
import os,random,shutil

music_folder_path="D:/muzicuta/Muzica"
new_folder_path="D:/muzicuta/"

def new_folder():
    nume=input("Adaugati numele folderului: ")
    name=new_folder_path+nume
    os.mkdir(name)

def random_music_list():
    content=os.listdir(music_folder_path)
    random.shuffle(content)
    return content


def list_99():
    count=0
    lista=[]
    for i in random_music_list():
        lista.append(i)
        count+=1
        if count==99:
            random.shuffle(lista)
            return lista
            
def rename_songs(path):
    old_names = random_music_list()
    new_names = []

    for number, name_song in enumerate(old_names):
        new_name = str(number) + "." + name_song
        new_names.append(new_name)

    for i in range(len(old_names)):
        os.rename(path + old_names[i], path + new_names[i]) 

def muta():
    nume_folder=input("Introduceti nume folder:")
    source_folder = "D:/muzicuta/Muzica"
    destination_folder = f"D:/muzicuta/{nume_folder}"
    for file_name in list_99():
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
    print("done")


def menu():
    optiune=0
    while optiune!=3:
        print("""
        1.Create new folder
        2.Move music
        3.Exit""")
        optiune=int(input("Alegeti optiune: "))
        if optiune==1:
            new_folder()
            print("Folder creat cu succes")
        if optiune ==2:
            muta()
            ramase=len(os.listdir("D:/muzicuta/Muzica"))
            print(f"Muzica mutata cu succes, au mai ramas {ramase} melodii")
        

menu()
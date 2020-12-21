from torf import Torrent
import x1337
import requests
import subprocess
import sys
# import pyperclip

title_art = r"""
████████╗░█████╗░██████╗░██████╗░███████╗██╗░░░░░██╗██╗░░██╗  ██████╗░██╗░░░░░██╗░░░██╗░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░░░██║╚██╗██╔╝  ██╔══██╗██║░░░░░██║░░░██║██╔════╝
░░░██║░░░██║░░██║██████╔╝██████╔╝█████╗░░██║░░░░░██║░╚███╔╝░  ██████╔╝██║░░░░░██║░░░██║╚█████╗░
░░░██║░░░██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░░░██║░██╔██╗░  ██╔═══╝░██║░░░░░██║░░░██║░╚═══██╗
░░░██║░░░╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║██╔╝╚██╗  ██║░░░░░███████╗╚██████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚══════╝░╚═════╝░╚═════╝░"""
print(title_art+'\n')


def search(movie_name,hindi,quality):
	
    if not movie_name:
       movie_name = input("Enter the movie name : ")
    print(f'Quality : {quality} Audio : {hindi}')
    print(f"Entered : {movie_name}")
    movie_name = movie_name.lower()
    imdbsuggestion = f'https://v2.sg.media-imdb.com/suggestion/{movie_name[0]}/{movie_name}.json'
    correct_movie_name = requests.get(imdbsuggestion).json()
    movie_name = correct_movie_name['d'][0]['l'] 
    print(f"Searching for {movie_name}")

    if hindi:
       movie_name = movie_name + quality + ' hindi' 
    torrent_results = x1337.search(movie_name,quality)
    seeder = 0
    name = ''
    magnet_link = ''
    for result in torrent_results:
        if result.get('seeder',1) > seeder and quality in result['name']:
            seeder = result.get('seeder',1)
            name = result['name']
            magnet_link = result['magnet']
            type =  result['files']['type']
            files = result['files']['file']
            # pyperclip.copy('1337x.to'+result['url'])
    
    print('Seed:',seeder,' > ',name)

    if type == 'movie':
    	print("Type : Movie")
    	stream(magnet_link)
    elif type == 'show':
    	print("\nSelect Show Episode > \n")
    	for index,file in enumerate(files):
    		print(index+1,' : ',file[index+1])
    	num = str(int(input('Enter no : ')) - 1)
    	stream(magnet_link,num)

def stream(magnet,num = False):
	if num:
		subprocess.call(['webtorrent','--vlc','--select',num,magnet],shell=True)
		return
	subprocess.call(['webtorrent','--vlc',magnet],shell=True)
	
def show(magnet,num):
	subprocess.call(['webtorrent','--vlc','--select',num,magnet],shell=True)
def movie(magnet):
    subprocess.call(['webtorrent','--vlc',magnet],shell=True)

if __name__ == '__main__':
    quality = '720'
    hindi = False
    number = 0
    for num,con in enumerate(sys.argv):
        if '-h' in con:
            number -= 1
            hindi = True

        if '-1080' in con:
            quality = '1080'
            number -= 1
    else:
        if number == 0:
            keyword = ' '.join(sys.argv[1:])
        else:
            keyword = ' '.join(sys.argv[1:number])

    search(keyword,hindi,quality)
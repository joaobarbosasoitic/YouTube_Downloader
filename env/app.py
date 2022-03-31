#-*- coding: utf-8 -*-


from pytube import YouTube
from pytube import Playlist
from pytube import Channel


def SingleVideoDownload(link):
    try:
        yt = YouTube(link)
        print('Baixando Video...')
        yt.streams.first().download('Download_video/')
        print('------ Download Concluido ------')
    except Exception as e:
        print('Erro ao efetuar o download\n', e)

def ChannelDownload(link):
    try:
        c = Channel(link)
        print(f'Baixando Canal: {c.channel_name}')
        for video in c.videos:
            print(f"Baixando video: {video.title}")
            video.streams.first().download('Download_Lista/')
            print('------ Download Concluido ------')
        print('Download efetuado com sucesso!')
    except Exception as e:
        print('Erro ao efetuar o download\n', e)

def PlaylistDownload(link):
    try:
        p = Playlist(link)
        print(f'baixando playlist {p.title}')
        for video in p.videos:
            print(f"Baixando video: {video.title}")
            video.streams.first().download('Download_Canal/') 
            print('------ Download Concluido ------')
        print('Download efetuado com sucesso!')
    except Exception as e:
        print('Erro ao efetuar o download\n', e)


print('Digite 1 para baixar um único video')
print('Digite 2 para baixar uma Lista de Reprodução')
print('Digite 3 para baixar o canal inteiro')
print()

op = input("Digite a opção: ")

try:
    if int(op) == 1:
        link = input("Digite o link do video: ")
        SingleVideoDownload(link)
    elif int(op) == 2:
        link = input("Digite o link da Lista de Reprodução: ")
        PlaylistDownload(link)
    elif int(op) == 3:
        link = input("Digite o link do canal: ")
        ChannelDownload(link)
except Exception as e:
    print('Comando não reconhecido\n', e)
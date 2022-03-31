#-*- coding: utf-8 -*-

from time import sleep
from pytube import YouTube
from pytube import Playlist
from pytube import Channel


def SingleVideoDownload(link):
    try:
        yt = YouTube(link)
        print('Baixando Video...')
        yt.streams.first().download('Download_video/')
        print('------ Download Concluido ------')
        sleep(1000)
    except Exception as e:
        print('Erro ao efetuar o download\n', e)


def PlaylistDownload(link):
    try:
        p = Playlist(link)
        print(f'baixando playlist {p.title}')
        for video in p.videos:
            print(f"Baixando video: {video.title}")
            video.streams.first().download(f'{p.title}/') 
            print('------ Download Concluido ------')
        print('Download efetuado com sucesso!')
        sleep(1000)
    except Exception as e:
        print('Erro ao efetuar o download\n', e)

def ChannelDownload(link):
    try:
        c = Channel(link)
        print(f'Baixando Canal: {c.channel_name}')
        for video in c.videos:
            print(f"Baixando video: {video.title}")
            video.streams.first().download(f'{c.channel_name}/')
            print('------ Download Concluido ------')
        print('Download efetuado com sucesso!')
        sleep(1000)
        
    except Exception as e:
        print('Erro ao efetuar o download\n', e)


print('[1] para baixar um único video\n[2] para baixar uma Lista de Reprodução\n[3] para baixar o canal inteiro')
print()

op = input("Digite a opção: ")

if int(op) == 1:
    try:
        link = input("Digite o link do video: ")
        SingleVideoDownload(link)
    except Exception as e:
        print('Comando não reconhecido\n', e)

elif int(op) == 2:
    try:
        link = input("Digite o link da Lista de Reprodução: ")
        PlaylistDownload(link)
    except Exception as e:
        print('Comando não reconhecido\n', e)

elif int(op) == 3:
    try:
        link = input("Digite o link do canal: ")
        ChannelDownload(link)
    except Exception as e:
     print('Comando não reconhecido\n', e)

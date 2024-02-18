from pytube import YouTube


class Downloader:
    ''' Baixa vídeos e/ou áudios do Yutube '''

    def __init__(self, url) -> None:
        self.url = url
        

    def download_video(self):
        try:
          yt = YouTube(self.url)
          print(f"Baixando o vídeo {yt.title}...")
          yt.streams.get_lowest_resolution().download(output_path = './downloads/videos_completos/')
          print(f"Download completo!")
        except Exception as error:
          print(f'An exception occurred: {error}')


    def download_audio(self):
        try:
          yt = YouTube(self.url)
          print(f"Baixando apenas o áudio de {yt.title}...")
          yt.streams.get_audio_only().download(output_path = './downloads/audios/')
          print(f"Download completo!")

        except Exception as error:
          print(f'An exception occurred: {error}')
        pass


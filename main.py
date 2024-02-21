from downloader import Downloader

def main_cli_program():

    
    print('###### SEJA BEM-VINDO(A) ####### \n')
    print('Selecione 1 para baixar o vídeo\n')
    print('ou\n')
    print('Selecione 2 para baixar o áudio\n')
    
    user_option = input('Digite a opção desejada: ')

    print(f'Você selecionou a opção {user_option} \n')

    video_url = input('Agora insira a url do vídeo que deseja baixar: ')

    download = Downloader(video_url)

    match user_option:
        case '1':
            download.download_video()

        case '2':
            download.download_audio()

main_cli_program()

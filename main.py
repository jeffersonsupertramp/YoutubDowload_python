import flet as ft
from time import sleep
from pytubefix import YouTube
import os
from pytubefix.cli import on_progress


def videod(url, page):
    yt = YouTube(url)
    print(yt.title)
    ys = yt.streams.get_highest_resolution()
    try:
        ys.download()
        
        dlg = ft.AlertDialog(
        title=ft.Text(f"{yt.title} has been successfully downloaded."))
        page.open(dlg)
    
    except Exception as e:
        #print(f"Error downloading video: {e}")
        #testando
         dlg = ft.AlertDialog(
         title=ft.Text(ft.Text("Error downloading video. Please check the URL and try again.")))
         page.open(dlg)
       

def mp3d(url, page):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
   
    destination = '.'
    try:
        out_file = video.download(output_path=destination)
        
        # Check for existing file names and rename if necessary
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        counter = 1
        while os.path.exists(new_file):
            new_file = f"{base}_{counter}.mp3"
            counter += 1

        os.rename(out_file, new_file)
        # result of success
        print(f"{yt.title} has been successfully downloaded.")
        dlg = ft.AlertDialog(
        title=ft.Text(f"{yt.title} has been successfully downloaded."))
        page.open(dlg)
       #on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    
        
        page.update()
    except Exception as e:
        print(f"Error downloading audio: {e}")
        dlg = ft.AlertDialog(
        title=ft.Text(ft.Text("Error downloading audio. Please check the URL and try again.")))
        page.open(dlg)
       


def main(page: ft.Page):
    page.title = "J3FF"
    page.bgcolor = ft.colors.BLACK
    page.title = "J3FF"
    pb = ft.ProgressBar
    page.padding = ft.padding.all(100)
   
    # texto Principal Titulo
    t1 = ft.Text(value="INSIRA SUA URL PARA COMEÇAR", theme_style=ft.TextThemeStyle.DISPLAY_LARGE)

    # Imputs
    url = ft.TextField(
        label="Cole aqui seu link",
        width=600,
        border_color=ft.colors.BLUE_300
    )
    t2 = ft.Text("Escolha o formato")

    escolha = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="mp3", label="Música"),
            ft.Radio(value="mp4", label="Video"), ])
    )

    t = ft.Text()

    def button_clicked(e):

        if url.value =="":
            dlg = ft.AlertDialog(
            title=ft.Text("Digite uma url para baixar"))
            page.open(dlg)
        elif escolha.value == "mp4":
            videod(url.value, page)
            
            url.value = ""
            page.update()
        else:
            mp3d(url.value, page)
            url.value = ""
            page.update()

    color_button = ft.ElevatedButton(
        text="Baixar",
        on_click=button_clicked
    )

    page.add(
        t1,
        ft.Column(
            controls=[
                url, t2, escolha, t, color_button,ft.Image(src="logo.jpg")
            ]),
    )

ft.app(target=main)

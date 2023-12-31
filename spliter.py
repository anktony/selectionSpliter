from pydub import AudioSegment
import subprocess
import os

def convert_to_mp3(input_file, output_file):
    subprocess.run(['ffmpeg', '-i', input_file, output_file])

def split_and_convert(input_file, split_points):
    audio = AudioSegment.from_file(input_file, format="aac")

    for index, (start_time, end_time, output_name) in enumerate(split_points, start=1):
        start_ms = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(":"))) * 1000
        end_ms = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(":"))) * 1000

        segment = audio[start_ms:end_ms]
        output_name_mp3 = "selecao/" + f"{index:02d} {os.path.splitext(output_name)[0]}.mp3"
        segment.export(output_name_mp3, format="mp3")
        print(f"Converted {output_name} to {output_name_mp3}")

if __name__ == "__main__":
    input_file = "ezCXSKZb5hNn.128.aac"

    split_points = [
        ("00:00:00", "00:02:10", "defumador.aac"),
        ("00:02:17", "00:05:42", "defuma.aac"),
        ("00:06:00", "00:08:13", "eu entrei num estudo.aac"),
        ("00:08:14", "00:10:50", "o bálsamo do céu.aac"),
        ("00:10:56", "00:15:05", "eu canto aqui na terra.aac"),
        ("00:15:14", "00:18:26", "meu beija flor o sol raiou.aac"),
        ("00:18:27", "00:21:06", "as sete cruzes de são miguel.aac"),
        ("00:21:15", "00:24:25", "da terra ao astral.aac"),
        ("00:24:30", "00:25:55", "vem chegando.aac"),
        ("00:25:55", "00:28:40", "O anjo de Deus.aac"),
        ("00:28:40", "00:31:17", "sou guia de muitos anjinhos.aac"),
        ("00:31:18", "00:35:25", "eu peço a meu são miguel.aac"),
        ("00:35:38", "00:38:46", "porteira do beija-flor.aac"),
        ("00:38:47", "00:40:32", "santo graal.aac"),
        ("00:40:33", "00:44:20", "Ogum em seu cavalo.aac"),
        ("00:44:21", "00:48:16", "cavalo branco.aac"),
        ("00:48:16", "00:51:30", "visão do apocalipse.aac"),
        ("00:51:33", "00:55:00", "porteiro tranca-ruas.aac"),
        ("00:55:00", "00:58:03", "senhoras e senhoritas.aac"),
        ("00:58:06", "01:01:17", "foi no clarão da lua.aac"),
        ("01:01:36", "01:03:58", "aliança.aac"),
        ("01:04:06", "01:08:17", "corta demanda.aac"),
        ("01:08:31", "01:10:54", "sete trancas.aac"),
        ("01:10:55", "01:13:55", "limpa a casa para trabalhar.aac"),
        ("01:13:55", "01:15:21", "Eu chamo exu caveira.aac"),
        ("01:15:23", "01:17:45", "Exu mirim.aac"),
        ("01:17:50", "01:21:07", "um bom amigo.aac"),
        ("01:21:08", "01:23:21", "meu camarada.aac"),
        ("01:23:32", "01:27:27", "padilha vem vencer demanda.aac"),
        ("01:27:29", "01:30:02", "o sino da igrejinha.aac"),
        ("01:30:05", "01:32:25", "O luar, ô luar.aac"),
        ("01:32:25", "01:34:34", "ogum mandou louvar exu.aac"),
        ("01:34:34", "01:35:58", "a sua casa não tem parede.aac"),
        ("01:35:58", "01:37:17", "sete cores.aac"),
        ("01:37:18", "01:39:59", "deu meia noite.aac"),
        ("01:40:01", "01:41:48", "vinha caminhando a pé.aac"),
        ("01:41:48", "01:43:45", "amei alguém.aac"),
        ("01:43:55", "01:45:32", "pombagira da praia.aac"),
        ("01:46:10", "01:49:20", "oi... como vai.aac"),
        ("01:50:35", "01:53:52", "Senhora da paz.aac"),
        ("01:54:07", "01:57:18", "Oke Arô.aac"),
        ("01:57:19", "02:02:30", "Santa Jurema.aac"),
        ("02:02:30", "02:05:37", "Tupinambá.aac"),
        ("02:05:37", "02:09:00", "dentro das matas.aac"),
        ("02:09:00", "02:11:08", "cabocla das matas.aac"),
        ("02:11:09", "02:13:06", "oxóssi é rei.aac"),
        ("02:13:06", "02:14:57", "a mata estava escura.aac"),
        ("02:15:00", "02:17:46", "os caboclos desceram do céu.aac"),
        ("02:17:46", "02:20:05", "flecha prateada.aac"),
        ("02:20:09", "02:22:48", "trabalhar com os caboclos.aac"),
        ("02:22:49", "02:23:53", "oxóssi é caçador.aac"),
        ("02:23:53", "02:25:23", "Tupinambá.aac"),
        ("02:25:24", "02:27:47", "Mamãe Jurema.aac"),
        ("02:27:47", "02:28:54", "Foi numa tarde serena.aac"),
        ("02:28:54", "02:30:01", "tava na beira do rio.aac"),
        ("02:30:05", "02:32:17", "vou chamar todos camaradas.aac"),
        ("02:32:32", "02:34:35", "haux com pajé.aac"),
        ("02:34:35", "02:36:57", "na força da mata eu tomo meu rapé.aac"),
        ("02:36:57", "02:39:22", "tomo meu rapé.aac"),
        ("02:39:28", "02:40:59", "preto velho.aac"),
        ("02:40:59", "02:43:52", "maria preta velha.aac"),
        ("02:43:54", "02:46:17", "rosa do amor.aac"),
        ("02:47:51", "02:51:01", "ja vai vovó.aac"),
        ("02:51:39", "02:54:54", "abençoa os pequeninos.aac"),
        ("02:54:58", "02:58:15", "roda dos meninos.aac"),
        ("02:58:16", "02:59:36", "estrelinha.aac"),
        ("03:00:00", "03:03:01", "maninhos e maninhas.aac"),
        ("03:03:01", "03:07:12", "ouvir o mestre.aac"),
        ("03:07:12", "03:09:40", "flores de obaluaê.aac"),
        ("03:09:43", "03:12:08", "a porteira.aac"),
        ("03:12:09", "03:17:21", "força das ondas do mar.aac")
    ]

    split_and_convert(input_file, split_points)
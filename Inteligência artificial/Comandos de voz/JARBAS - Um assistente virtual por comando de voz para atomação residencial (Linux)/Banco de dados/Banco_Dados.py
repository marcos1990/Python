import numpy as np
import os

speaker = input("Digite o nome do voluntário: ")
comandos = ["JARBAS", "LIGUE", "DESLIGUE", "MÚSICA", "SALA", "QUARTO", "COZINHA", "AR-CONDICIONADO", "TV", "CAFE"]
repeticoes = 3

for i in range(0, len(comandos)):
    for rodada in range (0, repeticoes):    #grava os comandos têrs vezes
        print(f"\nDIGA {comandos[i]}...\n")
        
        #arecord -d 10 -r 48000 -c 2 -f S16_LE audio.wav
        #gravar = "arecord -D hw:audiocodec, 0 -f dat -d 2 -c 1 -r 16000"
        #cmd = str(gravar) + str(speaker) + str("-") + str(i) + str ("-") + str(rodada) + str(".wav")
        
        #cmd = 'arecord -D hw:audiocodec,0 -f dat -d 2 -c 1 -r 16000 ' + str(speaker) + str('-') + str(i) + str('-') + str(rodada) + str('.wav')
        #os.system(cmd)
        os.system(f'arecord -D hw:0,0 -f dat -d 2 -c 1 -r 16000 {speaker}-{i}-{rodada}.wav')

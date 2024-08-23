import datetime 
def assistente_virtuale(comando):
    if comando == "qual è la data di oggi?":        
        oggi = datetime.datetime.now()          
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y") +"\n"  
  
    elif comando == "che ore sono?":        
        ora_attuale = datetime.datetime.now().time()          
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M") + "\n"
    
    elif comando == "come ti chiami?":        
        risposta = "Mi chiamo Assistente Virtuale\n" 
   
    else:       
        risposta = "Non ho capito la tua domanda.\n"
      
    print(risposta)

while True:   
    comando_utente = input("Cosa vuoi sapere?\npuoi chiedermi: \n\"Qual è la data di oggi?\"\n\"Che ore sono?\"\n\"Come ti chiami?\"\noppure scrivere \"esci\" per uscire.\nInserisci la tua domanda: ").lower()    
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    else:
        assistente_virtuale(comando_utente)
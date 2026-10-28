import fastf1

session = fastf1.get_session(2021, 7, 'Q') #Caricamento della sessione
print(session.event) #stampo a video con metodo .event

print()
print(session.event["EventName"]) #Stampo il nome dell'evento con oggetto event di panda.Series
print(session.event['EventDate']) #Stampo la data dell'evento con oggetto event di panda.Series

event = fastf1.get_event(2021, 7)
print(event)

#gli eventi e le sessioni si caricano anche tramite nome

event = fastf1.get_event(2021, "Emilia Romagna")
print(event["EventName"])


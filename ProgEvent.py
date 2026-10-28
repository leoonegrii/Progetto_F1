import fastf1

schedule = fastf1.get_event_schedule(2024)

print(schedule)
print()
print(schedule.columns)

"""
#Modalità eventi specifici
print()
gp_12 = schedule.get_event_by_round(12) #creo un oggetto gp_12 e gli assegno l'evento tramite round 
print(gp_12["Country"]) #stampo a video solo il nome dove si svolte tramite metodo pandas

print()
gp_austin = schedule.get_event_by_name("Austin") #stessa cosa di prima ma certo l'evento per nome
print(gp_austin["Country"]) #mi stampa a video il nome della nazione dove si svolge il GP di Austin
"""
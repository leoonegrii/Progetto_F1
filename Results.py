import fastf1

session = fastf1.get_session(2024, 16, 'R') #Caricamento della sessione
session.load()
print(session.results)
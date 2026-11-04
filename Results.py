import fastf1

session = fastf1.get_session(2021, "Franche Grand Prix", 'Q') #Caricamento della sessione
session.load()
#print(session.results)
#print(session.results.columns)
print()
#print(session.results.iloc[0:10].loc[:, ["Abbreviation", "Q3"]])
#print(session.laps)

fastest_lap = session.laps.pick_fastest()
print(fastest_lap["LapTime"])

print(fastest_lap["Driver"])
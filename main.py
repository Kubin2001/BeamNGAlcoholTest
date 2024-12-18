from beamngpy import BeamNGpy, Scenario, Vehicle
'''Nie ograniam jeszcze nic ale przynajmniej działa Uwaga pierwsze ładowanie może potrwać kila minut ale potem już git
 a i jeszcze trzeba zainstalować tą bibliotekę jak macie problemy to piszcie'''



bng = BeamNGpy('localhost', 64256, home='D:\Programy\BeamNG\BeamNG.tech.v0.33.3.0', user='D:\Studia\Programowanie\Python\BeamNG\Dokumentacja')
'''Home czyli tam gdzie macie folder gry nie exe USER bez różnicy chyba tam się tworzą pliki tej symulacji więc zróbicie sobie jakiś folder gdziekolwiek poprostu'''

bng.open()
'''Mapa powinna być łatwa do podmiany na naszą '''
scenario = Scenario('west_coast_usa', 'Alko Google', description="Testowy opis")


vehicle = Vehicle('ego_vehicle', model='etk800', license='AlkoTest')



scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot_quat=(0, 0, 0.3826834, 0.9238795))
scenario.make(bng)

# Load and start our scenario
bng.scenario.load(scenario)
bng.scenario.start()
# Make the vehicle's AI span the map
#vehicle.ai.set_mode('span') # nie ruszac tego jak to odkomentujecie to auto będzie samo jeździć
input('Hit enter when done...')
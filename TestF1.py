import fastf1
import warnings
warnings.filterwarnings('ignore')

session = fastf1.get_session(2021, 7, 'Q')
print(session.event)

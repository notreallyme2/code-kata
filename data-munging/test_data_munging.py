from data_munging import munge

WEATHER_URL = "http://codekata.com/data/04/weather.dat"
FOOTBALL_URL = "http://codekata.com/data/04/football.dat"

def test_munge():
    assert munge(data_url=WEATHER_URL) == None

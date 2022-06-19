from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
    "Philadelphia_Union" : {"name": "Philadelphia Union", "founded": 2008, "owner": "Jay Sugarman"},
    "Inter_Miami_CF" : {"name": "Inter Miami CF", "founded": 2020, "owner": "David Beckham"},
    "Atlanta_United_FC" : {"name": "Atlanta United FC", "founded": 2014, "owner": "Arthur Blank"},
    "LA_Galaxy" : {"name": "LA Galaxy", "founded": 1994, "owner": "Anschutz Entertainment Group"},
    "DC_United" : {"name": "D.C. United", "founded": 1994, "owner": "D.C. United Holdings"},
    "Chicago_Fire_FC" : {"name": "Chicago Fire FC", "founded": 1997, "owner": "Joe Mansueto"},
    "New_York_Red_Bulls" : {"name": "New York Red Bulls", "founded": 1994, "owner": "Red Bull GmbH"},
    "Charlotte_FC" : {"name": "Charlotte FC", "founded": 2019, "owner": "David Tepper"}
}

@app.get('/teams')
def list_teams():
    before_year = request.args.get('before_year') or '30000'
    after_year = request.args.get('after_year') or '0'
    qualifying_data = list(
        filter(
            lambda pl: int(before_year) > pl['founded'] > int(after_year),
            in_memory_datastore.values()
        )
    )
    return {"teams": qualifying_data}

@app.route('/teams/<team_name>')
def get_team(team_name):
    return in_memory_datastore[team_name]
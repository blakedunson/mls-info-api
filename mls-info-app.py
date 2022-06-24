from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
    "Philadelphia_Union" : {"name": "Philadelphia_Union", "founded": 2008, "owner": "Jay Sugarman"},
    "Inter_Miami_CF" : {"name": "Inter_Miami_CF", "founded": 2020, "owner": "David Beckham"},
    "Atlanta_United_FC" : {"name": "Atlanta_United_FC", "founded": 2014, "owner": "Arthur Blank"},
    "LA_Galaxy" : {"name": "LA_Galaxy", "founded": 1994, "owner": "Anschutz Entertainment Group"},
    "DC_United" : {"name": "DC_United", "founded": 1994, "owner": "D.C. United Holdings"},
    "Chicago_Fire_FC" : {"name": "Chicago_Fire_FC", "founded": 1997, "owner": "Joe Mansueto"},
    "New_York_Red_Bulls" : {"name": "New_York_Red_Bulls", "founded": 1994, "owner": "Red Bull GmbH"},
    "Charlotte_FC" : {"name": "Charlotte_FC", "founded": 2019, "owner": "David Tepper"}
}

@app.route('/teams', methods=['GET', 'POST'])
def teams_route():
    if request.method == 'GET':
        return list_teams()
    elif request.method == 'POST':
        return create_team(request.get_json(force=True))

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

def create_team(new_team):
    team_name = new_team['name']
    in_memory_datastore[team_name] = new_team
    return new_team

@app.route('/teams/<team_name>')
def get_team(team_name):
    return in_memory_datastore[team_name]
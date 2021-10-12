from flask import Flask,request
import requests
import json
app = Flask(__name__)

url = requests.get("https://4v9r83qfo4.execute-api.eu-central-1.amazonaws.com/dev")
text = url.text
data=json.loads(text)
#%%
@app.route('/' , methods=['GET'])
def thedata():
    return (data)
@app.route('/scores', methods=['GET'])
def thescores():
    return (data["scores"])
@app.route('/scores/<int:n>', methods=['GET'])
def thescoresn(n):
    scores=list(data['scores'])
    if (n <len(scores)):
        indexn=scores[n]
        scoresn=data['scores'][indexn]
        newlist={
        indexn:scoresn
        }
    return (newlist)
@app.route('/scores', methods=['POST'])
def add_score_post_scores():
    
    key=request.json['key']
    values=request.json['values']
    newlist={
        key:values
        }
    (data['scores'])[key]=values
    return(newlist)

@app.route('/scores/<int:n>', methods=['PUT'])
def add_score_put_scores(n):
    scores=list(data['scores'])
    if n<len(scores):
        add_index=request.json['adding_index']
        add_values=request.json['adding_values']
        if add_index!=scores[n]:
            del data['scores'][scores[n]]
        (data['scores'])[add_index]=add_values
        return(thescores)
            
if __name__ == '__main__':
    app.run()

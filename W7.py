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
        newlist1={
            indexn:scoresn
        }
    return (newlist1)
@app.route('/scores', methods=['POST'])
def add_score_post_scores():
    add_index=request.json['add_index']
    add_values=request.json['add_values']
    newlist2={
        add_index:add_values
    }
    (data['scores'])[add_index]=add_values
    return(newlist2)

@app.route('/scores/<int:n>', methods=['PUT'])
def add_score_put_scores(n):
    scores=list(data['scores'])
    if n<len(scores):
        add_index=request.json['add_index']
        add_values=request.json['add_values']
        if add_index!=scores[n]:
            del data['scores'][scores[n]]
        (data['scores'])[add_index]=add_values
        newlist3={
            add_index:add_values
        }
        return(newlist3)
            
if __name__ == '__main__':
    app.run()

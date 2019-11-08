from flask import Flask, escape, request, jsonify
import json


app = Flask(__name__)

class Tarefas:
    def __init__(self,name,size):
        self.name = name
        self.size = size
    def show(self):
        return [self.name,self.size]



d = {}
t1=Tarefas("tarefinha",1)
d[0]=t1
t1=Tarefas("tarefão",5)
d[1]=t1



@app.route('/Tarefa/',methods=["GET"])
def get():
    dt={}
    for i in d:
        dt[i]=d[i].show()
    return dt

@app.route('/Tarefa/',methods=["POST"])
def post():
    dt = request.form.to_dict(flat=False)
    n=dt["name"][0]
    s=int(dt["size"][0])
    tn=Tarefas(n,s)
    d[max(d.keys())+1]=tn

    r = ['Tarefa adicionada - name:', n, "size:", s]
    r=' '.join(map(str, r))
    return r


@app.route('/Tarefa/<int:tarefa_id>',methods=["GET"])
def get_tarefa(tarefa_id):
    dt={}
    dt[tarefa_id]=d[tarefa_id].show()
    return dt

@app.route('/Tarefa/<int:tarefa_id>',methods=["PUT"])
def update(tarefa_id):
    dt = request.form.to_dict(flat=False)
    n=dt["name"][0]
    s=int(dt["size"][0])
    tn=Tarefas(n,s)
    d[tarefa_id]=tn

    r = ['Tarefa atualizada - name:', n, "size:", s]
    r=' '.join(map(str, r))
    return r

@app.route('/Tarefa/<int:tarefa_id>',methods=["Delete"])
def deletar(tarefa_id):
    d.pop(tarefa_id)

    return "Tarefa deletada!"



@app.route('/he althcheck/',methods=["GET"])
def healthcheck():
    return ""


app.run(debug=True)
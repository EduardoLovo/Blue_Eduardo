from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tarefas= list()

# end-points / rotas

@app.route('/')
def index():
    return render_template('index.html', titulo='Lista', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/new', methods=['POST', 'GET'])
def new():
   if request.method == 'POST': 
      item = request.form['item'] 
      tarefas.append(item)
      return redirect('/') 


@app.route('/clear')
def clear(): 
   itens.clear()
   return redirect('/')


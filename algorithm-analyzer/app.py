from flask import Flask, render_template, request, redirect, url_for, flash
import os
from algorithms.analyzer import analyze_algorithm, compare_algorithms, time_execution , graph_function


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aquí iría la lógica para registrar un usuario
        flash('Usuario registrado exitosamente', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí iría la lógica de autenticación
        return redirect(url_for('analyze'))
    return render_template('login.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        code = request.form['algorithm_code']
        
        try:
            result = analyze_algorithm(code)
            exec_time = time_execution(code)
            graph_url = graph_function("n")  # Por ejemplo, para O(n)

            flash('Análisis completado', 'success')
            return render_template('report.html', result=result, exec_time=exec_time, graph_url=graph_url)

        except ValueError as e:
            flash(str(e), 'danger')
            return render_template('analyze.html')

    return render_template('analyze.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        code1 = request.form['algorithm1']
        code2 = request.form['algorithm2']
        
        try:
            comparison = compare_algorithms(code1, code2)
            flash('Comparación completada', 'success')
            return render_template('compare.html', comparison=comparison)

        except Exception as e:
            flash(f"Error en la comparación: {str(e)}", 'danger')
            return render_template('compare.html')

    return render_template('compare.html')

if __name__ == '__main__':
    app.run(debug=True)

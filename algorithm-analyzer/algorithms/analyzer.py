import time
import ast
import matplotlib.pyplot as plt
import io
import base64

def is_python_code(code):
    """
    Verifica si el código proporcionado está escrito en Python.
    """
    try:
        ast.parse(code)  # Intenta analizar el código para ver si es sintácticamente correcto en Python
        return True
    except SyntaxError:
        return False

def analyze_algorithm(code):
    """
    Analiza el código y genera la función tiempo equivalente.
    Si el código no es Python, se genera un error.
    """
    if not is_python_code(code):
        raise ValueError("Error: El código no pertenece al lenguaje Python.")

    # Simulación del análisis de complejidad (debes implementar la lógica específica)
    return "Complejidad calculada: O(n)"

def time_execution(code):
    """
    Calcula el tiempo de ejecución de un código Python.
    """
    local_vars = {}
    exec_time = None

    try:
        start_time = time.time()
        exec(code, {}, local_vars)  # Ejecuta el código y mide el tiempo
        exec_time = time.time() - start_time
    except Exception as e:
        return f"Error ejecutando el código: {str(e)}"
    
    return exec_time

def graph_function(function, title="Gráfica de la función tiempo"):
    """
    Grafica la función tiempo equivalente utilizando Matplotlib.
    """
    plt.figure(figsize=(6, 4))
    x = list(range(1, 100))  # Valores de entrada para simular n
    y = [eval(function.replace("n", str(i))) for i in x]  # Evalúa la función tiempo

    plt.plot(x, y, label=function)
    plt.xlabel('n')
    plt.ylabel('Tiempo')
    plt.title(title)
    plt.legend()

    # Convierte la gráfica a una imagen en base64 para mostrar en el navegador
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def compare_algorithms(code1, code2):
    """
    Compara dos algoritmos basados en su complejidad y tiempo de ejecución.
    """
    time1 = time_execution(code1)
    time2 = time_execution(code2)

    comparison = f"Algoritmo 1 - Tiempo de ejecución: {time1} segundos\n"
    comparison += f"Algoritmo 2 - Tiempo de ejecución: {time2} segundos\n"
    comparison += "Comparación de tiempos completada."

    return comparison


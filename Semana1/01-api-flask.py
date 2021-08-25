from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos = [{
    "nombre": "Palta fuerte",
    "precio": 5.20
}, {
    "nombre": "Albahaca 100 gr",
    "precio": 0.80
}
] 


@app.route("/")
def inicio():
    return {
        "message":"Bienvenido a mi API",
        "content": {}
    }

@app.route("/productos", methods=['POST', 'GET'])
def gestion_productos():
    print(request.method)

    if request.method == "GET":
        return {
            "message": "Los productos son:",
            "content": productos
        }

    elif request.method == "POST":
        producto = request.get_json()
        productos.append(producto)

        return {
            "message":"Producto creado exitosamente",
            "content": producto
        }, 201

@app.route("/producto/<int:id>", methods=["GET", "PUT", "DELETE"])
def gestion_producto(id):    
    total_productos = len(productos)
    if id < total_productos:
        if request.method == "GET":
            return {
                "message":"",
                "content": productos[id]
            }, 200
        elif request.method == "PUT":
            data = request.get_json()
            productos[id] = data

            return {
                "message":"Producto actualizado exitosamente",
                "content": productos[id]
            }, 201
        elif request.method == "DELETE":
            del productos[id]
            return {
                "content" : None,
                "message": "Producto eliminado exitosamente"
            }
    else:
        return {
            "message":"Producto no existe",
            "content": ""
        },404

    
    
    
   


if __name__ == "__main__":
    app.run(debug=True, port=5000)




from flask import Flask, jsonify, make_response, request
from datetime import date
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# AUTHOR: Jorge Loredo Meléndez
# GET USERS or USER by correo
# Esta función permite el cambio de escena, indicando el nombre de la nueva
# :param: /
# :returns: La información de todos los usuarios 

matrix=[]
boxMatrix=[]

def loadMatrix():
    file1 = open('movement.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        matrix.append(line)

def loadBoxMatrix():
    file1 = open('boxes.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        boxMatrix.append(line)

@app.route("/robots/<robot>", methods=['GET'])
def getUsers(robot):
    row = matrix[int(robot)].split(",")
    x_cor = row[0]
    y_cor = row[1]
    unique_id = row[2]
    cargo = row[3]

    return jsonify({"mensaje":"success", "x_cor": x_cor, "y_cor": y_cor, "unique_id": unique_id, "cargo": cargo})

@app.route("/boxes/<box>", methods=['GET'])
def getBoxes(box):
    row = boxMatrix[int(box)].split(",")
    x_cor = row[0]
    y_cor = row[1]
    binded = row[2]

    return jsonify({"mensaje":"success", "x_cor": x_cor, "y_cor": y_cor, "binded": binded})



if __name__ == '__main__':
    loadMatrix()
    loadBoxMatrix()
    print ("Running API...")
    app.run(host='0.0.0.0', port=10202,debug=True)


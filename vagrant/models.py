import os
import httplib2
import requests
import string
import random
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Computer, ComputerParts

app = Flask(__name__)

engine = create_engine('sqlite:///partsdata.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/computer/<int:computer_id>/parts/JSON')
def computerListJSON(computer_id):
    computer = session.query(Computer).filter_by(id=computer_id).one()
    parts = session.query(ComputerParts).filter_by(
        computer_id=computer_id).all()
    return jsonify(ComputerParts=[i.serialize for i in items])


@app.route('/computer/<int:computer_id>/parts/<int:parts_id>/JSON')
def computerPartsJSON(computer_id, parts_id):
    Computer_Parts = session.query(ComputerParts).filter_by(id=parts_id).one()
    return jsonify(Computer_Parts=Computer_Parts.serialize)


@app.route('/computer/JSON')
def computersJSON():
    computers = session.query(Computer).all()
    return jsonify(computers=[r.serialize for r in computers])


# Show all computers
@app.route('/')
@app.route('/computer/')
def showComputers():
    computers = session.query(Computer).all()
    # return "This page will show all my computers"
    return render_template('restaurants.html', computers=computers)


# Create a new computer
@app.route('/computer/new/', methods=['GET', 'POST'])
def newComputer():
    if request.method == 'POST':
        newComputer = Computer(name=request.form['name'])
        session.add(newComputer)
        session.commit()
        return redirect(url_for('showComputers'))
    else:
        return render_template('newComputer.html')
    # return "This page will be for making a new computer"

# Edit a computer


@app.route('/computer/<int:computer_id>/edit/', methods=['GET', 'POST'])
def editComputer(computer_id):
    editedComputer = session.query(
        Computer).filter_by(id=computer_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedComputer.name = request.form['name']
            return redirect(url_for('showComputers'))
    else:
        return render_template(
            'editComputer.html', computer=editedComputer)

    # return 'This page will be for editing computer %s' % computer_id

# Delete a computer


@app.route('/computer/<int:computer_id>/delete/', methods=['GET', 'POST'])
def deleteComputer(computer_id):
    computerToDelete = session.query(
        Computer).filter_by(id=computer_id).one()
    if request.method == 'POST':
        session.delete(computerToDelete)
        session.commit()
        return redirect(
            url_for('showComputers', computer_id=computer_id))
    else:
        return render_template(
            'deleteComputer.html', computer=computerToDelete)
    # return 'This page will be for deleting computers %s' % computer_id


# Show a computer part
@app.route('/computer/<int:computer_id>/')
@app.route('/computer/<int:computer_id>/parts/')
def showPart(computer_id):
    computer = session.query(Computer).filter_by(id=computer_id).one()
    parts = session.query(ComputerParts).filter_by(
        computer_id=computer_id).all()
    return render_template('menu.html', parts=parts, computer=computer)
    # return 'This page for the parts for computers %s' % computer_id

# Create a new part for the list


@app.route(
    '/computer/<int:conputer_id>/parts/new/', methods=['GET', 'POST'])
def newComputerPart(computer_id):
    if request.method == 'POST':
        newPart = ComputerParts(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'], course=request.form['course'], computer_id=computer_id)
        session.add(newPart)
        session.commit()

        return redirect(url_for('showPart', computer_id=computer_id))
    else:
        return render_template('newmenuitem.html', computer_id=computer_id)

    return render_template('newMenuItem.html', computer=computer)
    # return 'This page is for making a new computer parts for computer %s'
    #% computer_id

# Edit a computer item


@app.route('/computer/<int:computer_id>/parts/<int:parts_id>/edit',
           methods=['GET', 'POST'])
def editComputerPart(computer_id, part_id):
    editedPart = session.query(ComputerParts).filter_by(id=part_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedPart)
        session.commit()
        return redirect(url_for('showParts', computer_id=computer_id))
    else:

        return render_template(
            'editmenuitem.html', computer_id=computer_id, part_id=part_id, part=editedPart)

    # return 'This page is for editing parts %s' % part_id

# Delete a part


@app.route('/computer/<int:computer_id>/parts/<int:parts_id>/delete',
           methods=['GET', 'POST'])
def deleteComputerPart(computer_id, part_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)
    # return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

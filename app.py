from flask import Flask

FAI=Flask(__name__)


@FAI.route('/wish/<name>')
def wish(name):
    return  '<center><h1> Hello {} </h1></center> '.format(name)

if __name__=='__main__':
    FAI.run(debug=True)
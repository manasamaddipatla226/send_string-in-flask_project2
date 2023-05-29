from flask import Flask

FAI=Flask(__name__)

@FAI.route('/basic/<name>')

def basic(name):
    return (f' <h1>hello,how are u {name}</h1>')

if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.1.123')


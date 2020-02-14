from flask import Flask, render_template, request
from album import Album, Image, load
import yolo

app = Flask(__name__)

ALBUM_PATH = './static/album.txt'
try:
    album = load(ALBUM_PATH)
except:
    album = Album()


@app.route('/')
def index():
    return render_template('home.html', title='홈 페이지')


@app.route('/list')
def list():
    return render_template('list.html', images=album.images)


@app.route('/view')
def view():
    img = album.finder[int(request.args.get('id'))]
    return render_template('view.html', img=img)


@app.route('/upload', methods=['POST'])
def upload():
    img = request.files['img']
    title = request.form.get('title')
    algorithm = request.form.get('algorithm')
    filename = algorithm + '_' + img.filename
    pathSaved = './static/' + filename

    img.save(pathSaved)
    if algorithm == 'yolo':
        yolo.detectObject(pathSaved)
    album.add(Image(title, filename))
    album.save(ALBUM_PATH)

    return alertNGo('업로드 완료', '/list')


@app.route('/delete')
def delete():
    album.delete(int(request.args.get('id')))
    album.save(ALBUM_PATH)
    return alertNGo('삭제 완료', '/list')


def alertNGo(msg, href):
    js = f'''
        <script>
            alert('{msg}');
            window.location.href = '{href}';
        </script>
    '''
    return js


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

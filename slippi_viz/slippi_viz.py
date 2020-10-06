#!/usr/bin/python
import os, sys, socket

PY_VER = "38"
APP_URL= "http://127.0.0.1:5000"

#On Windows, make sure necessary Python paths are in PATH
if os.name == 'nt':
  sys.path.append(os.path.expanduser(os.path.join(
    "~","AppData","Roaming","Python",f"Python{PY_VER}","site-packages")))
  flaskpath = os.path.expanduser(os.path.join(
    "~","AppData","Roaming","Python",f"Python{PY_VER}","Scripts"))
  sys.path.append(os.path.expanduser(flaskpath))

from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
from app import create_app, db, generators #, cli
from app.models import User, Replay


app = create_app()
generators.config_generators(app)

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Replay': Replay}

@app.context_processor
def config_var():
    return app.config

if __name__ == "__main__":
  #pyfladesk code inlined here
  class ApplicationThread(QtCore.QThread):
      def __init__(self, application, port=5000):
          super(ApplicationThread, self).__init__()
          self.application = application
          self.port = port

      def __del__(self):
          self.wait()

      def run(self):
          self.application.run(port=self.port, threaded=True)

  class WebPage(QtWebEngineWidgets.QWebEnginePage):
      def __init__(self, root_url):
          super(WebPage, self).__init__()
          self.root_url = root_url

      def home(self):
          self.load(QtCore.QUrl(self.root_url))

      def acceptNavigationRequest(self, url, kind, is_main_frame):
          """Open external links in browser and internal links in the webview"""
          ready_url = url.toEncoded().data().decode()
          is_clicked = kind == self.NavigationTypeLinkClicked
          if is_clicked and self.root_url not in ready_url:
              QtGui.QDesktopServices.openUrl(url)
              return False
          return super(WebPage, self).acceptNavigationRequest(url, kind, is_main_frame)

  def init_gui(application, port=0, width=-1, height=-1,
    window_title="PyFladesk", icon="appicon.png", argv=None):
      if argv is None:
          argv = sys.argv

      if port == 0:
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.bind(('localhost', 0))
          port = sock.getsockname()[1]
          sock.close()

      # Application Level
      qtapp  = QtWidgets.QApplication(argv)
      webapp = ApplicationThread(application, port)
      webapp.start()
      qtapp.aboutToQuit.connect(webapp.terminate)

      # Main Window Level
      window = QtWidgets.QMainWindow()
      if width == -1 or height == -1:
        window.showMaximized() #Maximize window on opening
      else:
        window.resize(width, height)
      window.setWindowTitle(window_title)
      window.setWindowIcon(QtGui.QIcon(icon))

      # WebView Level
      webView = QtWebEngineWidgets.QWebEngineView(window)
      window.setCentralWidget(webView)

      # WebPage Level
      page = WebPage('http://localhost:{}'.format(port))
      page.home()
      webView.setPage(page)

      window.show()
      return qtapp.exec_()

  init_gui(app,window_title=app.config["SITE_NAME"],icon=app.config["SITE_ICON"])

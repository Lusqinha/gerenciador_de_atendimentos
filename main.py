import eel
from sistem.ORM.cliente import *
from sistem.ORM.sistema import *
from sistem.ORM.categoria import *
from sistem.ORM.status import *
from sistem.controller.service import Service


eel.init('web')


eel.start('index.html', size=(800, 600))

# Path: web\index.html
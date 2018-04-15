
from flask import (Flask, request, send_from_directory)
import programs.strandTest as strandTest
# import programs.off as Off
import programs.hue as Hue
# import programs.helpers as helpers
import controller

APP = Flask(__name__, static_folder='client')
STRIP = controller.STRIP

@APP.route("/hue", methods=['GET'])
def hue():
    r = int(request.args.get('r', default=255))
    g = int(request.args.get('g', default=255))
    b = int(request.args.get('b', default=255))

    controller.push([Hue.solid, STRIP, r, g, b])
    return "Color changed"

@APP.route("/program/<string:program>", methods=['GET'])
def genericProgramRoute(program):
    progParams = request.args.getlist('params')
    controller.push([Hue.solid, STRIP] + progParams)
    return "Program running"

# Start the server
if __name__ == "__main__":
    # Start server
    print('Server Started.')
    APP.run(host='0.0.0.0', port=4000)

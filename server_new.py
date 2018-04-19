
from flask import (Flask, request)
import programs.strandTest as strandTest
import programs.off as off
import programs.hue as hue
import controller

APP = Flask(__name__, static_folder='client')
STRIP = controller.STRIP
PROGRAMS = {
    "hue": hue,
    "strandTest": strandTest,
    "off": off
}

@APP.route("/program/<string:program>/<string:pattern>", methods=['POST'])
def genericProgramRoute(program, pattern):
    progParams = request.get_json()
    controller.push([PROGRAMS[program].__dict__.get(pattern), STRIP] + progParams)
    return "Program running"

# Start the server
if __name__ == "__main__":
    # Start server
    print('Server Started.')
    APP.run(host='0.0.0.0', port=4000)

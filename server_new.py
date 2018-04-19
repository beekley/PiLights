
from flask import (Flask, request, send_from_directory)
import programs.strandTest
# import programs.off as Off
import programs.hue
# import programs.helpers as helpers
import controller

APP = Flask(__name__, static_folder='client')
STRIP = controller.STRIP
# PROGRAMS = {
#     "hue": Hue.solid,
#     "rainbow": strandTest.rainbow
# }

@APP.route("/program/<string:program>/<string:pattern>", methods=['POST'])
def genericProgramRoute(program, pattern):
    progParams = request.get_json()
    print(progParams)
    controller.push([programs[program][pattern], STRIP] + progParams)
    return "Program running"

# Start the server
if __name__ == "__main__":
    # Start server
    print('Server Started.')
    APP.run(host='0.0.0.0', port=4000)

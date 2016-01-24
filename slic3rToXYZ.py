import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("gcode")
args = parser.parse_args()

new_filename = args.gcode.split(".")[0] + ".3w"

header_XYZ = "; filename = composition.3w\r\n; machine = daVinciF10\r\n; material = default\r\n; layer_height = 0.2\r\n; fill_density = 0.10\r\n; shells = 3\r\n; speed = 60\r\n; total_layers = 124\r\n; total_filament = 2116.02\r\n; dimension = 51.23:45.21:24.95\r\n; extruder = 1\r\n"

encoded_string = ""
gcode_stripped = ""
line = ""
n = 0
keep_lines = False

with open(args.gcode, "r") as gcode_file:
	for i in gcode_file:
		n += 1
		line = str(i)

		if (line[0:3] == "G21") or (keep_lines):
			gcode_stripped += line
			keep_lines = True


encoded_string = base64.b64encode(bytes(header_XYZ + gcode_stripped,'utf-8'))

# Create encoded output
out_file = open(new_filename,"wb")
out_file.write(encoded_string)
out_file.close()


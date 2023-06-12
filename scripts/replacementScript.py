import os
from os.path import join

# This file is used by the github action to replace the variant files with the
# custom ones created for our board. It was custom made for the runner and will
# not work locally.

os.chdir("/home/runner")

# Location of the variant folder in the platformio installation on the runner machine
FRAMEWORK_DIR = join(".platformio", "packages", "framework-arduino-samd-adafruit", "variants", "feather_m0")

# location of custom variant files in project
VARIANT_DIR = join("work", "iondb", "iondb", "variant")

# Code to remove old files and replace with new ones
variant_c_file_old = join(FRAMEWORK_DIR, "variant.cpp")
variant_h_file_old = join(FRAMEWORK_DIR, "variant.h")

os.remove(variant_c_file_old)
os.remove(variant_h_file_old)

variant_c_file_new = join(VARIANT_DIR, "variant.cpp")
variant_h_file_new = join(VARIANT_DIR, "variant.h")

os.replace(variant_c_file_new, variant_c_file_old)
os.replace(variant_h_file_new, variant_h_file_old)

import configparser

# Paths
INPUT_FILE = "color-matugen.ini"
OUTPUT_FILE = "color.ini"

# Read the hex color file
config = configparser.ConfigParser()
config.read(INPUT_FILE)

# Prepare new config for RGB
rgb_config = configparser.ConfigParser()

for section in config.sections():
    rgb_config.add_section(section)
    for key, hex_value in config[section].items():
        hex_value = hex_value.strip()
        # Convert hex to RGB
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        rgb_config.set(section, key, f"{r},{g},{b}")

# Write RGB colors to new file
with open(OUTPUT_FILE, "w") as f:
    rgb_config.write(f)

print(f"RGB colors written to {OUTPUT_FILE}")


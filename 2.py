import json
import sys
import subprocess

outfile = sys.argv[1]

def convert_to_json(input_file, output_file):
    packages = []
    package_dict = {}
    current_key = None
    current_value = []

    with open(input_file, 'r') as file:
        for line in file:
            # Detect the start of a new package when "Repository" appears
            if line.startswith("Repository") and package_dict:
                # Save the previous package to the list and reset for a new package
                packages.append(package_dict)
                package_dict = {}
                current_key = None
                current_value = []

            # Check if the line starts with a new key (contains colon and starts a new field)
            if ":" in line and not line.startswith(" "):
                if current_key is not None:
                    # Finalize the current key-value pair and add to the dictionary
                    package_dict[current_key] = " ".join(current_value).strip()

                # Start a new key-value pair
                key, value = line.split(":", 1)
                current_key = key.strip()
                current_value = [value.strip()]
            else:
                # If it's a continuation of the current field, append it to the current value
                current_value.append(line.strip())

        # Add the last package after exiting the loop
        if package_dict:
            package_dict[current_key] = " ".join(current_value).strip()
            packages.append(package_dict)

    # Write the list of packages to the JSON file
    with open(output_file, 'w') as json_file:
        json.dump(packages, json_file, indent=2)
    
    print(f"Converted data for multiple packages has been saved to {output_file}")


################################################################################################

print("--------------------------------------------------------------------------------------------")
print("APJ v1.0 (Arch Package JSON)")
print("--------------------------------------------------------------------------------------------")
print("Output File: " + outfile)
print("--------------------------------------------------------------------------------------------")

print("Getting pacage metadata...")

command = "pacman -Slq | xargs -P 20 -I {} pacman -Si {} | awk 'BEGIN{RS=\"\\n\\n\"} {print $0}' > arch_packages_temp.json"
subprocess.run(command, shell=True, check=True)

print("Done!")
print("--------------------------------------------------------------------------------------------")

print("Converting to json...")
convert_to_json("arch_packages_temp.json", outfile)
print("Done!")

print("--------------------------------------------------------------------------------------------")
print("Script Done!")
print("--------------------------------------------------------------------------------------------")

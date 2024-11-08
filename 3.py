import json

def query_package_by_name(json_file, search_term):
    # Load the JSON data from the file
    with open(json_file, 'r') as file:
        packages = json.load(file)
    
    # Search for packages where the name contains the search term (case-insensitive)
    results = [pkg for pkg in packages if search_term.lower() in pkg.get("Name", "").lower()]

    # Display results
    if results:
        print(f"Found {len(results)} package(s) with the name containing '{search_term}':")
        for result in results:
            print(json.dumps(result, indent=4))
    else:
        print(f"No package found with the name containing '{search_term}'.")

# Example usage
query_package_by_name('gg.json', 'Ax')

import requests
from bs4 import BeautifulSoup


flight_url = ''

column_headers = " | Date        | F#   | Origin                       | Destination             | Departure   | Arrival      | Duration      "

# List of airlines matched to their prefix
# Will add more later
airline_mapping = {
    "united": "UAL",
    "southwest": "SWA",
    "delta": "DAL",
    "american airlines": "AAL",
    "qatar airways": "QTR",
    "turkish airlines": "THY",
    "air china": "CCA",
    "china eastern": "CES",
    "emirates": "UAE",
    "alaska airlines": "ASA",
    "china southern airlines": "CSN",
    "jetblue": "JBU",
    "indigo": "IGO",
    "skywest": "SKW",
    "spirit": "NKS",
    "air canada": "ACA",
    "british airways": "BAW",
    "japan airlines": "JAL",
    "air france": "AFR",
    "sichuan airlines": "CSC",
    "frontier": "FFT",
    "lufthansa": "DLH",
    "ethiopian airlines": "ETH",
    "aeroflot": "AFL",
    "allegiant air": "AAY",
    "hainan airlines": "CHH",
    "etihad airways": "ETD",
    "saudia": "SVA",
    "shenzhen airlines": "CSZ",
    "spring airlines": "CQH",
    "westjet": "WJA",
    "copa airlines": "CMP",
    "latam brasil": "TAM",
    "ryanair": "RYR",
    "korean air": "KAL",
    "qantas": "QFA",
    "singapore airlines": "SIA",
    "xiamenair": "CXA",
    "all nippon": "ANA",
    "air new zealand": "ANZ",
    "azul brazilian airlines": "AZU",
    "cathay pacific": "CPA",
    "tui airways": "TOM",
    "aeroméxico": "AMX",
    "avianca": "AVA",
    "republic": "RPA",
    "pegasus airlines": "PGT",
    "virgin australia": "VOZ",
    "gol transportes aereos": "GLO",
    "air india": "AIC",
    "volaris": "VOI",
    "jetstar": "JST",
    "beijing capital airlines": "CBJ",
    "klm": "KLM",
    "china airlines": "CAL",
    "iberia": "IBE",
    "eva air": "EVA",
    "s7 airlines": "SBI",
    "easyjet": "EZY",
    "airasia": "AXM",
    "vivaaerobus": "VIV",
    "flydubai": "FDB",
    "juneyao airlines": "DKH",
    "zhejiang loong": "CDC",
    "egypt air": "MSR",
    "fedex": "FDX",
    "endeavor air": "EDV",
    "lucky air": "LKE",
    "vietjet air": "VJC",
    "aerolineas argentinas": "ARG",
    "porter airlines": "POE",
    "envoy air": "ENY",
    "asiana": "AAR",
    "tap air portugal": "TAP",
    "vietnam airlines": "HVN",
    "el al": "ELY",
    "latam peru": "LPE",
    "latam": "LAN",
    "united parcel service": "UPS",
    "jazz": "JZA",
    "hawaiian airlines": "HAL",
    "west air": "CHB",
    "garuda indonesia": "GIA",
    "rossiya airlines": "SDM",
    "malaysia airlines": "MAS",
    "shanghai airlines": "CSH",
    "lion air": "LNI",
    "sun express": "SXS",
    "air arabia": "ABY",
    "atlas air": "GTI",
    "citilink": "CTV",
    "cebu pacific air": "CEB",
    "9 air": "JYH",
    "ural": "SVR",
    "virgin atlantic": "VIR",
    "philippine air lines": "PAL",
    "oman air": "OMA",
    "china express airlines": "HXA",
    "gulf air": "GFA",
    "air india express": "AXB",
    "ita airways": "ITY",
    "atp": "CXK",
    "jeju air": "JJA",
    "batik air": "BTK",
    "peach aviation": "APJ",
    "swiss": "SWR",
    "royal air maroc": "RAM",
    "china united airlines": "CUA",
    "cargolux airlines international": "CLX",
    "kenya airways": "KQA",
    "breeze airways": "MXY",
    "mesa": "ASH",
    "chengdu airlines": "UEA",
    "scoot": "TGW",
    "tway air": "TWB",
    "netjets aviation": "EJA",
    "super air jet": "SJV",
    "icelandair": "ICE",
    "thai airways": "THA",
    "sun country airlines": "SCX"
}


def flight_id_history(url, user_input):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with class "prettyTable fullWidth tablesaw tablesaw-stack"
    table = soup.find('table', class_='prettyTable fullWidth tablesaw tablesaw-stack')

    # Initialize an empty string to store the stripped data
    stripped = ''

    print(column_headers)

    if table:

        # Find all rows within the table that match the specified class
        rows = table.find_all('tr', class_=['smallActiverow1 rowClickTarget', 'smallActiverow2 rowClickTarget'])

        if rows:
            for row in rows:
                columns = row.find_all('td')  # Find all columns (td elements) within the row

                for column in columns:
                    stripped += " | " + column.text.strip()  # Append stripped text from each column

                stripped += "\n"  # Add a newline after each row for formatting
        else:
            print("No rows found with class 'smallActiverow1 rowClickTarget' or 'smallActiverow2 rowClickTarget")
    else:
        print("No table found with class 'prettyTable fullWidth tablesaw tablesaw-stack'")

    print(stripped)

    # Ask the user if they want to save the output to a text file
    save_to_file = input("Would you like to save the output to a text file? (yes/no): ").strip().lower()

    if save_to_file == "yes":
        # Ask for the filename
        filename = input("Enter the name of the file to save under (without extension): ").strip()

        # Append .txt extension to the filename
        filename = filename + ".txt"

        try:
            with open(filename, 'w') as file:
                file.write("Flight history for: " + user_input)
                file.write("\n")
                file.write("Flightaware URL: " + url)
                file.write("\n")
                file.write(column_headers)
                file.write("\n")
                file.write(stripped)
            print(f"Output successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to {filename}: {e}")


def get_flight_url(airline_mapping):

    # User input is taken for the airline and flight number
    user_input = input("Enter airline and flight number (ex. Ryanair 2642): ")
    user_input = user_input.lower()

    # We check to make sure that the users input included an airline and flight number
    parts = user_input.split()
    if len(parts) < 2:
        raise ValueError("Input format should be 'airline flight_number'")

    # We join all parts except for the last one, assuming this is the flight number
    # This is for situations where the airline has multiple words such as 'Emirates Airline'
    # Flight_number is assigned to the last part of the users input
    airline_name = " ".join(parts[:-1])
    flight_number = parts[-1]

    airline_code = airline_mapping.get(airline_name, None)
    if not airline_code:
        raise ValueError(f"Airline '{airline_name}' not found in the mapping.")

    flight_id = airline_code + flight_number

    try:
        flight_url = f"https://www.flightaware.com/live/flight/{flight_id}/history"
        print("Flightaware URL: ", flight_url)
    except ValueError as e:
        print("Error:", e)

    flight_id_history(flight_url, user_input)


get_flight_url(airline_mapping)


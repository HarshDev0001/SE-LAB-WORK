
def parse_ride_duration(text):
    """
    Converts HH:MM into minutes.
    Returns 0 for invalid inputs.
    """
    if not isinstance(text, str):
        return 0

    try:
        parts = text.strip().split(':')

        if len(parts) != 2:
            return 0

        hours, minutes = map(int, parts)

        if hours < 0 or minutes < 0 or minutes >= 60:
            return 0

        return hours * 60 + minutes

    except (ValueError, TypeError):
        return 0


def format_station_code(code):
    """
    Formats a station code as ZONE-NUMBER.
    Returns INVALID for malformed inputs.
    """
    if not isinstance(code, str):
        return "INVALID"

    code = code.strip().upper()

    if len(code) < 2:
        return "INVALID"

    if not code[0].isalpha() or not code[1:].isdigit():
        return "INVALID"

    return code[0] + '-' + code[1:]


def parse_ride_log(line):
    """
    Parses bike_type,minutes,subscriber.
    Returns a default tuple for invalid inputs.
    """
    if not isinstance(line, str):
        return ("", 0, False)

    parts = line.split(',')

    if len(parts) != 3:
        return ("", 0, False)

    bike_type = parts[0].strip()
    subscriber = parts[2].strip().lower()

    try:
        minutes = int(parts[1].strip())

        if not bike_type or minutes < 0:
            return ("", 0, False)

        if subscriber not in ("yes", "no"):
            return ("", 0, False)

        return bike_type, minutes, subscriber == "yes"

    except (ValueError, TypeError):
        return ("", 0, False)


def main():
    print("==== Running parse_ride_duration ====")
    value = input("Enter a ride duration as HH:MM (e.g. 01:15): ")
    print("Duration in minutes:", parse_ride_duration(value))

    print("\n==== Running format_station_code ====")
    value = input("Enter a station code (e.g. a12): ")
    print("Formatted station code:", format_station_code(value))

    print("\n==== Running parse_ride_log ====")
    value = input("Enter a ride log line as type,minutes,subscriber (e.g. electric,45,yes): ")
    print("Parsed ride log:", parse_ride_log(value))


if __name__ == "__main__":
    main()

from pysyslogclient import SyslogClientRFC3164
from time import sleep
from datetime import datetime, UTC


def main():
    client = SyslogClientRFC3164("127.0.0.1", 514, proto="UCP")
    print("Started Sending Test Logs")
    count = 0
    while True:
        # sleep()
        client.log(f"Test Log {count} - {datetime.now(UTC)}")
        count += 1


if __name__ == "__main__":
    main()

import socket
import argparse

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-dest",
                        help="Destination server to inspect",
                        type=str)
    parser.add_argument("-start",
                        help="Start range of ports",
                        default=1,
                        type=int)
    parser.add_argument("-end",
                        help="End range of ports",
                        default=1024,
                        type=int)
    parser.add_argument("-trueonly",
                        help="",
                        default=False,
                        type=bool)

    args = parser.parse_args(None)
    return args

class server_inspect():

    def __init__(self, dest):
        self.dest  = dest

    def inspect_port(self, start, end):
        for port in range(start, end + 1):
            print('port {0}: {1}'.format(port, self._check_port(port)))

    def _check_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((self.dest, port))
        if result == 0:
            return True
        return False


def main():
    ARGS = get_args()
    server_inspect(ARGS.dest).inspect_port(ARGS.start, ARGS.end)

if __name__ == "__main__":
    main()
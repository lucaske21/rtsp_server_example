import pyrtsp
import sys
def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: python main.py <server_address> <video_file>")
        sys.exit(1)
    server_address = sys.argv[1]
    video_file = sys.argv[2]
    return server_address, video_file

def main():
    server_address, video_file = parse_arguments()
    server_port = 8554

    # Create an RTSP server instance
    server = pyrtsp.RtspServer(server_address, server_port)

    # Add a media stream to the server
    server.add_media_stream(video_file)

    # Start the RTSP server
    server.start()

if __name__ == "__main__":
    main()

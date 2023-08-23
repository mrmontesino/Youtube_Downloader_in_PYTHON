# Import the necessary modules:
from pytube import Playlist, YouTube


def get_playlist_info(playlist_url):
    """
    Retrieve playlist information and return the playlist object, number of videos, and download directory.
    """
    playlist = Playlist(playlist_url)
    num_videos = int(len(playlist.video_urls))
    title = playlist.title
    print(title)

    print(f'Number of videos in playlist: {num_videos}')

    for url in playlist.video_urls:
        print(url)

    print(f'Number of videos in playlist: {num_videos}')

    print(title)
    download_dir = f'C:/Users/mrmon/Downloads/{title}'
    return playlist, num_videos, download_dir, title


def ask_yes_no(question):
    """
    Prompt the user with a yes/no question and return True or False based on their answer.
    """
    while True:
        answer = input(question + ' (y/n): ')
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print('Invalid input. Please enter y or n.')


def download_videos(start, end, enum_var, playlist, num_videos, download_dir):
    """
    Download the videos within the specified range.
    Get the video URL and create a YouTube object.
    Get the highest resolution stream and download the video.
    """

    for i in range(max(start, 1), min(end, num_videos) + 1):
        # Get the video URL and create a YouTube object
        video_url = playlist[i - 1]
        print(f'Downloading video {i}:\n{video_url}')

        yt = YouTube(video_url)
        if enum_var:
            num_prefix_video = str(i) + " "
        else:
            num_prefix_video = str()

        # Get the highest resolution stream and download the video
        streams = yt.streams.filter(resolution='1080p')
        if streams:
            stream = streams.first()
        else:
            print(f'No 1080p stream available for video {i}')
            stream = yt.streams.get_highest_resolution()

        try:
            stream.download(filename_prefix=num_prefix_video, output_path=download_dir)
            print(f'Video {i} downloaded successfully')
        except Exception as e:
            print(f'Error downloading video {i}: {e}')


def main():
    """
    Prompt the user to input the starting and ending video numbers.
    Download the videos within the specified range.
    """

    input_playlist_url = input('Please enter a playlist URL: ')
    start_num = int(input('Enter the starting video number: '))
    end_num = int(input('Enter the ending video number: '))

    playlist, num_videos, download_dir, title = get_playlist_info(input_playlist_url)
    enumerate_var = ask_yes_no('Do you want to enumerate?')

    download_videos(start_num, end_num, enumerate_var, playlist, num_videos, download_dir)
    print(download_dir)
    print('download task finished')



if __name__ == '__main__':
    main()

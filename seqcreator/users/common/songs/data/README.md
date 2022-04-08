In order for the animations in users/common/songs/* to work, the songs in this ./data folder should be copied to the rapsberry pi.
The path on the raspberry pi is defined in the docker-compose file.

Open pathToFile/docker-compose.yaml file.
Look for something like:
    wavplayeralsa:
        volumes:
            - /home/pi/Music:/wav_files
And copy the songs to /home/pi/Music with the .wav extension.


WHAT IS A TINGEL TANGEL

    This is a very simple youtube music downloader. It prompts for the
    URL of a YouTube video or playlist, downloads the videos, extracts
    MP3 files, from where you can then put them on a simple, old
    school MP3 player (Sandisk still sells them).

    This isn't really intended to be used by anyone else, so it
    hardcodes the folder on my share drive where the MP3s go, and only
    works on Windows, because that's what's on the machine this gets
    used on.

    This relies on something called yt-dlp, which is a fork of
    youtube-dl. While yt-dlp does have a library interface, only the
    CLI is properly documented. Fortunately, we can just call the
    main() function and pass in the command line arguments and it all
    works just fine. This makes it feasible (or easier, anyway) to
    package the script up as a single Windows executable.


BUILD

    Work from Windows cmd.exe or PowerShell, NOT from WSL bash.

    To run the script,

        pipenv run python tingeltangel.py

    To build the executable file,

        pipenv run exe


    

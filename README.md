# Music-player
Requirements

-PyGame : Use the package manager pip to install PyGame.

-PIL : Use for imgae procesing tasks(known as pillow).

-pip install pygame

-pip install pillow

This project is designed to manage wallpapers for a music player application. It consists of two folders:

-new: This folder contains gif wallpapers that are used by the main music player application (main.py) to display random wallpapers during playback.

-wallpaper: Users can add jpg images to this folder. The wallpaper_manage.py script is used to automatically convert these jpg images to gif format and transfer them to the "new" folder for use with the music player.

Usage

-Adding New Wallpapers.

-Place your jpg images in the "wallpaper" folder.

-Run the wallpaper_manage.py script to convert the jpg images to gif format and transfer them to the "new" folder.

-Music Player Integration

-The main music player application (main.py) is configured to load random wallpapers from the "new" folder in gif format. This adds a dynamic visual element to the music playback experience.

-Double click the main.py to open the GUI application, then click the load songs button, navigate to the directory where you have saved the mp3's, It will automatically load them. Click the play button or press space to start playing the music and use to the slider to control audio volume

-Left arrow key : play the previous song
-Right arrow key : play the next song
-Space key : Play / Pause Music

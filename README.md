# GPMDP-Linux-Lyrics-Art-Window
A simple GUI for displaying lyrics and artwork for Google Play Music Desktop Player on Linux


![alt text](https://github.com/nkschlos/GPMDP-LInux-Lyrics-Art-Window/blob/master/screenshot.png?raw=true)
Screenshot of the program running with GPMDP

I have been frustrated with the Google Play Desktop Player's current lyrics display which
  * only shows a few lines at a time
  * scrolls at rate defined by the length of the song, so songs with long instrumental breaks screw up the lyrics
  * takes over the window, and forces you to close it to skip songs, search, etc.
  
I would prefer if I could see *static* lyrics for my song, the album artwork that would show in the mini player, and the search bar and song list all at the same time, which was my motivation for writing this

The program queries the json data that GPMDP live-updates for lyrics, song metadata, and album art. It then displays the lyrics in a scrollbar window and the album art

I've designed it to look good with my dark gnome environment, but you can customize it by adjusting the color hex codes. It's also really designed for multiple-monitor users who wish to have a screen completely dedicated to music. By fixing the initial window locations, this ensures that you can set it to always start in a neat configuration.

The lyrics box can be a little finicky graphically, I might update this in the future.
I've also added a google play music icon to the taskbar display so it looks integrated


![alt text](https://github.com/nkschlos/GPMDP-LInux-Lyrics-Art-Window/blob/master/screenshot2.png?raw=true)




I don't claim for this to be stable, fleshed-out, or concise, as I am not really a programmer.
It's a simple tool that I wrote because I wanted it, and you might like it as well.

Enjoy,
Noah Schlossberger
May 2018

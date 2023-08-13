# Kimai Fast

Some utils to control Kimai from an i3 desktop.
Contains three binaries to be symlinked in a location included in `PATH`.

- `kimai-select`: A quick GTK UI to choose an existing activity.
- `kimai-show`: Shows the current activity and the time it has been running for.
- `kimai-stop`: Stops the current activity if any.

Creation of Projects, Activities or Deletion are not implemented yet as these are not so frequent operations, that can be done from the regular Kimai web ui.

The purpose idea is to quickly select and start and activity from the desktop environment, and have the time tracking status displayed all the time.

This is an example of the `kimai-select` GTK ui starting using a keybind.

![Quick activity selection](https://github.com/namelivia/kimai-fast/assets/1571416/550a4f30-163d-4e9a-b356-400546e05fb9)

And here is an example of having `kimai-show` configured with `i3blocks` to appear in the status bar.

![Time tracker in i3blocks](https://github.com/namelivia/kimai-fast/assets/1571416/f1aa4068-254d-4f5a-9387-108026905493)

Finally `kimai-stop` would quickly stop the running activity.

## Requirements

 - Python3

## Installing

To install it, run `sudo ./create_symlinks` and the binaries will be symlinked from `/user/local/bin` so typically you'll be able to just run them from any location. To remove then run `sudo ./remove_symlinks`.

You'll need to create a YML configuration file in `~/.config/kimai-fast/config.yml` with your Kimai user, token and base url like:

```
user: your-user
token: your-token
url: https://your.kimai.url
```

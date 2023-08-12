# Kimai Fast

Some utils to control Kimai from an i3 desktop.
Contains three binaries to be symlinked in a location included in `PATH`.

- `kimai-select`: A quick GTK UI to choose an existing activity.
- `kimai-show`: Shows the current activity and the time it has been running for.
- `kimai-stop`: Stops the current activity if any.

Creation of Projects, Activities or Deletion are not implemented yet as these are not so frequent operations, that can be done from the regular Kimai web ui.

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

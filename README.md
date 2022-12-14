# GIF to Keyframe

A short python script to convert a GIF to a CSS keyframe animation based on box-shadow effects.

## Live Demo:

[Click here to view](https://hatulapro.github.io/gif_to_keyframe/index.html)

## Usage:

1. Edit the contents of `gif_to_keyframe.py` to fit your needs

2. Run the file with python:
    
    Output goes to stdout, so you should probably write it to a file.

    ```console
    $ python gif_to_keyframe.py > your-output-file.css
    ```

3. Import your animation using CSS:

    ```css
    @import url('./your-output-file.css');
    ```

4. use it like any other animation:

    ```css
    .magic {
        animation: magicAnimation 1s steps(1, start);
    }
    ```

   - TIP: use the `steps` function to remove the transition between colors.

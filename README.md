# `Buildout` recipe for configuring `vim` built-in python environment

Author: Ivo Kubjas

License: BSD 2-clause license

## Why?
This recipe was created to allow `vim` autocompletion to work in `buildout`
projects. The `bin/activate_this.py` adds only the paths for the packages
installed in `virtualenv` but the `buildout` eggs could belong to other directories.

## What it does?
`ik.recipe.vimconf` is a `buildout` recipe for configuring the environment for the
built-in python interpretor in `vim`. It does this by outputting a python module
which modifies the system path to contain the installed eggs and project eggs.
Furthermore, it also constructs a local `.vimrc` for the buildout project which
handles all the necessary `vim` configuration.

## Configuration
The `vim` configuration depends on environment variables set by `virtualenv`, so a
`virtualenv` environment must be created and activated for the configuration to
work.

The global `vim` configuration must include
```VimL
if filereadable($VIRTUAL_ENV . '/.vimrc')
    source $VIRTUAL_ENV/.vimrc
endif
```
for the local configuration to be read.

The `buildout` configuration file (usually `buildout.cfg`) should include the
following part:
```ini
[vimconf]
recipe = ik.recipe.vimconf
eggs = 
    ${buildout:project-eggs}
```

The `vimconf` part should be added to `parts` directive in `[buildout]` section
so it would be included while running `bin/buildout`.

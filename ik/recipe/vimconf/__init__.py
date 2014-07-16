import logging
import zc.buildout
import zc.recipe.egg
import os.path


class VimConf(object):
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        self.logger = logging.getLogger(self.name)
        self.egg = zc.recipe.egg.Eggs(buildout, name, options)

    def install(self):
        eggs = self.egg.working_set()

        directory = self.buildout['buildout']['directory']
        bin_dir = self.buildout['buildout']['bin-directory']
        executable = self.buildout['buildout']['executable']
        vim_env_activation = self.options.get('environment', 'vim-activate.py')
        activation_content = vimconf_template.format(
            executable=executable,
            paths="',\n  '".join(eggs[1].entries))
        vimrc_content = vimrc_template.format(
            bin_dir=bin_dir,
            vim_env=vim_env_activation)
        vimrc_location = os.path.join(directory, ".vimrc")
        vimenv_location = os.path.join(bin_dir, vim_env_activation)
        with open(vimenv_location, "w") as f:
            f.write(activation_content)
        with open(vimrc_location, "w") as f:
            f.write(vimrc_content)
        return [vimrc_location, vimenv_location]

    def update(self):
        return self.install()

vimconf_template = \
"""#! {executable}
import sys

sys.path[0:0] = [
  '{paths}',
  ]
"""

vimrc_template = \
"""py << EOF
import os.path
import sys
import vim
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join("{bin_dir}", "{vim_env}")
    execfile(activate_this, dict(__file__=activate_this))
EOF
"""

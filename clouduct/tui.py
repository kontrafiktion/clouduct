#!/usr/bin/env python
"""TextUI for clouduct."""

import boto3
import npyscreen
import os
import textwrap
import itertools


HELP_WIDTH = 40


class SelectOneWithHelp(npyscreen.SelectOne):  # noqa: D101
    """'Option' Group that displays a help text for the group."""

    def __init__(self, *args, **kwargs):  # noqa: D102
        self.helpText = kwargs["helpText"]
        self.values_with_help = kwargs.get("values_with_help", None)
        super().__init__(*args, **kwargs)

    def update(self, clear=True):
        """Update an option and displays the 'help' for that option.

        This is called whenever the cursor moves to the option.
        When the first option is highlighted this is called multiple times,
        but for now this works fin anyway.
        """
        super().update(clear)
        self._show_help()

    def _show_help(self):
        """Show the help in the configured help widget.

        If the widget is not available (because the terminal is width to small: do nothing)
        """
        if self.values_with_help:
            self.parent.set_help(self.helpText + "\n\n" +
                                 self.values_with_help[self.cursor_line]["desc"])
        else:
            self.parent.set_help(self.helpText)


class TitleSelectOneWithHelp(npyscreen.TitleSelectOne):
    """Container with title for 'Option' Group with Help."""

    _entry_type = SelectOneWithHelp


def _wrap(text, length):
    for para in text.split("\n"):
        if len(para) > length:
            for line in textwrap.wrap(para, length):
                yield line
        else:
            yield para


class AwsProfileForm(npyscreen.Form):
    """TextUI Form for clouduct."""

    def __init__(self, env_profile, profiles, *args, **kwargs):
        self.env_profile = env_profile
        self.profiles = profiles
        super().__init__(*args, **kwargs)

    def set_help(self, text):
        """"Display the (wrapped) help text."""
        self.helpWidget.values = list(_wrap(text, self.helpWidget.width - 6))
        self.helpWidget.display()

    def create(self):
        """"Create the TextUI."""
        term_size = os.get_terminal_size()
        self.profile = self.add(TitleSelectOneWithHelp,
                                max_height=3,
                                name='Profile',
                                max_width=term_size.columns - 6 - HELP_WIDTH,
                                values=self.profiles,
                                helpText='Profile Help',
                                value=self.profiles.index(self.env_profile),
                                scroll_exit=True
                                )
        self.templates = self.add(TitleSelectOneWithHelp,
                                  max_height=3,
                                  name='Templates',
                                  helpText="Choose a template",
                                  values_with_help=values1,
                                  max_width=term_size.columns - 6 - HELP_WIDTH,
                                  values=[value["key"] for value in values1],
                                  value=0,
                                  scroll_exit=True
                                  )
        self.helpWidget = self.add(npyscreen.BoxTitle,
                                   name='Help',
                                   editable=False,
                                   width=HELP_WIDTH,
                                   height=term_size.lines - 5,
                                   relx=-HELP_WIDTH - 4,
                                   rely=-(term_size.lines - 2),
                                   values=["Blah-Other"]
                                   )


def aws_function(*args):
    """Central Function to display the UI."""
    session = boto3.session.Session()
    profiles = session.available_profiles
    profile_form = AwsProfileForm(os.environ['AWS_PROFILE'], profiles)
    profile_form.edit()
    return profiles[profile_form.profile.value[0]]

values1 = [{"key": "rest-spring-beanstalk",
            "desc": "Web Service using Spring Boot on Elastic Beanstalk"},
           {"key": "spa-nginx-ec2",
            "desc": "Angular Single Page Application served by nginx on EC2"},
           {"key": "py-flask-passenger-ec2",
            "desc": "Python Flask web app using Passenger on EC2"}
           ]

if __name__ == '__main__':
    print(npyscreen.wrapper_basic(aws_function))
    helpText = "Lorem ipsum dolor sit amet, , AFTER>\n \n<BEFOREsed do eiusmod tempor incididunt"
    result = list(itertools.chain.from_iterable(_wrap(helpText, HELP_WIDTH - 3)))
    print(result)

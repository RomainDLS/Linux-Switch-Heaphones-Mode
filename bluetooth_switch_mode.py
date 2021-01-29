#!/usr/bin/python3

import re
import os

PROFILES = [
    'headset_head_unit',
    'a2dp_sink'
]

if __name__ == "__main__":
    """
    Change PulseAudio card active profile. If profile is set to
    `headset_head_unit`, switch to `a2dp_sink` and vice-versa.
    """

    stream = os.popen('pacmd list-cards')
    output = stream.read()

    for card_str in output.split('index: '):
        # Get info from command result
        card = {
            'id': re.match(r'^([0-9]+)', card_str).group(),
            'is_bluetooth': 'name: <bluez_card.' in card_str,
            'profiles': list(filter(lambda x: f'{x}: ' in card_str, PROFILES)),
            'active_profile': next(iter(re.findall(r'active profile: <(.*)>', card_str)), None)
        }

        if (
            card['is_bluetooth'] and
            card['active_profile'] in PROFILES
        ):
            # Change profile
            next_profile = next(
                filter(lambda p: p != card['active_profile'], card['profiles']))
            action = f"pacmd set-card-profile {card['id']} {next_profile}"
            print(f'run : {action}')
            os.popen(action)

#!/usr/bin/python3

import re
import os

PROFILES = [
    'headset-head-unit-cvsd',
    'a2dp-sink-aptx'
]

if __name__ == "__main__":
    """
    Change Pipewire card active profile. If profile is set to
    `headset_head_unit`, switch to `a2dp_sink` and vice-versa.

    > pactl set-card-profile bluez_card.00_1B_66_82_C3_9D a2dp-sink
    > pactl set-card-profile bluez_card.00_1B_66_82_C3_9D headset-head-unit
    """

    stream = os.popen('pactl list cards')
    output = stream.read()

    for card_str in output.split('\n\n'):
        # Get info from command result
        name = re.search(r'Name: (.+)\n', card_str).groups()[0]
        card = {
            'name': name,
            'is_bluetooth': 'bluez_card' in name,
            'profiles': list(filter(lambda x: f'{x}: ' in card_str, PROFILES)),
            'active_profile': next(iter(re.findall(r'Active Profile: (.*)', card_str)), None)
        }

        if (
            card['is_bluetooth'] and
            card['active_profile'] in PROFILES
        ):
            # Change profile
            next_profile = next(
                filter(lambda p: p != card['active_profile'], card['profiles']))
            action = f"pactl set-card-profile {card['name']} {next_profile}"
            print(f'run : {action}')
            os.popen(action)

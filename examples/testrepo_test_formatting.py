# SPDX-FileCopyrightText: 2019 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT


class PuffDetector:
    def __init__(
        self,
        display,
        min_pressure=1,
        high_pressure=2,
        config_filename="settings.json",
        display_timeout=1,
    ):
        self.display = display
        self.state_display_start = 0
        self.detection_result_str = ""
        self.duration_str = ""
        self.high_pressure = high_pressure
        self.min_pressure = min_pressure
        self.display_timeout = display_timeout
        self.config_filename = config_filename

    def fake(self):
        pass

# AutoTrim
AutoTrim is a command-line Python script that automatically trims ROMs by trimming all trailing instances of the last byte, thus not requiring it to be FF.

Usage: `python autotrim file.bin`

A backup (`file.bin.bak`) is created in case trimming the ROM causes problems.

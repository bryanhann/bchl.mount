#!/usr/bin/env python3
from pathlib import Path
import os
import sys
from pprint import pprint
MOUNTS="/Volumes /media"
MOUNTS=[ Path(path) for path in MOUNTS.split()  ]
MOUNTS=[ path for path in MOUNTS if path.is_dir() ]

def parse(path):
    if path.is_file():
        lines = path.read_text().split('\n')
    else:
        lines = []
    lines = [ xx.strip() for xx in lines ]
    lines = [ xx for xx in lines if not xx.startswith('#') ]
    return lines
class Device:
    def __init__(self, path):
        self._path = Path(path)
        self._reg = path/'.bch.mnt/register'
    def info(self):
        acc=dict()
        for line in parse(self._reg):
            parts=line.strip().split()
            if len(parts) == 4:
                _,_,key,relative_path=parts
                target = f'{self._path}/{relative_path}'
                acc[ key ] = target
        return acc
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self._path}>'
    def display(self):
        pprint( (self, self.info()) )
    def dump(self):
        device_name=self._path.name
        for key,val in self.info().items():
            line=f'DEVICE_{device_name}_{key}={val}'
            print(line)

def devices():
    for mount in MOUNTS:
        for device in mount.glob('*'):
            yield Device(device)


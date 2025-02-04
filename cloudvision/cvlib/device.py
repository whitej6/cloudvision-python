# Copyright (c) 2022 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from typing import Dict, List, Optional

from .exceptions import (
    TagMissingException,
    TagTooManyValuesException
)
from .tags import Tag


class Device:
    '''
    Object to store device information
    - ip:           IP address of device
    - deviceId:     ID of the device
    - deviceMac:    Mac address of the device
    - hostName:     Hostname of the device
    - modelName:    Model name of the device
    '''

    def __init__(self, deviceId: Optional[str] = None,
                 ip: Optional[str] = None,
                 deviceMac: Optional[str] = None,
                 hostName: Optional[str] = None,
                 modelName: Optional[str] = None):
        self.id = deviceId
        self.ip = ip
        self.mac = deviceMac
        self.hostName = hostName
        self.modelName = modelName
        # dict of interface name -> interface
        self._interfaces: Dict = {}

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def getInterfaces(self):
        '''
        Returns a dictionary list of the interfaces assigned to the Device object
        '''
        return self._interfaces.values()

    def getInterface(self, name):
        '''
        Returns a particular named interface from the interfaces assigned to the Device
        object
        '''
        return self._interfaces.get(name)

    def addInterface(self, name: str):
        '''
        addInterface assigns an interface to the Device object
        '''
        intf = self._interfaces.get(name)
        if intf:
            # interface already exists, do a noop
            return
        intf = Interface(name, self)
        self._interfaces[name] = intf

    def getSingleTag(self, ctx, label: str, required: bool = True):
        '''
        Returns a Tag of the label assigned to the device.
        Raises TagTooManyValuesException if there are multiple tags of the label assigned.
        Raises TagMissingException if required is True and the tag is missing.
        Returns None if required is False and the tag is missing.
        '''
        devName = str(self.hostName) if self.hostName else str(self.id)
        values = ctx.tags._getDeviceTags(self.id).get(label)
        if values and len(values) > 1:
            raise TagTooManyValuesException(label, devName, values)
        if required and not values:
            raise TagMissingException(label, devName)
        return Tag(label, values[0]) if values else None

    def getTags(self, ctx, label: str = None):
        '''
        Returns a list of Tags matching the specified label assigned to the device.
        If label is unspecified then it returns all Tags assigned to the device.
        '''
        devTags: List[Tag] = []
        if not (ctxDevTags := ctx.tags._getDeviceTags(self.id)):
            return devTags
        for tagLabel, values in ctxDevTags.items():
            if label and label != tagLabel:
                continue
            for value in values:
                devTags.append(Tag(tagLabel, value))
        return devTags

    def _assignTag(self, ctx, tag: Tag, replaceValue: bool = True):
        '''
        Assign a Tag to a device.
        If replaceValue is True ensures only one value of label is assigned to device.
        '''
        ctx.tags._assignDeviceTag(self.id, tag.label, tag.value, replaceValue)

    def _unassignTag(self, ctx, tag: Tag):
        '''
        Unassign a Tag from a device.
        If tag.value is unspecified unassign all tags of label from device.
        '''
        if tag.value:
            ctx.tags._unassignDeviceTag(self.id, tag.label, tag.value)
        else:
            ctx.tags._unassignDeviceTagLabel(self.id, tag.label)


# Interfaces and devices are defined together to avoid circular imports
class Interface:
    '''
    Object to store interface related information
    - name:     The name of the interface
    - device:   The device that the interface is on
    '''

    def __init__(self, name: str, device: Device):
        self.name = name
        self._device = device
        self._peerInterface = None
        self._peerDevice: Optional[Device] = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def getPeerInterface(self):
        return self._peerInterface

    def getPeerDevice(self):
        return self._peerDevice

    def getDevice(self):
        return self._device

    def setPeerInfo(self, device: Device, interface):
        self._peerInterface = interface
        self._peerDevice = device

    def getPeerInfo(self):
        return self._peerDevice, self._peerInterface

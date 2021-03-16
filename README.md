# Simulation of the proton beam tracker/calorimeter
> This project will have tools to aid a simulation and optimizatin of the proton beam tracker/calorimeter in application for determining the corrections to the proton stopping powers for treatment plannig.


```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


## Prerequisites

To use this package you need to first install:
* [root](https://root.cern/install/) 
* [Gate](http://www.opengatecollaboration.org)
    * I am using a version of Gate I cloned from [their Github](https://github.com/OpenGATE/Gate) page, because the official 9.0 verion has a bug.
* [Geant4](https://geant4.web.cern.ch/support/download)
    * Check the requirements for the correct verion of Geant4 on [OpenGate](http://www.opengatecollaboration.org) page
* [Cmake](https://cmake.org/download/)

## Install

**Not working yet**

~~`pip install gate_simulation`~~

## How to use

Create a sensor:

```python
create_sensor()
```

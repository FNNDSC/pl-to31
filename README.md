# Alignment to31

[![Version](https://img.shields.io/docker/v/fnndsc/pl-to31?sort=semver)](https://hub.docker.com/r/fnndsc/pl-to31)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-to31)](https://github.com/FNNDSC/pl-to31/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-to31/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-to31/actions/workflows/ci.yml)

`pl-to31` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which takes in ...  as input files and
creates ... as output files.

## Abstract

...

## Installation

`pl-to31` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://ipfs.babymri.org/ipfs/QmaQM9dUAYFjLVn3PpNTrpbKVavvSTxNLE5BocRCW1UoXG/light.png)](https://chrisstore.co/plugin/pl-to31)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-to31` as a container:

```shell
singularity exec docker://fnndsc/pl-to31 align_to31 [--args values...] input/ output/
```

To print its available options, run:

```shell
singularity exec docker://fnndsc/pl-to31 align_to31 --help
```

## Examples

`align_to31` requires two positional arguments: a directory containing
input data, and a directory where to create output data.
First, create the input directory and move input data into it.

```shell
mkdir incoming/ outgoing/
mv some.dat other.dat incoming/
singularity exec docker://fnndsc/pl-to31:latest align_to31 [--args] incoming/ outgoing/
```

## Development

Instructions for developers.

### Building

Build a local container image:

```shell
docker build -t localhost/fnndsc/pl-to31 .
```

### Get JSON Representation

Run [`chris_plugin_info`](https://github.com/FNNDSC/chris_plugin#usage)
to produce a JSON description of this plugin, which can be uploaded to a _ChRIS Store_.

```shell
docker run --rm localhost/fnndsc/pl-to31 chris_plugin_info > chris_plugin_info.json
```

### Local Test Run

Mount the source code `align_to31.py` into a container to test changes without rebuild.

```shell
docker run --rm -it --userns=host -u $(id -u):$(id -g) \
    -v $PWD/align_to31.py:/usr/local/lib/python3.10/site-packages/align_to31.py:ro \
    -v $PWD/in:/incoming:ro -v $PWD/out:/outgoing:rw -w /outgoing \
    localhost/fnndsc/pl-to31 align_to31 /incoming /outgoing
```

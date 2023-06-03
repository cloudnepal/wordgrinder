from build.ab2 import (
    Rule,
    Targets,
    normalrule,
)
from os.path import *


@Rule
def windres(self, name, srcs: Targets, deps: Targets = [], label="WINDRES"):
    normalrule(
        replaces=self,
        ins=srcs,
        deps=deps,
        outs=[name + ".o"],
        label=label,
        commands=["$(WINDRES) {ins[0]} {outs[0]}"],
    )


@Rule
def makensis(
    self, name, srcs: Targets, deps: Targets = [], defs={}, label="MAKENSIS"
):
    d = ""
    for k in defs:
        d += f" -d{k}={defs[k]}"

    normalrule(
        replaces=self,
        ins=srcs,
        deps=deps,
        outs=[name + ".o"],
        label=label,
        commands=[
            "$(MAKENSIS) -nocd -v2 " + d + " -dOUTFILE={outs[0]} {ins[0]}"
        ],
    )

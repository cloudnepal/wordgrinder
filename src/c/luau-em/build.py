from build.c import clibrary

clibrary(
    name="luau-em",
    srcs=["./lauxlib.cc"],
    hdrs=["./lauxlib.h"],
    deps=["third_party/luau"],
)

{
    "targets": [{
        "target_name": "testaddon",
        "cflags!": [ "-fno-exceptions" ],
        "cflags_cc!": [ "-fno-exceptions" ],
        "sources": [
            # define here EXTERNAL source code to compile

            # define here INTERNAL source code to compile
            "mod_wrapper/main.cpp",
            "mod_wrapper/src/functionexample.cpp",
            "mod_wrapper/src/classexample.cpp"
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")"
        ],
        'link_settings': {
            'libraries': [
                # define here all external prebuild libraries
                '$(RPI_RGB_MATRIX_LED)/mod_external/lib/actualclass.o',
            ],
        },
        'libraries': [
        ],
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")"
        ],
        'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }]
}
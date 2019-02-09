{
    "targets": [{
        "target_name": "rpi_rgb_led_matrix_nodejs",
        "cflags!": [ "-fno-exceptions" ],
        "cflags_cc!": [ "-fno-exceptions" ],
        "sources": [
            # define here EXTERNAL source code to compile

            # define here INTERNAL source code to compile
            "mod_wrapper/main.cpp",
            #"mod_external/src/actualclass.cc",
            "mod_wrapper/src/functionexample.cpp",
            "mod_wrapper/src/classexample.cpp"
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")"
        ],
        'link_settings': {
            'libraries': [
                # define here all external prebuild libraries
                #'$(RPI_RGB_MATRIX_LED)/mod_external/lib/actualclass.o',
                '$(RPI_RGB_MATRIX_LED)/lib/actualclass.o',
                '$(RPI_RGB_MATRIX_LED)/lib/bdf-font.o',
                '$(RPI_RGB_MATRIX_LED)/lib/content-streamer.o',
                '$(RPI_RGB_MATRIX_LED)/lib/framebuffer.o',
                '$(RPI_RGB_MATRIX_LED)/lib/gpio.o',
                '$(RPI_RGB_MATRIX_LED)/lib/graphics.o',
                '$(RPI_RGB_MATRIX_LED)/lib/hardware-mapping.o',
                '$(RPI_RGB_MATRIX_LED)/lib/led-matrix-c.o',
                '$(RPI_RGB_MATRIX_LED)/lib/led-matrix.o',
                '$(RPI_RGB_MATRIX_LED)/lib/multiplex-mappers.o',
                '$(RPI_RGB_MATRIX_LED)/lib/options-initialize.o',
                '$(RPI_RGB_MATRIX_LED)/lib/pixel-mapper.o',
                '$(RPI_RGB_MATRIX_LED)/lib/thread.o',
                '$(RPI_RGB_MATRIX_LED)/lib/transformer.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/c-example.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/clock.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/demo-main.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/input-example.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/ledcat.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/minimal-example.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/scrolling-text-example.o',
                '$(RPI_RGB_MATRIX_LED)/examples-api-use/text-example.o',
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
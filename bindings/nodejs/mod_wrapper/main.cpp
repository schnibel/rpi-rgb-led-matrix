/* cppsrc/main.cpp */
#include <napi.h>
#include "src/functionexample.h"
#include "src/classexample.h"

Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
    
    functionexample::Init(env, exports);
    ClassExample::Init(env, exports);
    return exports;
}

/**
* This code defines the entry-point for the Node addon, it tells Node where to go
* once the library has been loaded into active memory. The first argument must
* match the "target" in our *binding.gyp*. Using NODE_GYP_MODULE_NAME ensures
* that the argument will be correct, as long as the module is built with
* node-gyp (which is the usual way of building modules). The second argument
* points to the function to invoke. The function must not be namespaced.
*/
//NODE_API_MODULE(testaddon, InitAll)
NODE_API_MODULE(NODE_GYP_MODULE_NAME, InitAll);
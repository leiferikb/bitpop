# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'target_defaults': {
    'conditions': [
      ['mojo_shell_debug_url != ""', {
        'defines': [
          'MOJO_SHELL_DEBUG=1',
          'MOJO_SHELL_DEBUG_URL="<(mojo_shell_debug_url)"',
         ],
      }],
    ],
  },
  'variables': {
    'chromium_code': 1,
    'mojo_shell_debug_url%': "",
  },
  'includes': [
    'mojo_apps.gypi',
    'mojo_examples.gypi',
    'mojo_public.gypi',
    'mojo_services.gypi',
  ],
  'targets': [
    {
      'target_name': 'mojo',
      'type': 'none',
      'dependencies': [
        'mojo_apps_js_unittests',
        'mojo_compositor_app',
        'mojo_common_lib',
        'mojo_common_unittests',
        'mojo_cpp_bindings',
        'mojo_js',
        'mojo_js_bindings',
        'mojo_js_unittests',
        'mojo_message_generator',
        'mojo_native_viewport_service',
        'mojo_pepper_container_app',
        'mojo_public_test_utils',
        'mojo_public_bindings_unittests',
        'mojo_public_environment_unittests',
        'mojo_public_system_perftests',
        'mojo_public_system_unittests',
        'mojo_public_utility_unittests',
        'mojo_sample_app',
        'mojo_service_manager',
        'mojo_service_manager_unittests',
        'mojo_shell',
        'mojo_shell_lib',
        'mojo_system',
        'mojo_system_impl',
        'mojo_system_unittests',
        'mojo_utility',
        'mojo_view_manager_lib',
        'mojo_view_manager_lib_unittests',
      ],
      'conditions': [
        ['use_aura==1', {
          'dependencies': [
            'mojo_aura_demo',
            'mojo_launcher',
            'mojo_sample_view_manager_app',
            'mojo_view_manager',
            'mojo_view_manager_unittests',
          ],
        }],
        ['OS == "android"', {
          'dependencies': [
            'mojo_public_java',
            'mojo_system_java',
            'libmojo_system_java',
            'mojo_test_apk',
          ],
        }],
        ['OS == "linux"', {
          'dependencies': [
            'mojo_dbus_echo',
            'mojo_dbus_echo_service',
          ],
        }],
      ]
    },
    {
      'target_name': 'mojo_external_service_bindings',
      'type': 'static_library',
      'sources': [
        'shell/external_service.mojom',
      ],
      'variables': {
        'mojom_base_output_dir': 'mojo',
      },
      'includes': [ 'public/tools/bindings/mojom_bindings_generator.gypi' ],
      'export_dependent_settings': [
        'mojo_cpp_bindings',
      ],
      'dependencies': [
        'mojo_cpp_bindings',
      ],
    },
    {
      'target_name': 'mojo_run_all_unittests',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:test_support_base',
        '../testing/gtest.gyp:gtest',
        'mojo_system_impl',
        'mojo_test_support',
        'mojo_test_support_impl',
      ],
      'sources': [
        'common/test/run_all_unittests.cc',
      ],
    },
    {
      'target_name': 'mojo_run_all_perftests',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:test_support_base',
        'mojo_system_impl',
        'mojo_test_support',
        'mojo_test_support_impl',
      ],
      'sources': [
        'common/test/run_all_perftests.cc',
      ],
    },
    {
      'target_name': 'mojo_system_impl',
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
      ],
      'defines': [
        'MOJO_SYSTEM_IMPL_IMPLEMENTATION',
        'MOJO_SYSTEM_IMPLEMENTATION',
        'MOJO_USE_SYSTEM_IMPL',
      ],
      'sources': [
        'embedder/embedder.cc',
        'embedder/embedder.h',
        'embedder/platform_channel_pair.cc',
        'embedder/platform_channel_pair.h',
        'embedder/platform_channel_pair_posix.cc',
        'embedder/platform_channel_pair_win.cc',
        'embedder/platform_channel_utils_posix.cc',
        'embedder/platform_channel_utils_posix.h',
        'embedder/platform_handle.cc',
        'embedder/platform_handle.h',
        'embedder/scoped_platform_handle.h',
        'system/channel.cc',
        'system/channel.h',
        'system/constants.h',
        'system/core.cc',
        'system/core.h',
        'system/data_pipe.cc',
        'system/data_pipe.h',
        'system/data_pipe_consumer_dispatcher.cc',
        'system/data_pipe_consumer_dispatcher.h',
        'system/data_pipe_producer_dispatcher.cc',
        'system/data_pipe_producer_dispatcher.h',
        'system/dispatcher.cc',
        'system/dispatcher.h',
        'system/entrypoints.cc',
        'system/handle_table.cc',
        'system/handle_table.h',
        'system/local_data_pipe.cc',
        'system/local_data_pipe.h',
        'system/local_message_pipe_endpoint.cc',
        'system/local_message_pipe_endpoint.h',
        'system/mapping_table.cc',
        'system/mapping_table.h',
        'system/memory.cc',
        'system/memory.h',
        'system/message_in_transit.cc',
        'system/message_in_transit.h',
        'system/message_in_transit_queue.cc',
        'system/message_in_transit_queue.h',
        'system/message_pipe.cc',
        'system/message_pipe.h',
        'system/message_pipe_dispatcher.cc',
        'system/message_pipe_dispatcher.h',
        'system/message_pipe_endpoint.cc',
        'system/message_pipe_endpoint.h',
        'system/proxy_message_pipe_endpoint.cc',
        'system/proxy_message_pipe_endpoint.h',
        'system/raw_channel.cc',
        'system/raw_channel.h',
        'system/raw_channel_posix.cc',
        'system/raw_channel_win.cc',
        'system/raw_shared_buffer.cc',
        'system/raw_shared_buffer.h',
        'system/raw_shared_buffer_posix.cc',
        'system/raw_shared_buffer_win.cc',
        'system/shared_buffer_dispatcher.cc',
        'system/shared_buffer_dispatcher.h',
        'system/simple_dispatcher.cc',
        'system/simple_dispatcher.h',
        'system/transport_data.cc',
        'system/transport_data.h',
        'system/waiter.cc',
        'system/waiter.h',
        'system/waiter_list.cc',
        'system/waiter_list.h',
        # Test-only code:
        # TODO(vtl): It's a little unfortunate that these end up in the same
        # component as non-test-only code. In the static build, this code should
        # hopefully be dead-stripped.
        'embedder/test_embedder.cc',
        'embedder/test_embedder.h',
      ],
      'all_dependent_settings': {
        # Ensures that dependent projects import the core functions on Windows.
        'defines': ['MOJO_USE_SYSTEM_IMPL'],
      }
    },
    {
      'target_name': 'mojo_system_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:run_all_unittests',
        '../testing/gtest.gyp:gtest',
        'mojo_common_test_support',
        'mojo_system_impl',
      ],
      'sources': [
        'embedder/embedder_unittest.cc',
        'embedder/platform_channel_pair_posix_unittest.cc',
        'system/channel_unittest.cc',
        'system/core_unittest.cc',
        'system/core_test_base.cc',
        'system/core_test_base.h',
        'system/data_pipe_unittest.cc',
        'system/dispatcher_unittest.cc',
        'system/local_data_pipe_unittest.cc',
        'system/message_pipe_dispatcher_unittest.cc',
        'system/message_pipe_unittest.cc',
        'system/multiprocess_message_pipe_unittest.cc',
        'system/raw_channel_unittest.cc',
        'system/raw_shared_buffer_unittest.cc',
        'system/remote_message_pipe_unittest.cc',
        'system/shared_buffer_dispatcher_unittest.cc',
        'system/simple_dispatcher_unittest.cc',
        'system/test_utils.cc',
        'system/test_utils.h',
        'system/waiter_list_unittest.cc',
        'system/waiter_test_utils.cc',
        'system/waiter_test_utils.h',
        'system/waiter_unittest.cc',
      ],
    },
    {
      'target_name': 'mojo_gles2_impl',
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../gpu/gpu.gyp:command_buffer_client',
        '../gpu/gpu.gyp:command_buffer_common',
        '../gpu/gpu.gyp:gles2_cmd_helper',
        '../gpu/gpu.gyp:gles2_implementation',
        'mojo_gles2',
        'mojo_gles2_bindings',
        'mojo_environment_chromium',
        'mojo_system_impl',
      ],
      'defines': [
        'MOJO_GLES2_IMPL_IMPLEMENTATION',
      ],
      'sources': [
        'gles2/command_buffer_client_impl.cc',
        'gles2/command_buffer_client_impl.h',
        'gles2/gles2_impl_export.h',
        'gles2/gles2_support_impl.cc',
        'gles2/gles2_support_impl.h',
        'gles2/gles2_context.cc',
        'gles2/gles2_context.h',
      ],
    },
    {
      'target_name': 'mojo_test_support_impl',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
      ],
      'sources': [
        'common/test/test_support_impl.cc',
        'common/test/test_support_impl.h',
      ],
    },
    {
      'target_name': 'mojo_common_lib',
      'type': '<(component)',
      'defines': [
        'MOJO_COMMON_IMPLEMENTATION',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_system_impl',
      ],
      'export_dependent_settings': [
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_system_impl',
      ],
      'sources': [
        'common/channel_init.cc',
        'common/channel_init.h',
        'common/common_type_converters.cc',
        'common/common_type_converters.h',
        'common/environment_data.cc',
        'common/environment_data.h',
        'common/handle_watcher.cc',
        'common/handle_watcher.h',
        'common/message_pump_mojo.cc',
        'common/message_pump_mojo.h',
        'common/message_pump_mojo_handler.h',
        'common/time_helper.cc',
        'common/time_helper.h',
      ],
    },
    {
      'target_name': 'mojo_common_test_support',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:test_support_base',
        '../testing/gtest.gyp:gtest',
        'mojo_system_impl',
      ],
      'sources': [
        'common/test/multiprocess_test_helper.cc',
        'common/test/multiprocess_test_helper.h',
        'common/test/test_utils.h',
        'common/test/test_utils_posix.cc',
        'common/test/test_utils_win.cc',
      ],
    },
    {
      'target_name': 'mojo_common_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_message_loop_tests',
        '../testing/gtest.gyp:gtest',
        'mojo_cpp_bindings',
        'mojo_environment_chromium',
        'mojo_common_lib',
        'mojo_common_test_support',
        'mojo_public_test_utils',
        'mojo_run_all_unittests',
      ],
      'sources': [
        'common/common_type_converters_unittest.cc',
        'common/handle_watcher_unittest.cc',
        'common/message_pump_mojo_unittest.cc',
        'common/test/multiprocess_test_helper_unittest.cc',
      ],
    },
    {
      'target_name': 'mojo_environment_chromium',
      'type': 'static_library',
      'dependencies': [
        'mojo_common_lib',
        'mojo_environment_chromium_impl',
      ],
      'sources': [
        'environment/default_async_waiter.cc',
        'environment/buffer_tls.cc',
        'environment/environment.cc',
      ],
      'include_dirs': [
        '..',
      ],
      'export_dependent_settings': [
        'mojo_environment_chromium_impl',
      ],
    },
    {
      'target_name': 'mojo_environment_chromium_impl',
      'type': '<(component)',
      'defines': [
        'MOJO_ENVIRONMENT_IMPL_IMPLEMENTATION',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_common_lib'
      ],
      'sources': [
        'environment/default_async_waiter_impl.cc',
        'environment/default_async_waiter_impl.h',
        'environment/buffer_tls_impl.cc',
        'environment/buffer_tls_impl.h',
      ],
      'include_dirs': [
        '..',
      ],
    },
    {
      'target_name': 'mojo_service_manager',
      'type': '<(component)',
      'defines': [
        'MOJO_SERVICE_MANAGER_IMPLEMENTATION',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../net/net.gyp:net',
        '../url/url.gyp:url_lib',
        'mojo_common_lib',
        'mojo_environment_chromium',
        'mojo_shell_bindings',
        'mojo_system_impl',
      ],
      'sources': [
        'service_manager/background_service_loader.cc',
        'service_manager/background_service_loader.h',
        'service_manager/service_loader.h',
        'service_manager/service_manager.cc',
        'service_manager/service_manager.h',
        'service_manager/service_manager_export.h',
      ],
      'export_dependent_settings': [
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_shell_bindings',
      ],
    },
    {
      'target_name': 'mojo_spy',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_static',
        '../net/net.gyp:http_server',
        '../url/url.gyp:url_lib',
        'mojo_service_manager',
      ],
      'sources': [
        'spy/spy.cc',
        'spy/spy.h',
        'spy/websocket_server.cc',
        'spy/websocket_server.h',
      ],
    },
    {
      'target_name': 'mojo_shell_lib',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_static',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../net/net.gyp:net',
        '../url/url.gyp:url_lib',
        'mojo_external_service_bindings',
        'mojo_gles2_impl',
        'mojo_service_manager',
        'mojo_shell_bindings',
        'mojo_system_impl',
        'mojo_native_viewport_service',
        'mojo_spy',
      ],
      'variables': {
        'mojom_base_output_dir': 'mojo',
      },
      'includes': [ 'public/tools/bindings/mojom_bindings_generator.gypi' ],
      'sources': [
        'shell/app_child_process.cc',
        'shell/app_child_process.h',
        'shell/app_child_process.mojom',
        'shell/app_child_process_host.cc',
        'shell/app_child_process_host.h',
        'shell/child_process.cc',
        'shell/child_process.h',
        'shell/child_process_host.cc',
        'shell/child_process_host.h',
        'shell/context.cc',
        'shell/context.h',
        'shell/dbus_service_loader_linux.cc',
        'shell/dbus_service_loader_linux.h',
        'shell/dynamic_service_loader.cc',
        'shell/dynamic_service_loader.h',
        'shell/dynamic_service_runner.h',
        'shell/init.cc',
        'shell/init.h',
        'shell/in_process_dynamic_service_runner.cc',
        'shell/in_process_dynamic_service_runner.h',
        'shell/keep_alive.cc',
        'shell/keep_alive.h',
        'shell/loader.cc',
        'shell/loader.h',
        'shell/network_delegate.cc',
        'shell/network_delegate.h',
        'shell/out_of_process_dynamic_service_runner.cc',
        'shell/out_of_process_dynamic_service_runner.h',
        'shell/run.cc',
        'shell/run.h',
        'shell/storage.cc',
        'shell/storage.h',
        'shell/switches.cc',
        'shell/switches.h',
        'shell/task_runners.cc',
        'shell/task_runners.h',
        'shell/test_child_process.cc',
        'shell/test_child_process.h',
        'shell/url_request_context_getter.cc',
        'shell/url_request_context_getter.h',
        'shell/view_manager_loader.cc',
        'shell/view_manager_loader.h',
      ],
      'conditions': [
        ['OS=="linux"', {
          'dependencies': [
            '../build/linux/system.gyp:dbus',
            '../dbus/dbus.gyp:dbus',
          ],
        }],
        ['use_aura==1', {
          'dependencies': [
            # These are only necessary as long as we hard code use of ViewManager.
            '../skia/skia.gyp:skia',
            'mojo_gles2',
            'mojo_shell_client',
            'mojo_view_manager',
            'mojo_view_manager_bindings',
          ],
        }, {  # use_aura==0
          'sources!': [
            'shell/view_manager_loader.cc',
            'shell/view_manager_loader.h',
          ],
        }],
      ],
    },
    {
      'target_name': 'mojo_shell_test_support',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_static',
        '../url/url.gyp:url_lib',
        'mojo_service_manager',
        'mojo_shell_lib',
        'mojo_system_impl',
      ],
      'sources': [
        'shell/shell_test_helper.cc',
        'shell/shell_test_helper.h',
      ],
    },
    {
      'target_name': 'mojo_shell',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../ui/gl/gl.gyp:gl',
        '../url/url.gyp:url_lib',
        'mojo_common_lib',
        'mojo_environment_chromium',
        'mojo_service_manager',
        'mojo_shell_lib',
        'mojo_system_impl',
      ],
      'sources': [
        'shell/desktop/mojo_main.cc',
      ],
    },
    {
      'target_name': 'mojo_service_manager_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../testing/gtest.gyp:gtest',
        '../url/url.gyp:url_lib',
        'mojo_common_lib',
        'mojo_cpp_bindings',
        'mojo_environment_chromium',
        'mojo_run_all_unittests',
        'mojo_service_manager',
        'mojo_shell_client',
      ],
      'variables': {
        'mojom_base_output_dir': 'mojo',
      },
      'includes': [ 'public/tools/bindings/mojom_bindings_generator.gypi' ],
      'sources': [
        'service_manager/service_manager_unittest.cc',
        'service_manager/test.mojom',
      ],
    },
    {
      'target_name': 'mojo_js_bindings_lib',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../gin/gin.gyp:gin',
        '../v8/tools/gyp/v8.gyp:v8',
        'mojo_common_lib',
      ],
      'export_dependent_settings': [
        '../base/base.gyp:base',
        '../gin/gin.gyp:gin',
        'mojo_common_lib',
      ],
      'sources': [
        'bindings/js/core.cc',
        'bindings/js/core.h',
        'bindings/js/handle.cc',
        'bindings/js/handle.h',
        'bindings/js/support.cc',
        'bindings/js/support.h',
        'bindings/js/unicode.cc',
        'bindings/js/unicode.h',
        'bindings/js/waiting_callback.cc',
        'bindings/js/waiting_callback.h',
      ],
    },
    {
      'target_name': 'mojo_js_unittests',
      'type': 'executable',
      'dependencies': [
        '../gin/gin.gyp:gin_test',
        'mojo_common_test_support',
        'mojo_js_bindings_lib',
        'mojo_run_all_unittests',
        'mojo_public_test_interfaces',
      ],
      'sources': [
        'bindings/js/run_js_tests.cc',
      ],
    },
    {
      'target_name': 'mojo_message_generator',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../testing/gtest.gyp:gtest',
        'mojo_common_lib',
        'mojo_cpp_bindings',
        'mojo_environment_chromium',
        'mojo_system_impl',
      ],
      'sources': [
        'tools/message_generator.cc',
      ],
    },
    {
      'target_name': 'mojo_cc_support',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../cc/cc.gyp:cc',
        '../skia/skia.gyp:skia',
        '../gpu/gpu.gyp:gles2_implementation',
        'mojo_gles2',
      ],
      'sources': [
        'cc/context_provider_mojo.cc',
        'cc/context_provider_mojo.h',
      ],
    },
  ],
  'conditions': [
    ['OS=="android"', {
      'targets': [
        {
          'target_name': 'mojo_jni_headers',
          'type': 'none',
          'dependencies': [
            'mojo_java_set_jni_headers',
          ],
          'sources': [
            'android/javatests/src/org/chromium/mojo/system/CoreTest.java',
            'android/system/src/org/chromium/mojo/system/CoreImpl.java',
            'services/native_viewport/android/src/org/chromium/mojo/NativeViewportAndroid.java',
            'shell/android/apk/src/org/chromium/mojo_shell_apk/MojoMain.java',
          ],
          'variables': {
            'jni_gen_package': 'mojo',
            'jni_generator_ptr_type': 'long',
         },
          'includes': [ '../build/jni_generator.gypi' ],
        },
        {
          'target_name': 'mojo_system_java',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base_java',
            'mojo_public_java',
          ],
          'variables': {
            'java_in_dir': '<(DEPTH)/mojo/android/system',
          },
          'includes': [ '../build/java.gypi' ],
        },
        {
          'target_name': 'libmojo_system_java',
          'type': 'static_library',
          'dependencies': [
            '../base/base.gyp:base',
            '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
            'mojo_common_lib',
            'mojo_environment_chromium',
            'mojo_jni_headers',
            'mojo_shell_bindings',
            'mojo_shell_lib',
          ],
          'sources': [
            'android/system/core_impl.cc',
            'android/system/core_impl.h',
          ],
        },
        {
          'target_name': 'libmojo_java_unittest',
          'type': 'shared_library',
          'dependencies': [
            '../base/base.gyp:base',
            'libmojo_system_java',
            'mojo_jni_headers',
          ],
          'sources': [
            'android/javatests/core_test.cc',
            'android/javatests/core_test.h',
            'android/javatests/init_library.cc',
          ],
        },
        {
          'target_name': 'mojo_test_apk',
          'type': 'none',
          'dependencies': [
            'mojo_system_java',
            '../base/base.gyp:base_java_test_support',
          ],
          'variables': {
            'apk_name': 'MojoTest',
            'java_in_dir': '<(DEPTH)/mojo/android/javatests',
            'resource_dir': '<(DEPTH)/mojo/android/javatests/apk',
            'native_lib_target': 'libmojo_java_unittest',
            'is_test_apk': 1,
            # Given that this apk tests itself, it needs to bring emma with it
            # when instrumented.
            'conditions': [
              ['emma_coverage != 0', {
                'emma_instrument': 1,
              }],
            ],
          },
          'includes': [ '../build/java_apk.gypi' ],
        },
        {
          'target_name': 'mojo_native_viewport_java',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base_java',
          ],
          'variables': {
            'java_in_dir': '<(DEPTH)/mojo/services/native_viewport/android',
          },
          'includes': [ '../build/java.gypi' ],
        },
        {
          'target_name': 'mojo_java_set_jni_headers',
          'type': 'none',
          'variables': {
            'jni_gen_package': 'mojo',
            'jni_generator_ptr_type': 'long',
            'input_java_class': 'java/util/HashSet.class',
          },
          'includes': [ '../build/jar_file_jni_generator.gypi' ],
        },
        {
          'target_name': 'libmojo_shell',
          'type': 'shared_library',
          'dependencies': [
            '../base/base.gyp:base',
            '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gl/gl.gyp:gl',
            'mojo_common_lib',
            'mojo_environment_chromium',
            'mojo_jni_headers',
            'mojo_shell_bindings',
            'mojo_shell_lib',
          ],
          'sources': [
            'shell/android/library_loader.cc',
            'shell/android/mojo_main.cc',
            'shell/android/mojo_main.h',
          ],
        },
        {
          'target_name': 'mojo_shell_apk',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base_java',
            '../net/net.gyp:net_java',
            'mojo_native_viewport_java',
            'libmojo_shell',
          ],
          'variables': {
            'apk_name': 'MojoShell',
            'java_in_dir': '<(DEPTH)/mojo/shell/android/apk',
            'resource_dir': '<(DEPTH)/mojo/shell/android/apk/res',
            'native_lib_target': 'libmojo_shell',
          },
          'includes': [ '../build/java_apk.gypi' ],
        }
      ],
    }],
    ['OS=="linux"', {
      'targets': [
        {
          'target_name': 'mojo_dbus_service',
          'type': 'static_library',
          'dependencies': [
            '../base/base.gyp:base',
            '../build/linux/system.gyp:dbus',
            '../dbus/dbus.gyp:dbus',
            'mojo_common_lib',
            'mojo_external_service_bindings',
            'mojo_shell_client',
            'mojo_system_impl',
          ],
          'sources': [
            'dbus/dbus_external_service.h',
            'dbus/dbus_external_service.cc',
          ],
        },
      ],
    }],
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'mojo_js_unittests_run',
          'type': 'none',
          'dependencies': [
            'mojo_js_unittests',
          ],
          'includes': [
            '../build/isolate.gypi',
            'mojo_js_unittests.isolate',
          ],
          'sources': [
            'mojo_js_unittests.isolate',
          ],
        },
      ],
    }],
    ['use_aura==1', {
      'targets': [
        {
          'target_name': 'mojo_aura_support',
          'type': 'static_library',
          'dependencies': [
            '../cc/cc.gyp:cc',
            '../ui/aura/aura.gyp:aura',
            '../ui/events/events.gyp:events',
            '../ui/events/events.gyp:events_base',
            '../ui/compositor/compositor.gyp:compositor',
            '../ui/gl/gl.gyp:gl',
            '../webkit/common/gpu/webkit_gpu.gyp:webkit_gpu',
            'mojo_cc_support',
            'mojo_gles2',
            'mojo_native_viewport_bindings',
          ],
          'sources': [
            'aura/context_factory_mojo.cc',
            'aura/context_factory_mojo.h',
            'aura/screen_mojo.cc',
            'aura/screen_mojo.h',
            'aura/window_tree_host_mojo.cc',
            'aura/window_tree_host_mojo.h',
          ],
        },
      ],
    }],
  ],
}
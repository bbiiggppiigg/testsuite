#ifdef __cplusplus
extern "C" {
#endif
#include "../src/mutatee_call_info.h"


mutatee_call_info_t mutatee_funcs[] = {
  {"test_relocations", test_relocations_mutatee, GROUPED, "test_relocations"},
  {"test_module", test_module_mutatee, GROUPED, "test_module"},
  {"test_type_info", test_type_info_mutatee, GROUPED, "test_type_info"},
  {"test_line_info", test_line_info_mutatee, GROUPED, "test_line_info"},
  {"test_local_var_lookup", test_local_var_lookup_mutatee, GROUPED, "test_local_var_lookup"},
  {"test_local_var_locations", test_local_var_locations_mutatee, GROUPED, "test_local_var_locations"},
  {"test_add_symbols", test_add_symbols_mutatee, GROUPED, "test_add_symbols"},
  {"test_lookup_func", test_lookup_func_mutatee, GROUPED, "test_lookup_func"},
  {"test_lookup_var", test_lookup_var_mutatee, GROUPED, "test_lookup_var"}
};

int max_tests = 9;
int runTest[9];
int passedTest[9];
#ifdef __cplusplus
}
#endif

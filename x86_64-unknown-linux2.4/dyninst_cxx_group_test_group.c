#ifdef __cplusplus
extern "C" {
#endif
#include "../src/mutatee_call_info.h"


mutatee_call_info_t mutatee_funcs[] = {
  {"test5_8", test5_8_mutatee, GROUPED, "test5_8"},
  {"test5_5", test5_5_mutatee, GROUPED, "test5_5"},
  {"test5_7", test5_7_mutatee, GROUPED, "test5_7"},
  {"test5_1", test5_1_mutatee, GROUPED, "test5_1"},
  {"test5_3", test5_3_mutatee, GROUPED, "test5_3"},
  {"test5_9", test5_9_mutatee, GROUPED, "test5_9"},
  {"test5_2", test5_2_mutatee, GROUPED, "test5_2"},
  {"test5_4", test5_4_mutatee, GROUPED, "test5_4"}
};

int max_tests = 8;
int runTest[8];
int passedTest[8];
#ifdef __cplusplus
}
#endif

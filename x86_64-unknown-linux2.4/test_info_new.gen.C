/* This file automatically generated from test specifications.  See
    * specification/spec.pl and specification/makemake.py
    */

#include "test_info_new.h"



                static unsigned int test_count = 0;
                static unsigned int group_count = 0;
                static std::vector<RunGroup *> *tests = NULL;

                static void fini_group(RunGroup *rg) {
                    rg->index = group_count++;
                    tests->push_back(rg);
                    test_count = 0;
                }

static void add_test(RunGroup *rg, const char *ts) {
    rg->tests.push_back(new TestInfo(test_count++, ".so", ts));
}

// Now we insert the test lists into the run groups
void initialize_mutatees(std::vector<RunGroup *> &t) {
    tests = &t;
    RunGroup *rg;
  rg = new RunGroup("test_thread_6.dyn_gcc_32_pic_none", 
		DELAYEDATTACH, CREATE, TNone, PNone, 
		local, local, no_launch, 
		DynamicLink, true, PIC, 
		"dyninst", "gcc", "none", "32", "NONE");
  add_test(rg, "{test: test_thread_6, mutator: None, grouped: false, mutatee: test_thread_6}, compiler: gcc}, optimization: none}, run_mode: createProcess}, start_state: delayedattach}}}, abi: 32}, thread_mode: None}, process_mode: None}, format: dynamicMutatee}, mutatorstart: local}, mutateestart: local}, mutateeruntime: no_launch}, pic: pic}, platmode: NONE}");
  fini_group(rg);
}

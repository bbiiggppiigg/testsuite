import os
import tuples
import utils

def print_mutators_list(out, mutator_dict, test_dict, info, platform):
    LibSuffix = platform['filename_conventions']['library_suffix']
    ObjSuffix = platform['filename_conventions']['object_suffix']


    out.write("######################################################################\n")
    out.write("# A list of all the mutators to be compiled\n")
    out.write("######################################################################\n\n")

    module_list = []
    for t in test_dict:
        module_list.append(t['module'])
    module_set = set(module_list)

    for m in module_set:
        out.write("\n")
        out.write("include_directories (\"../src/%s\")\n" % m)
        out.write("set (%s_MUTATORS\n" % (m))
        module_tests = filter(lambda t: m == t['module'], test_dict)
        module_mutators = map(lambda t: t['mutator'], module_tests)
        for t in utils.uniq(module_mutators):
            out.write("\t%s\n" % (t))
        out.write(")\n\n")
        out.write("set (%s_OBJS_ALL_MUTATORS\n" % (m))
        for t in utils.uniq(module_mutators):
            out.write("\t%s%s\n" % (t, ObjSuffix))
        out.write(")\n\n")


        # We're doing this cmake list style, so we need multiple iterations
        # since cmake doesn't support structs
        # Iteration 1: print the list of libraries
        out.write("set (MUTATOR_NAME_LIST\n")
    for m in mutator_dict:
        out.write("\t%s\n" % m['name'])
    out.write("\t)\n\n")

    # Iteration 2: The appropriate module library for each mutator
    out.write("set (MUTATOR_MODULE_LIB_LIST\n")
    for m in mutator_dict:
        # Module info is stored with the "test" dictionary, not the
        # "mutator" dictionary
        tests = filter(lambda t: t['mutator'] == m['name'], test_dict)
        modules = map(lambda t: t['module'], tests)
        if (len(utils.uniq(modules)) != 1):
            print("ERROR: multiple modules for test " + m['name'])
            raise
        module = modules.pop()
        out.write("\ttest%s\n" % module)
        # Keep this so we can provide source directories
        m['module'] = module
    out.write("\t)\n\n")

    # Iteration 3: print the list of sources for these libraries. Sources
    # must be singular (so, really, 'source')
    out.write("set (SRC src)\n")
    out.write("set (MUTATOR_SOURCE_LIST\n")
    for m in mutator_dict:
        if (len(m['sources']) != 1):
            print("ERROR: multiple sources for test " + m['name'])
            raise
        out.write("\t${SRC}/%s/%s\n" % (m['module'], m['sources'][0]))
    out.write("\t)\n\n")

    # Now, iterate over these lists in parallel with a CMake foreach
    # statement to build the add_library directive
    out.write("foreach (val RANGE %d)\n" % (len(list(mutator_dict)) - 1))
    out.write("\tlist (GET MUTATOR_NAME_LIST ${val} lib)\n")
    out.write("\tlist (GET MUTATOR_SOURCE_LIST ${val} source)\n")
    out.write("\tlist (GET MUTATOR_MODULE_LIB_LIST ${val} comp_dep)\n")
    out.write("\tset(SKIP FALSE)\n")
    out.write("\tforeach (dep ${comp_dep})\n")
    out.write("\t\tif(NOT TARGET ${dep})\n")
    out.write("\t\t\tset(SKIP TRUE)\n")
    out.write("\t\tendif()\n")
    out.write("\tendforeach()\n")
    out.write("\tif(NOT SKIP)\n")
    out.write("\t\tadd_library (${lib} ${source})\n")
    out.write("\t\ttarget_link_libraries (${lib} ${comp_dep} ${LIBTESTSUITE})\n")
    out.write("\t\tinstall (TARGETS ${lib} \n")
    out.write("\t\t         RUNTIME DESTINATION ${INSTALL_DIR}\n")
    out.write("\t\t         LIBRARY DESTINATION ${INSTALL_DIR})\n")
    out.write("\tendif()\n")
    out.write("endforeach()\n\n")



def write_mutator_cmakelists(directory, info, platform):
   mutator_dict = info['mutators']
   test_dict = info['tests']
   LibSuffix = platform['filename_conventions']['library_suffix']
   header = """
# This file is automatically generated by the Dyninst testing system.
# For more information, see core/testsuite/src/specification/cmake_mutators.py

"""
   out = open(directory + '/cmake-mutators.txt', "w")
   out.write(header)
   print_mutators_list(out, mutator_dict, test_dict, info, platform)
   out.close()

#

##  setup.py
##  Make  pyd library
##
##  Copyright (c) 2022 WPC Systems Ltd.
##  All rights reserved.

import os
import sys
import sysconfig
import setuptools as sut
import subprocess as spc
import shutil
import Cython.Build as cbuild
import Cython.Distutils as cdutils
sys.path.append('src/')

from WPC_config import PKG_NAME, __version__
from WPC_config import PRODUCT_DICT, EXAMPLE_DICT, LABEL_DICT

################################################################################
## Configuration

SRC_PATH = 'src/'
MERGED_FILE_NAME = f'build/{PKG_NAME}.py'
START_MODULE_NAME = 'WPC_products'
LIB_PATH = f'{PKG_NAME}/'
DOC_PATH = 'docs/'
DIST_PATH = 'dist/'

COMPUTER_NAME = os.environ['COMPUTERNAME']
if COMPUTER_NAME == 'DESKTOP-3JGLNTQ':
    RELEASE_PATH = '../../WPC_Python_driver_release/'
else:
    RELEASE_PATH = '../WPC_Python_driver_release/'

################################################################################
## Merge files

def findKey(line):
    ## Identify end-of-the-line comments
    ## If there are comments, do not search in them
    ind0 = line.find('#')
    if ind0 < 0:
        ind0 = len(line)

    ## Cut the trailing comment & search for "WPC_"
    ind1 = line[:ind0].find('WPC_')
    return ind1

def processLine(line, visited_set, block_cmt=False):
    ## If the line is commented, keep the line.
    line1 = line.lstrip(' \t')
    if len(line1) == 0 or line1[0] == '#':
        return line, block_cmt

    ## Determine if block comment begins or ends
    if len(line1) >= 3 and line1[:3] in ['\"\"\"', '\'\'\'']:
        block_cmt = not block_cmt

    if block_cmt:
        return line, block_cmt

    ## Find "WPC_" which is not in trailing comments
    ind1 = findKey(line)

    ## If there is "WPC_"
    while ind1 >= 0:
        ## Check if the line is an "import" line
        if 'from' in line[:ind1] or 'import' in line[:ind1]:
            ## If yes, we notify that this module should be visited first
            ## by returning "Module: `mod_name`"
            ind2 = line[ind1:].find(' ')
            mod_name = line[ind1:ind2]
            return 'Module: ' + mod_name, block_cmt

        ## If the line is not an "import" line,
        ## remove the module's prefix and the dot.
        ind2 = line[ind1:].find('.')
        mod_name = line[ind1:ind1+ind2]
        line = line.split(mod_name+'.')
        line = ''.join(line)

        ## Finally, update the index by searching for eventually remaining "WPC_"
        ind1 = findKey(line)

    ## In the end, the returned line will be without any WPC modules.
    return line, block_cmt

def parseFile(path, mod_name, out_file, visited_set, verbose=True):
    in_name = path + mod_name + '.py'

    with open(in_name, 'r') as in_file:
        if verbose:
            print('Opened '+in_name)
        block_cmt = False

        for i, line in enumerate(in_file):
            line, block_cmt = processLine(line, visited_set, block_cmt=block_cmt)

            if line[:7] == 'Module:':
                mod_name_2 = line[8:]
                if mod_name_2 not in visited_set:
                    parseFile(path, mod_name_2, out_file, visited_set)
                    out_file.write('\n')
            else:
                out_file.write(line)
        visited_set.add(mod_name)

        if verbose:
            print('Closed '+in_name)

def processSingleSource():
    print()
    print('################################################################################')
    print('## Merge files')
    print()

    os.makedirs(os.path.dirname(MERGED_FILE_NAME), exist_ok=True)
    visited_set = set()
    with open(MERGED_FILE_NAME, 'w') as out_file:
        parseFile(SRC_PATH, START_MODULE_NAME, out_file, visited_set, verbose=True)

################################################################################
## Compile library

## This is for setting the name of compiled library.
class CustomBuilder(cdutils.build_ext):
    def get_ext_filename(self, ext_name):
        file_name = super().get_ext_filename(ext_name)
        ext = os.path.splitext(file_name)[1]
        suffix = sysconfig.get_config_var('EXT_SUFFIX')
        return file_name.replace(suffix, '') + ext

def processLibrary():
    print()
    print('################################################################################')
    print('## Compile library')
    print()

    ## Use the `setup` function in `setuptools` (but check `distutils` for documentation)
    sut.setup(
        name=PKG_NAME,
        version=__version__,
        description='WPC Python device driver',
        cmdclass={"build_ext": CustomBuilder},
        ext_modules=cbuild.cythonize([MERGED_FILE_NAME], language_level='3'),
        options={'build': {'build_lib': LIB_PATH}},
        script_args=['build'],
    )

################################################################################
## Generate documentation

def saveRstProduct(prod_tag, verbose=True):
    path = f'{DOC_PATH}source/products/'
    os.makedirs(path, exist_ok=True)

    prod_name = LABEL_DICT[prod_tag]
    out_name = f'{path}{prod_tag}.rst'

    with open(out_name, 'w') as out_file:
        out_file.write(f'{prod_name}\n')
        out_file.write( '{}\n'.format('='*len(prod_name)))
        out_file.write( '\n')
        out_file.write(f'.. autoclass:: pywpc.{prod_tag}\n')
        out_file.write( '   :members:\n')
        out_file.write( '   :undoc-members:\n')
        out_file.write( '   :inherited-members:\n')

        if verbose:
            print(f'Saved \"{out_name}\"')
    return

def saveRstProductList(verbose=True):
    folder_tag = 'products'
    out_name = f'{DOC_PATH}source/{folder_tag}.rst'

    with open(out_name, 'w') as out_file:
        str_ = LABEL_DICT[folder_tag]
        out_file.write(f'{str_}\n')
        out_file.write( '{}\n'.format('='*len(str_)))

        for prod_category, prod_tag_list in PRODUCT_DICT.items():
            str_ = LABEL_DICT[prod_category]
            out_file.write( '\n')
            out_file.write(f'{str_}\n')
            out_file.write( '{}\n'.format('-'*len(str_)))
            out_file.write( '\n')

            out_file.write(f'.. toctree::\n')
            out_file.write( '   :maxdepth: 4\n')
            out_file.write( '\n')

            for prod_tag in prod_tag_list:
                out_file.write(f'   {folder_tag}/{prod_tag}\n')

        if verbose:
            print(f'Saved \"{out_name}\"')
    return

def saveRstExample(ex_category, ex_tag, verbose=True):
    path = f'{DOC_PATH}source/examples/{ex_category}/'
    os.makedirs(path, exist_ok=True)

    ex_name = LABEL_DICT[ex_tag]
    out_name = f'{path}{ex_tag}.rst'

    with open(out_name, 'w') as out_file:
        out_file.write(f'{ex_name}\n')
        out_file.write( '{}\n'.format('='*len(ex_name)))
        out_file.write( '\n')
        out_file.write(f'.. literalinclude:: ../../../../{RELEASE_PATH}Examples/Console/{ex_category}/example_{ex_tag}.py\n')
        # out_file.write(f'.. literalinclude:: ../../../../examples/{ex_category}/example_{ex_tag}.py\n')
        out_file.write( '   :language: python\n')
        out_file.write( '   :linenos:\n')

        if verbose:
            print(f'Saved \"{out_name}\"')
    return

def saveRstExampleList(verbose=True):
    folder_tag = 'examples'
    out_name = f'{DOC_PATH}source/{folder_tag}.rst'

    with open(out_name, 'w') as out_file:
        str_ = LABEL_DICT[folder_tag]
        out_file.write(f'{str_}\n')
        out_file.write( '{}\n'.format('='*len(str_)))

        for ex_category, ex_tag_list in EXAMPLE_DICT.items():
            str_ = LABEL_DICT[ex_category]
            out_file.write( '\n')
            out_file.write(f'{str_}\n')
            out_file.write( '{}\n'.format('-'*len(str_)))
            out_file.write( '\n')

            out_file.write(f'.. toctree::\n')
            out_file.write( '   :maxdepth: 4\n')
            out_file.write( '\n')

            for ex_tag in ex_tag_list:
                out_file.write(f'   {folder_tag}/{ex_category}/{ex_tag}\n')

        if verbose:
            print(f'Saved \"{out_name}\"')
    return

def saveRst_all(verbose=True):
    saveRstProductList(verbose=verbose)

    ## .rst file for individual product
    for _, prod_tag_list in PRODUCT_DICT.items():
        for prod_tag in prod_tag_list:
            saveRstProduct(prod_tag, verbose=verbose)

    saveRstExampleList(verbose=verbose)

    ## .rst file for individual example
    for ex_category, ex_tag_list in EXAMPLE_DICT.items():
        for ex_tag in ex_tag_list:
            saveRstExample(ex_category, ex_tag, verbose=verbose)

def removeRst_all(verbose=True):
    path = f'{DOC_PATH}source/products/'
    shutil.rmtree(path, True)
    path = f'{DOC_PATH}source/examples/'
    shutil.rmtree(path, True)

    if verbose:
        print(f'Removed .rst files')

def processRst():
    print()
    print('################################################################################')
    print('## Clean documentation')
    print()

    spc.check_call(['docs\make.bat', 'clean'], shell=True)
    removeRst_all()
    print()
    saveRst_all(verbose=True)

def processDocumentation():
    print()
    print('################################################################################')
    print('## Generate documentation')
    print()

    spc.check_call(['docs\make.bat', 'html'], shell=True)

################################################################################
## Make distribution

def incrementIfExist(name):
    name = name.rstrip('/\\')
    name_0 = name
    count = 0

    while os.path.isdir(name):
        count += 1
        name = f'{name_0}({count})'
    return name + '/'

def processDistribution(verbose=True):
    print()
    print('################################################################################')
    print('## Make distribution')
    print()

    full_dist_path = f'{DIST_PATH}{PKG_NAME}-{__version__}/'
    full_dist_path = incrementIfExist(full_dist_path)

    ## Copy library
    ## src = 'pywpc/**'
    ## dst = 'dist/pywpc-v0.1.13/pywpc/**'
    shutil.copytree(f'{LIB_PATH}', f'{full_dist_path}{LIB_PATH}', copy_function=shutil.copy2, dirs_exist_ok=True)

    ## Copy example codes
    # shutil.copytree(f'examples/', f'{full_dist_path}examples/', copy_function=shutil.copy2, dirs_exist_ok=True)

    ## Copy documentations
    ## src = 'docs/build/html/**'
    ## dst = 'dist/pywpc-v0.1.13/docs/**'
    shutil.copytree(f'{DOC_PATH}build/html/', f'{full_dist_path}{DOC_PATH}', copy_function=shutil.copy2, dirs_exist_ok=True)
    shutil.copytree(f'{DOC_PATH}build/html/', f'{RELEASE_PATH}{full_dist_path}{DOC_PATH}', copy_function=shutil.copy2, dirs_exist_ok=True)
    shutil.copytree(f'{DOC_PATH}build/html/', f'{RELEASE_PATH}{DOC_PATH}', copy_function=shutil.copy2, dirs_exist_ok=True)
    if verbose:
        print(f'Made a distribution at \"{full_dist_path}\"')

################################################################################
## Main function

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_list = sys.argv[1:]
    else:
        arg_list = ['all']

    if 'all' in arg_list or 'merge' in arg_list:
        processSingleSource()
    if 'all' in arg_list or 'lib' in arg_list or 'pyd' in arg_list or 'build' in arg_list:
        processLibrary()
    if 'all' in arg_list or 'clean' in arg_list:
        processRst()
    if 'all' in arg_list or 'docs' in arg_list:
        processDocumentation()
    if 'all' in arg_list or 'dist' in arg_list:
        processDistribution()

    print()
    print('## End')
    print('################################################################################')

## End of file
################################################################################

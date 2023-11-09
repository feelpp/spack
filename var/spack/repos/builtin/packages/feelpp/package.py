from spack import *

class Feelpp(CMakePackage):
    """A description of Feel++."""

    homepage = "https://docs.feelpp.org"
    git      = "https://github.com/feelpp/feelpp.git"

    maintainers = ['prudhomm']

    version('master', branch='master')

    # Specify minimum versions for dependencies and ensure petsc is compiled with mumps
    depends_on('cmake@3.22:', type='build')
    depends_on('boost@1.80:')
    depends_on('petsc@3.15:+mumps+metis+double')
    # Add other dependencies as necessary

    def cmake_args(self):
        args = []
        # Add any necessary CMake arguments here
        return args

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            cmake('--preset', 'feelpp')
            cmake('--build', '--preset', 'feelpp')
            # If ctest is included in the preset, it can be used here as well.

    def install(self, spec, prefix):
        # Custom installation logic, if necessary
        pass

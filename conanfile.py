from conans import ConanFile, CMake


class CrowConan(ConanFile):
    name = "crow"
    description = "Crow is very fast and easy to use C++ micro web framework (inspired by Python Flask)"
    version = "0.1"
    url = "https://github.com/ipkn/crow"
    license = "MIT; see https://github.com/ipkn/crow/blob/master/LICENSE"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"

    requires = (("boost/1.67.0@conan/stable"),
                ("OpenSSL/1.0.2@conan/stable"))

    # No exports necessary

    def source(self):
        # this will create a hello subfolder, take it into account
        self.run("git clone https://github.com/ipkn/crow.git")

    def build(self):
        cmake = CMake(self)
        self.run('cmake %s/crow %s' % (self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)
        self.run("make")

    def package(self):
        self.copy("*.h", dst="include", src="amalgamate")

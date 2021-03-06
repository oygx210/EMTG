# EMTG: Evolutionary Mission Trajectory Generator
# An open-source global optimization tool for preliminary mission design
# Provided by NASA Goddard Space Flight Center
#
# Copyright (c) 2013 - 2020 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Other Rights Reserved.
#
# Licensed under the NASA Open Source License (the "License"); 
# You may not use this file except in compliance with the License. 
# You may obtain a copy of the License at:
# https://opensource.org/licenses/NASA-1.3
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied.   See the License for the specific language
# governing permissions and limitations under the License.

def make_PyMissionOptions(journeyOptionsDefinitions, missionoptionsDefinitions, now):
    with open("PyMissionOptions.h","w") as file:

        file.write('//header file for PyMissionOptions class\n')
        file.write('//auto-generated by make_EMTG_missionoptions_journeyoptions.py\n')
        file.write('\n')
        file.write('#ifdef EMTG_OPTIONS_PYTHON_INTERFACE\n')
    
        file.write('#include "boost/python.hpp"\n')
        file.write('#include "boost/python/list.hpp"\n')
        file.write('#include "boost/python/extract.hpp"\n')
        file.write('\n')
        file.write('    BOOST_PYTHON_MODULE(PyMissionOptions)\n')
        file.write('    {\n')
        file.write('        using namespace EMTG;\n')
        file.write('\n')
        file.write('        boost::python::class_<JourneyOptions>("JourneyOptions", boost::python::init<std::string>())\n')
    
        for option in journeyOptionsDefinitions:
            if option['dataType'] == 'std::vector':
                print('do boost::python stuff for lists, not sure how')
            else:
                file.write('                                          .def_readwrite("' + option['name'] + '", &JourneyOptions::' + option['name'] + ')\n')
        file.write('                                          ;\n')
        file.write('\n')
        file.write('        boost::python::class_<missionoptions>("MissionOptions", boost::python::init<std::string>())\n')
        file.write('                                          .def_readwrite("Journeys", &missionoptions::Journeys)\n')
        file.write('                                          .def_readwrite("number_of_journeys", &missionoptions::number_of_journeys)\n')
    
        for option in missionoptionsDefinitions:
            if option['dataType'] == 'std::vector':
                print('do  boost::python stuff for lists, not sure how')
            else:
                file.write('                                          .def_readwrite("' + option['name'] + '", &missionoptions::' + option['name'] + ')\n')
        file.write('                                          ;\n')
        file.write('\n')
        file.write('\n')
        file.write('    }\n')
        file.write('#endif\n')
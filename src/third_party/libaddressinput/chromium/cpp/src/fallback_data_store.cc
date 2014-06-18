// Copyright (C) 2014 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "fallback_data_store.h"

#include <string>

namespace i18n {
namespace addressinput {

bool FallbackDataStore::Get(const std::string& key, std::string* data) {
  if (key != "data/US")
    return false;

  // Available at https://i18napis.appspot.com/ssl-aggregate-address/data/US
  data->assign(
      "{\"data/US/LA\": {\"lang\": \"en\", \"zipex\": \"70000,71599\", \"nam"
      "e\": \"Louisiana\", \"zip\": \"70|71[0-5]\", \"key\": \"LA\", \"id\":"
      " \"data/US/LA\"}, \"data/US/VT\": {\"lang\": \"en\", \"zipex\": \"0500"
      "0,05999\", \"name\": \"Vermont\", \"zip\": \"05\", \"key\": \"VT\", \""
      "id\": \"data/US/VT\"}, \"data/US/NM\": {\"lang\": \"en\", \"zipex\": \""
      "87000,88499\", \"name\": \"New Mexico\", \"zip\": \"87|88[0-4]\", \"k"
      "ey\": \"NM\", \"id\": \"data/US/NM\"}, \"data/US/NJ\": {\"lang\": \"e"
      "n\", \"zipex\": \"07000,08999\", \"name\": \"New Jersey\", \"zip\": \""
      "0[78]\", \"key\": \"NJ\", \"id\": \"data/US/NJ\"}, \"data/US/NH\": {\""
      "lang\": \"en\", \"zipex\": \"03000,03899\", \"name\": \"New Hampshire\""
      ", \"zip\": \"03[0-8]\", \"key\": \"NH\", \"id\": \"data/US/NH\"}, \"d"
      "ata/US/ND\": {\"lang\": \"en\", \"zipex\": \"58000,58999\", \"name\":"
      " \"North Dakota\", \"zip\": \"58\", \"key\": \"ND\", \"id\": \"data/US"
      "/ND\"}, \"data/US/NE\": {\"lang\": \"en\", \"zipex\": \"68000,69999\","
      " \"name\": \"Nebraska\", \"zip\": \"6[89]\", \"key\": \"NE\", \"id\":"
      " \"data/US/NE\"}, \"data/US/NC\": {\"lang\": \"en\", \"zipex\": \"2700"
      "0,28999\", \"name\": \"North Carolina\", \"zip\": \"2[78]\", \"key\":"
      " \"NC\", \"id\": \"data/US/NC\"}, \"data/US/PR\": {\"lang\": \"en\", \""
      "zipex\": \"00600,00799:00900,00999\", \"name\": \"Puerto Rico\", \"zi"
      "p\": \"00[679]\", \"key\": \"PR\", \"id\": \"data/US/PR\"}, \"data/US/"
      "RI\": {\"lang\": \"en\", \"zipex\": \"02800,02999\", \"name\": \"Rhode"
      " Island\", \"zip\": \"02[89]\", \"key\": \"RI\", \"id\": \"data/US/RI\""
      "}, \"data/US/NY\": {\"lang\": \"en\", \"zipex\": \"10000,14999:06390:"
      "00501:00544\", \"name\": \"New York\", \"zip\": \"1[0-4]|06390|00501|0"
      "0544\", \"key\": \"NY\", \"id\": \"data/US/NY\"}, \"data/US/NV\": {\"l"
      "ang\": \"en\", \"zipex\": \"88900,89999\", \"name\": \"Nevada\", \"zi"
      "p\": \"889|89\", \"key\": \"NV\", \"id\": \"data/US/NV\"}, \"data/US/K"
      "Y\": {\"lang\": \"en\", \"zipex\": \"40000,42799\", \"name\": \"Kentuc"
      "ky\", \"zip\": \"4[01]|42[0-7]\", \"key\": \"KY\", \"id\": \"data/US/K"
      "Y\"}, \"data/US/PA\": {\"lang\": \"en\", \"zipex\": \"15000,19699\", \""
      "name\": \"Pennsylvania\", \"zip\": \"1[5-8]|19[0-6]\", \"key\": \"PA\""
      ", \"id\": \"data/US/PA\"}, \"data/US/OH\": {\"lang\": \"en\", \"zipe"
      "x\": \"43000,45999\", \"name\": \"Ohio\", \"zip\": \"4[3-5]\", \"key\""
      ": \"OH\", \"id\": \"data/US/OH\"}, \"data/US/AS\": {\"lang\": \"en\","
      " \"zipex\": \"96799\", \"name\": \"American Samoa\", \"zip\": \"96799\""
      ", \"key\": \"AS\", \"id\": \"data/US/AS\"}, \"data/US/AA\": {\"lang\""
      ": \"en\", \"zipex\": \"34000,34099\", \"name\": \"Armed Forces (AA)\","
      " \"zip\": \"340\", \"key\": \"AA\", \"id\": \"data/US/AA\"}, \"data/US"
      "/GA\": {\"lang\": \"en\", \"zipex\": \"30000,31999:39800,39899:39901\""
      ", \"name\": \"Georgia\", \"zip\": \"3[01]|398|39901\", \"key\": \"GA\""
      ", \"id\": \"data/US/GA\"}, \"data/US/OK\": {\"lang\": \"en\", \"zipex\""
      ": \"73000,74999\", \"name\": \"Oklahoma\", \"zip\": \"7[34]\", \"key\""
      ": \"OK\", \"id\": \"data/US/OK\"}, \"data/US/CO\": {\"lang\": \"en\","
      " \"zipex\": \"80000,81999\", \"name\": \"Colorado\", \"zip\": \"8[01]\""
      ", \"key\": \"CO\", \"id\": \"data/US/CO\"}, \"data/US/AK\": {\"lang\""
      ": \"en\", \"zipex\": \"99500,99999\", \"name\": \"Alaska\", \"zip\": \""
      "99[5-9]\", \"key\": \"AK\", \"id\": \"data/US/AK\"}, \"data/US/WV\": "
      "{\"lang\": \"en\", \"zipex\": \"24700,26999\", \"name\": \"West Virgin"
      "ia\", \"zip\": \"24[7-9]|2[56]\", \"key\": \"WV\", \"id\": \"data/US/W"
      "V\"}, \"data/US/AL\": {\"lang\": \"en\", \"zipex\": \"35000,36999\", \""
      "name\": \"Alabama\", \"zip\": \"3[56]\", \"key\": \"AL\", \"id\": \"d"
      "ata/US/AL\"}, \"data/US/GU\": {\"lang\": \"en\", \"zipex\": \"96910,96"
      "932\", \"name\": \"Guam\", \"zip\": \"969([1-2]\\\\d|3[12])\", \"key\":"
      " \"GU\", \"id\": \"data/US/GU\"}, \"data/US/AR\": {\"lang\": \"en\", \""
      "zipex\": \"71600,72999\", \"name\": \"Arkansas\", \"zip\": \"71[6-9]|"
      "72\", \"key\": \"AR\", \"id\": \"data/US/AR\"}, \"data/US/AP\": {\"lan"
      "g\": \"en\", \"zipex\": \"96200,96699\", \"name\": \"Armed Forces (AP"
      ")\", \"zip\": \"96[2-6]\", \"key\": \"AP\", \"id\": \"data/US/AP\"}, \""
      "data/US/AZ\": {\"lang\": \"en\", \"zipex\": \"85000,86999\", \"name\""
      ": \"Arizona\", \"zip\": \"8[56]\", \"key\": \"AZ\", \"id\": \"data/US/"
      "AZ\"}, \"data/US/VI\": {\"lang\": \"en\", \"zipex\": \"00800,00899\","
      " \"name\": \"Virgin Islands\", \"zip\": \"008\", \"key\": \"VI\", \"i"
      "d\": \"data/US/VI\"}, \"data/US/CT\": {\"lang\": \"en\", \"zipex\": \""
      "06000,06999\", \"name\": \"Connecticut\", \"zip\": \"06\", \"key\": \""
      "CT\", \"id\": \"data/US/CT\"}, \"data/US/ME\": {\"lang\": \"en\", \"zi"
      "pex\": \"03900,04999\", \"name\": \"Maine\", \"zip\": \"039|04\", \"ke"
      "y\": \"ME\", \"id\": \"data/US/ME\"}, \"data/US/MD\": {\"lang\": \"en\""
      ", \"zipex\": \"20600,21999\", \"name\": \"Maryland\", \"zip\": \"20[6"
      "-9]|21\", \"key\": \"MD\", \"id\": \"data/US/MD\"}, \"data/US/IN\": {\""
      "lang\": \"en\", \"zipex\": \"46000,47999\", \"name\": \"Indiana\", \""
      "zip\": \"4[67]\", \"key\": \"IN\", \"id\": \"data/US/IN\"}, \"data/US/"
      "MA\": {\"lang\": \"en\", \"zipex\": \"01000,02799:05501:05544\", \"nam"
      "e\": \"Massachusetts\", \"zip\": \"01|02[0-7]|05501|05544\", \"key\":"
      " \"MA\", \"id\": \"data/US/MA\"}, \"data/US/IL\": {\"lang\": \"en\", \""
      "zipex\": \"60000,62999\", \"name\": \"Illinois\", \"zip\": \"6[0-2]\""
      ", \"key\": \"IL\", \"id\": \"data/US/IL\"}, \"data/US/MO\": {\"lang\":"
      " \"en\", \"zipex\": \"63000,65999\", \"name\": \"Missouri\", \"zip\":"
      " \"6[3-5]\", \"key\": \"MO\", \"id\": \"data/US/MO\"}, \"data/US/MN\":"
      " {\"lang\": \"en\", \"zipex\": \"55000,56799\", \"name\": \"Minnesota\""
      ", \"zip\": \"55|56[0-7]\", \"key\": \"MN\", \"id\": \"data/US/MN\"},"
      " \"data/US/IA\": {\"lang\": \"en\", \"zipex\": \"50000,52999\", \"nam"
      "e\": \"Iowa\", \"zip\": \"5[0-2]\", \"key\": \"IA\", \"id\": \"data/US"
      "/IA\"}, \"data/US/TN\": {\"lang\": \"en\", \"zipex\": \"37000,38599\","
      " \"name\": \"Tennessee\", \"zip\": \"37|38[0-5]\", \"key\": \"TN\", \""
      "id\": \"data/US/TN\"}, \"data/US/WY\": {\"lang\": \"en\", \"zipex\": \""
      "82000,83199:83414\", \"name\": \"Wyoming\", \"zip\": \"82|83[01]|8341"
      "4\", \"key\": \"WY\", \"id\": \"data/US/WY\"}, \"data/US/KS\": {\"lan"
      "g\": \"en\", \"zipex\": \"66000,67999\", \"name\": \"Kansas\", \"zip\""
      ": \"6[67]\", \"key\": \"KS\", \"id\": \"data/US/KS\"}, \"data/US/MI\":"
      " {\"lang\": \"en\", \"zipex\": \"48000,49999\", \"name\": \"Michigan\""
      ", \"zip\": \"4[89]\", \"key\": \"MI\", \"id\": \"data/US/MI\"}, \"data"
      "/US/ID\": {\"lang\": \"en\", \"zipex\": \"83200,83999\", \"name\": \"I"
      "daho\", \"zip\": \"83[2-9]\", \"key\": \"ID\", \"id\": \"data/US/ID\"}"
      ", \"data/US/MT\": {\"lang\": \"en\", \"zipex\": \"59000,59999\", \"nam"
      "e\": \"Montana\", \"zip\": \"59\", \"key\": \"MT\", \"id\": \"data/US/"
      "MT\"}, \"data/US/MS\": {\"lang\": \"en\", \"zipex\": \"38600,39799\","
      " \"name\": \"Mississippi\", \"zip\": \"38[6-9]|39[0-7]\", \"key\": \"M"
      "S\", \"id\": \"data/US/MS\"}, \"data/US/MP\": {\"lang\": \"en\", \"zip"
      "ex\": \"96950,96952\", \"name\": \"Northern Mariana Islands\", \"zip\""
      ": \"9695[0-2]\", \"key\": \"MP\", \"id\": \"data/US/MP\"}, \"data/US/P"
      "W\": {\"lang\": \"en\", \"zipex\": \"96940\", \"name\": \"Palau\", \"z"
      "ip\": \"969(39|40)\", \"key\": \"PW\", \"id\": \"data/US/PW\"}, \"data"
      "/US/SC\": {\"lang\": \"en\", \"zipex\": \"29000,29999\", \"name\": \"S"
      "outh Carolina\", \"zip\": \"29\", \"key\": \"SC\", \"id\": \"data/US/S"
      "C\"}, \"data/US/MH\": {\"lang\": \"en\", \"zipex\": \"96960,96979\", \""
      "name\": \"Marshall Islands\", \"zip\": \"969[67]\", \"key\": \"MH\","
      " \"id\": \"data/US/MH\"}, \"data/US/WI\": {\"lang\": \"en\", \"zipex\""
      ": \"53000,54999\", \"name\": \"Wisconsin\", \"zip\": \"5[34]\", \"key\""
      ": \"WI\", \"id\": \"data/US/WI\"}, \"data/US/SD\": {\"lang\": \"en\","
      " \"zipex\": \"57000,57999\", \"name\": \"South Dakota\", \"zip\": \"5"
      "7\", \"key\": \"SD\", \"id\": \"data/US/SD\"}, \"data/US/OR\": {\"lan"
      "g\": \"en\", \"zipex\": \"97000,97999\", \"name\": \"Oregon\", \"zip\""
      ": \"97\", \"key\": \"OR\", \"id\": \"data/US/OR\"}, \"data/US/UT\": {\""
      "lang\": \"en\", \"zipex\": \"84000,84999\", \"name\": \"Utah\", \"zi"
      "p\": \"84\", \"key\": \"UT\", \"id\": \"data/US/UT\"}, \"data/US/VA\":"
      " {\"lang\": \"en\", \"zipex\": \"20100,20199:22000,24699\", \"name\":"
      " \"Virginia\", \"zip\": \"201|2[23]|24[0-6]\", \"key\": \"VA\", \"id\""
      ": \"data/US/VA\"}, \"data/US/AE\": {\"lang\": \"en\", \"zipex\": \"090"
      "00,09999\", \"name\": \"Armed Forces (AE)\", \"zip\": \"09\", \"key\":"
      " \"AE\", \"id\": \"data/US/AE\"}, \"data/US/FL\": {\"lang\": \"en\", \""
      "zipex\": \"32000,33999:34100,34999\", \"name\": \"Florida\", \"zip\":"
      " \"3[23]|34[1-9]\", \"key\": \"FL\", \"id\": \"data/US/FL\"}, \"data/U"
      "S/FM\": {\"lang\": \"en\", \"zipex\": \"96941,96944\", \"name\": \"Mic"
      "ronesia\", \"zip\": \"9694[1-4]\", \"key\": \"FM\", \"id\": \"data/US/"
      "FM\"}, \"data/US/DE\": {\"lang\": \"en\", \"zipex\": \"19700,19999\","
      " \"name\": \"Delaware\", \"zip\": \"19[7-9]\", \"key\": \"DE\", \"id\""
      ": \"data/US/DE\"}, \"data/US/CA\": {\"lang\": \"en\", \"zipex\": \"900"
      "00,96199\", \"name\": \"California\", \"zip\": \"9[0-5]|96[01]\", \"ke"
      "y\": \"CA\", \"id\": \"data/US/CA\"}, \"data/US\": {\"lang\": \"en\","
      " \"upper\": \"CS\", \"sub_zipexs\": \"35000,36999~99500,99999~96799~85"
      "000,86999~71600,72999~34000,34099~09000,09999~96200,96699~90000,96199~"
      "80000,81999~06000,06999~19700,19999~20000,20099:20200,20599:56900,5699"
      "9~32000,33999:34100,34999~30000,31999:39800,39899:39901~96910,96932~96"
      "700,96798:96800,96899~83200,83999~60000,62999~46000,47999~50000,52999~"
      "66000,67999~40000,42799~70000,71599~03900,04999~96960,96979~20600,2199"
      "9~01000,02799:05501:05544~48000,49999~96941,96944~55000,56799~38600,39"
      "799~63000,65999~59000,59999~68000,69999~88900,89999~03000,03899~07000,"
      "08999~87000,88499~10000,14999:06390:00501:00544~27000,28999~58000,5899"
      "9~96950,96952~43000,45999~73000,74999~97000,97999~96940~15000,19699~00"
      "600,00799:00900,00999~02800,02999~29000,29999~57000,57999~37000,38599~"
      "75000,79999:88500,88599:73301:73344~84000,84999~05000,05999~00800,0089"
      "9~20100,20199:22000,24699~98000,99499~24700,26999~53000,54999~82000,83"
      "199:83414\", \"zipex\": \"95014,22162-1010\", \"name\": \"UNITED STATE"
      "S\", \"zip\": \"\\\\d{5}([ \\\\-]\\\\d{4})?\", \"zip_name_type\": \"zi"
      "p\", \"fmt\": \"%N%n%O%n%A%n%C %S %Z\", \"state_name_type\": \"state\""
      ", \"languages\": \"en\", \"sub_keys\": \"AL~AK~AS~AZ~AR~AA~AE~AP~CA~CO"
      "~CT~DE~DC~FL~GA~GU~HI~ID~IL~IN~IA~KS~KY~LA~ME~MH~MD~MA~MI~FM~MN~MS~MO~"
      "MT~NE~NV~NH~NJ~NM~NY~NC~ND~MP~OH~OK~OR~PW~PA~PR~RI~SC~SD~TN~TX~UT~VT~V"
      "I~VA~WA~WV~WI~WY\","
      " \"key\": \"US\", \"require\": \"ACSZ\", \"posturl\": \"https://tools."
      "usps.com/go/ZipLookupAction!input.action\", \"id\": \"dat"
      "a/US\", \"sub_names\": \"Alabama~Alaska~American Samoa~Arizona~Arkansa"
      "s~Armed Forces (AA)~Armed Forces (AE)~Armed Forces (AP)~California~Col"
      "orado~Connecticut~Delaware~District of Columbia~Florida~Georgia~Guam~H"
      "awaii~Idaho~Illinois~Indiana~Iowa~Kansas~Kentucky~Louisiana~Maine~Mars"
      "hall Islands~Maryland~Massachusetts~Michigan~Micronesia~Minnesota~Miss"
      "issippi~Missouri~Montana~Nebraska~Nevada~New Hampshire~New Jersey~New "
      "Mexico~New York~North Carolina~North Dakota~Northern Mariana Islands~O"
      "hio~Oklahoma~Oregon~Palau~Pennsylvania~Puerto Rico~Rhode Island~South "
      "Carolina~South Dakota~Tennessee~Texas~Utah~Vermont~Virgin Islands~Virg"
      "inia~Washington~West Virginia~Wisconsin~Wyoming\", \"sub_zips\": \"3[5"
      "6]~99[5-9]~96799~8[56]~71[6-9]|72~340~09~96[2-6]~9[0-5]|96[01]~8[01]~0"
      "6~19[7-9]~20[02-5]|569~3[23]|34[1-9]~3[01]|398|39901~969([1-2]\\\\d|3[12"
      "])~967[0-8]|9679[0-8]|968~83[2-9]~6[0-2]~4[67]~5[0-2]~6[67]~4[01]|42[0"
      "-7]~70|71[0-5]~039|04~969[67]~20[6-9]|21~01|02[0-7]|05501|05544~4[89]~"
      "9694[1-4]~55|56[0-7]~38[6-9]|39[0-7]~6[3-5]~59~6[89]~889|89~03[0-8]~0["
      "78]~87|88[0-4]~1[0-4]|06390|00501|00544~2[78]~58~9695[0-2]~4[3-5]~7[34"
      "]~97~969(39|40)~1[5-8]|19[0-6]~00[679]~02[89]~29~57~37|38[0-5]~7[5-9]|"
      "885|73301|73344~84~05~008~201|2[23]|24[0-6]~98|99[0-4]~24[7-9]|2[56]~5"
      "[34]~82|83[01]|83414\"}, \"data/US/TX\": {\"lang\": \"en\", \"zipex\":"
      " \"75000,79999:88500,88599:73301:73344\", \"name\": \"Texas\", \"zip\""
      ": \"7[5-9]|885|73301|73344\", \"key\": \"TX\", \"id\": \"data/US/TX\"}"
      ", \"data/US/WA\": {\"lang\": \"en\", \"zipex\": \"98000,99499\", \"nam"
      "e\": \"Washington\", \"zip\": \"98|99[0-4]\", \"key\": \"WA\", \"id\":"
      " \"data/US/WA\"}, \"data/US/DC\": {\"lang\": \"en\", \"zipex\": \"2000"
      "0,20099:20200,20599:56900,56999\", \"name\": \"District of Columbia\","
      " \"zip\": \"20[02-5]|569\", \"key\": \"DC\", \"id\": \"data/US/DC\"},"
      " \"data/US/HI\": {\"lang\": \"en\", \"zipex\": \"96700,96798:96800,968"
      "99\", \"name\": \"Hawaii\", \"zip\": \"967[0-8]|9679[0-8]|968\", \"key"
      "\": \"HI\", \"id\": \"data/US/HI\"}}");
  return true;
}

}  // namespace addressinput
}  // namespace i18n
import requests
from bs4 import BeautifulSoup
base_link = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2023-14&Breadth=ANY&Dept=+ALL&CourseNum=&Division=ANY&CourseCodes={code}&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Include&Bldg=&Room=&Submit=Display+Web+Results"


class shovel:


    def __init__(self, class_code):
        self.class_code = class_code
        self.soc_link = base_link.format(code=self.class_code)


    def check_status(self):
        """
        Checks the status of a class (open, waitlist, full)
        """

        code_data = self.get_code_data()

        return code_data['status']
    

    def get_raw_html(self):
        """
        Gets the raw html for the given code so it can be parsed
        """
        sesh = requests.session()
        soc_request = sesh.get(self.soc_link)
        soup = BeautifulSoup(soc_request.text, 'html.parser')
        code_data_html = soup.find_all('tr')[5].find_all('td')

        return code_data_html


    def get_code_data(self):
        """
        Gets all corresponding data for a given code
        """
        code_data_html = self.get_raw_html()
        class_data = ['code', 'type', 'section', 'units', 'insrtuctor', 'time', 'place', 'final', 'max', 'enrolled', 'waitlist', 'required', 'rstr', 'textbooks','status']
        class_data_dict = {class_data[i]:code_data_html[i].text for i in range(len(class_data))}

        return class_data_dict

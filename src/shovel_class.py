import requests
from bs4 import BeautifulSoup
base_link = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2023-14&Breadth=ANY&Dept=+ALL&CourseNum=&Division=ANY&CourseCodes={code}&InstrName=&CourseTitle=&ClassType=ALL&Units=&Days=&StartTime=&EndTime=&MaxCap=&FullCourses=ANY&FontSize=100&CancelledCourses=Include&Bldg=&Room=&Submit=Display+Web+Results"


class shovel:

    def __init__(self, class_code):
        self.class_code = class_code
        self.soc_link = base_link.format(code=self.class_code)
        self.raw_html = self.get_raw_html()

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

        return soup
    
    def get_course_headers(self):
        course_headers = list(self.raw_html.find("td", {"class": "CourseTitle"}))
        course_section = course_headers[0].text.strip().replace("\xa0", "")
        course_name = course_headers[1].text

        return {"dept_section": course_section, "course_name":course_name}

    def get_course_data(self):
        code_data_html = self.raw_html.find_all('tr')[5].find_all('td')
        class_data = ['code', 'type', 'section', 'units', 'insrtuctor', 'time', 'place', 'max', 'enrolled', 'waitlist', 'required', 'rstr', 'textbooks', 'web', 'status']
        class_data_dict = {class_data[i]:code_data_html[i].text for i in range(len(code_data_html))}

        return class_data_dict

    def course_summary(self):
        """
        Gets all corresponding data for a given code
        """
        course_dict = self.get_course_data()
        headers_dict = self.get_course_headers()

        return course_dict|headers_dict


    
if __name__ == "__main__":
    d = shovel(44200).course_summary()
    print(d)
# https://discord.com/api/oauth2/authorize?client_id=1088993845343178772&permissions=534723950656&scope=bot
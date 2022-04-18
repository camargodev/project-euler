from os import listdir
from os.path import isfile, join
import pathlib
from urllib import request
from bs4 import BeautifulSoup

class Solution:
    def __init__(self, name):
        self.id = (name.split("-"))[1].split(".")[0]
        self.name = name

    def get_documentation(self):
        fields = []
        fields.append("[" + self.__get_type_name(self.name) + "](https://github.com/camargodev/project-euler/src/" + self.name + ")")
        return fields

    def __get_type_name(self, name):
        types = {"py": "Python"}
        return types[(name.split("."))[1]]

class Problem:
    def __init__(self, problem_data):
        self.id = problem_data[0]
        self.url = "https://projecteuler.net/problem=" + self.id
        self.name = problem_data[1]

    def get_documentation(self):
        fields = []
        fields.append("#" + self.id)
        fields.append("[" + self.name + "](" + self.url + ")")
        return fields

def get_source_path():
    return str(pathlib.Path(__file__).parent.resolve())

def is_valid_file(source_path, file_name):
    return isfile(join(source_path, file_name)) and not file_name.startswith('.')

def get_source_file_names():
    source_path = get_source_path().replace("res", "src/")
    source_files = [entry for entry in listdir(source_path) if is_valid_file(source_path, entry)]
    return sorted(source_files)

def fetch_problems_data():
    problem_map = dict()
    page_request = request.urlopen("https://projecteuler.net/archives")
    page_content = page_request.read().decode('utf-8')
    page_html = BeautifulSoup(page_content, "html.parser")
    problems_table = page_html.find("table", {"id": "problems_table"})
    for problem in problems_table.find_all("tr"):
        problem_data = [column.text.strip() for column in problem.find_all('td')]
        if len(problem_data) == 0:
            continue
        problem_map[problem_data[0]] = Problem(problem_data)
    return problem_map

def make_solution_data():
    solution_file_names = get_source_file_names()
    return [Solution(solution_file_name) for solution_file_name in solution_file_names]

def make_solutions_documentation():
    documentation = []
    problems = fetch_problems_data()
    solutions = make_solution_data()
    documentation.append(make_header_line())
    for solution in solutions:
        problem = problems[solution.id]
        solution_line = make_solution_line(problem, solution)
        documentation.append(solution_line)
    return documentation

def make_header_line():
    return "|Id|Problem|Our solution|"

def make_solution_line(problem, solution):
    problem_fields = "|".join(problem.get_documentation())
    solution_fields = "|".join(solution.get_documentation())
    return "|" + problem_fields + "|" + solution_fields + "|"

def get_readme_path():
    return get_source_path().replace("res", "") + "README.md"

def read_readme(readme_path):
    readme = open(readme_path)
    # with open(readme_path) as readme:
    lines = readme.readlines()
    solution_table_header_index = lines.index("## Solution List\n")
    readme.close()
    return lines[0:solution_table_header_index+2]

def update_readme(readme_path):
    readme_content = read_readme(readme_path)
    solutions = make_solutions_documentation()
    for solution in solutions:
        readme_content.append(solution+"\n")
    readme = open(readme_path, "w")
    readme.writelines(readme_content)

update_readme(get_readme_path())
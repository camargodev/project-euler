from os import listdir
from os.path import isfile, join
import pathlib
from urllib import request
from bs4 import BeautifulSoup
from math import ceil

class Solution:
    def __init__(self, name):
        self.id = (name.split("-"))[1].split(".")[0]
        self.name = name

    def get_documentation(self):
        fields = []
        fields.append("[" + self.__get_type_name(self.name) + "](https://github.com/camargodev/project-euler/blob/main/src/" + self.name + ")")
        return fields

    def __get_type_name(self, name):
        types = {"py": "Python", "cpp": "C++"}
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
    file_names = [entry for entry in listdir(source_path) if is_valid_file(source_path, entry)]
    print("Found " + str(len(file_names)) + " problem solutions in " + source_path)
    return file_names

def fetch_problems_data_from_page(source_url):
    print("Fetching data from page " + source_url)
    problem_map = dict()
    page_request = request.urlopen(source_url)
    page_content = page_request.read().decode('utf-8')
    page_html = BeautifulSoup(page_content, "html.parser")
    problems_table = page_html.find("table", {"id": "problems_table"})
    for problem in problems_table.find_all("tr"):
        problem_data = [column.text.strip() for column in problem.find_all('td')]
        if len(problem_data) == 0:
            continue
        problem_map[add_leading_zeros(problem_data[0])] = Problem(problem_data)
    return problem_map

def add_leading_zeros(id):
    number_of_zeros = 3 - len(id)
    leading_zeros = "0" * number_of_zeros
    return leading_zeros + id

def make_solution_data():
    solution_file_names = get_source_file_names()
    return [Solution(solution_file_name) for solution_file_name in solution_file_names]

def get_highest_id(solutions):
    ids = [int(solution.id) for solution in solutions]
    return max(ids)

def fetch_problems_data(solutions):
    all_problems = dict()
    pages_urls = get_problem_pages_urls(solutions)
    for page_url in pages_urls:
        problems_of_page = fetch_problems_data_from_page(page_url)
        all_problems = all_problems | problems_of_page
    print("Found problem data for " + str(len(all_problems)) + " problems")
    return all_problems

def get_problem_pages_urls(solutions):
    problems_by_page = 50
    highest_problem_id = get_highest_id(solutions)
    number_of_pages = ceil(highest_problem_id/problems_by_page)
    return [get_problems_page_url(index+1) for index in range(number_of_pages)]

def get_problems_page_url(page_index):
    base_url = "https://projecteuler.net/archives"
    page_index_append = ";page=" + str(page_index)
    return base_url if page_index == 1 else base_url + page_index_append

def make_solutions_documentation():
    documentation = []
    solutions = make_solution_data()
    problems = fetch_problems_data(solutions)
    documentation.extend(make_header_lines())
    sorted_solutions = sorted(solutions, key=lambda x:int(x.id))
    for solution in sorted_solutions:
        problem = problems[solution.id]
        print("Processing problem " + solution.id)
        solution_line = make_solution_line(problem, solution)
        documentation.append(solution_line)
    return documentation

def make_header_lines():
    return ["|Id|Problem|Our solution|", "|-|-|-|"]

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
    print("Current readme has " + str(len(lines)) + " lines")
    solution_table_header_index = lines.index("## Solution List\n")
    readme.close()
    print("The first " + str(solution_table_header_index+1) + " will remain equal")
    return lines[0:solution_table_header_index+2]

def update_readme(readme_path):
    solutions = make_solutions_documentation()
    readme_content = read_readme(readme_path)
    for solution in solutions:
        readme_content.append(solution+"\n")
    print(str(len(solutions)+1) + " lines will be added to readme")
    readme = open(readme_path, "w")
    readme.writelines(readme_content)

update_readme(get_readme_path())
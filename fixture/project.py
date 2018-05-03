from sys import maxsize


class ProjectHelper:

    row_selector = "div.table-responsive:nth-child(2) tbody tr"
    name_field = "div.table-responsive:nth-child(2) tbody tr td a"

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        self.init_create_project()
        self.fill_project_form(project.name)
        self.click_proceed()

    def init_create_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("[type='submit']").click()

    def go_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, name):
        wd = self.app.wd
        wd.find_element_by_css_selector('input#project-name').send_keys(name)
        wd.find_element_by_css_selector("[type='submit']").click()

    def click_proceed(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".skin-3").click()

    def get_projects_list(self):
        wd = self.app.wd
        result_list = []
        if 'manage_proj_page.php' not in wd.current_url:
            self.go_to_projects_page()
        if self.projects_count() == 0:
            return result_list
        else:
            for row in wd.find_elements_by_css_selector(self.row_selector):
                result_list.append(row.find_element_by_css_selector(self.name_field).text)
        return result_list

    def projects_count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector(self.row_selector))

    def delete_some_project(self, name):
        wd = self.app.wd
        assert self.projects_count() > 0
        self.go_to_project(name)
        wd.find_element_by_css_selector("[value='Delete Project']").click()
        wd.find_element_by_css_selector(".center [value='Delete Project']").click()

    def go_to_project(self, name):
        wd = self.app.wd
        for row in wd.find_elements_by_css_selector(self.row_selector):
            element = row.find_element_by_css_selector(self.name_field)
            if element.text == name:
                element.click()
                break

    def id_or_max(self, project):
        if project.id:
            return int(project.id)
        else:
            return maxsize

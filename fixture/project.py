

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, name):
        self.init_create_project()
        self.fill_project_form(name)
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
        rows = wd.find_elements_by_css_selector("div.table-responsive:nth-child(2) tbody tr")
        if len(rows) == 0:
            return result_list
        else:
            for row in rows:
                result_list.append(row.find_element_by_css_selector("div.table-responsive:nth-child(2) tbody tr td a")
                                   .text)
        return result_list

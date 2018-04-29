

def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.go_to_projects_page()
    project_name = 'project_02'
    old_project_list = app.project.get_projects_list()
    app.project.create_project(project_name)
    new_project_list = app.project.get_projects_list()
    old_project_list.append(project_name)
    assert sorted(old_project_list) == sorted(new_project_list)

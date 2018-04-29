import random


def test_delete_project(app):
    app.session.login('administrator', 'root')
    app.project.go_to_projects_page()
    old_project_list = app.project.get_projects_list()
    if len(old_project_list) == 0:
        app.project.create_project('created project')
        old_project_list = app.project.get_projects_list()
    project_for_deletion = random.choice(old_project_list)
    app.project.delete_some_project(project_for_deletion)
    new_project_list = app.project.get_projects_list()
    old_project_list.remove(project_for_deletion)
    assert sorted(old_project_list) == sorted(new_project_list)
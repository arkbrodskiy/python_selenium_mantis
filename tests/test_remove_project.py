import random

from model.project import Project


def test_delete_project(app):
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    app.project.go_to_projects_page()
    old_project_list = app.soap.get_projects_list(username, password)
    if len(old_project_list) == 0:
        app.project.create_project(Project(name='created project'))
        old_project_list = app.soap.get_projects_list(username, password)
    project_for_deletion = random.choice(old_project_list)
    app.project.delete_project(project_for_deletion)
    new_project_list = app.soap.get_projects_list(username, password)
    old_project_list.remove(project_for_deletion)
    assert sorted(old_project_list, key=app.project.id_or_max) == sorted(new_project_list, key=app.project.id_or_max)
